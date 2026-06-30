# Copyright (C) 2011-2016 Ilias Stamatis <stamatis.iliass@gmail.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import os
import sys
import re
import io
import signal
import threading
import subprocess
import shlex
import logging

from PyQt5.QtCore import pyqtSignal, QTimer
from PyQt5.QtGui import QTextCursor
from PyQt5.QtWidgets import (
        QApplication, QDialog, QFrame, QLabel, QPushButton, QProgressBar,
        QMessageBox, QTextEdit, QCommandLinkButton, QSizePolicy, QCheckBox
        )

from ffmulticonverter import utils


class Progress(QDialog):
    file_converted_signal = pyqtSignal()
    update_text_edit_signal = pyqtSignal(str)

    def __init__(self, files, tab, delete, parent, test=False):
        """
        Keyword arguments:
        files  -- list with dicts containing file names
        tab -- instanseof AudioVideoTab, ImageTab or DocumentTab
               indicating currently active tab
        delete -- boolean that shows if files must removed after conversion
        parent -- parent widget

        files:
        Each dict have only one key and one corresponding value.
        Key is a file to be converted and it's value is the name of the new
        file that will be converted.

        Example list:
        [{"/foo/bar.png" : "/foo/bar.bmp"}, {"/f/bar2.png" : "/f/bar2.bmp"}]
        """
        super(Progress, self).__init__(parent)
        self.parent = parent

        self.files = files
        self.num_total_files = len(self.files)
        self.tab = tab
        self.delete = delete
        if not test:
            self._type = tab.name
        self.ok = 0
        self.error = 0
        self.running = True

        self.nowQL = QLabel(self.tr('In progress: '))
        self.nowQPBar = QProgressBar()
        self.nowQPBar.setValue(0)
        self.shutdownQCB = QCheckBox(self.tr('Shutdown after conversion'))
        self.cancelQPB = QPushButton(self.tr('Cancel'))

        detailsQPB = QCommandLinkButton(self.tr('Details'))
        detailsQPB.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        detailsQPB.setCheckable(True)
        detailsQPB.setMaximumWidth(113)
        line = QFrame()
        line.setFrameShape(QFrame.HLine)
        line.setFrameShadow(QFrame.Sunken)
        self.outputQTE = QTextEdit()
        self.outputQTE.setReadOnly(True)
        self.frame = QFrame()
        frame_layout = utils.add_to_layout('h', self.outputQTE)
        self.frame.setLayout(frame_layout)
        self.frame.hide()

        hlayout1 = utils.add_to_layout('h', None, self.nowQL, None)
        hlayout2 = utils.add_to_layout('h', detailsQPB, line)
        hlayout3 = utils.add_to_layout('h', self.frame)
        hlayout4 = utils.add_to_layout('h', None, self.cancelQPB)
        vlayout = utils.add_to_layout(
                'v', hlayout1, self.nowQPBar, hlayout2, hlayout3,
                self.shutdownQCB, hlayout4
                )
        self.setLayout(vlayout)

        detailsQPB.toggled.connect(self.resize_dialog)
        detailsQPB.toggled.connect(self.frame.setVisible)
        self.cancelQPB.clicked.connect(self.reject)
        self.file_converted_signal.connect(self.next_file)
        self.update_text_edit_signal.connect(self.update_text_edit)

        self.resize(484, 190)
        self.setWindowTitle('FF Multi Converter - ' + self.tr('Conversion'))

        if not test:
            self.get_data() # should be first and not in QTimer.singleShot()
            QTimer.singleShot(0, self.manage_conversions)

    def get_data(self):
        """Collect conversion data from parents' widgets."""
        if self._type == 'AudioVideo':
            self.cmd = self.tab.commandQLE.text()
        elif self._type == 'Images':
            width = self.tab.widthQLE.text()
            self.size = ''
            self.mntaspect = False
            if width:
                height = self.tab.heightQLE.text()
                self.size = '{0}x{1}'.format(width, height)
                self.mntaspect = self.tab.imgaspectQChB.isChecked()
            self.imgcmd = self.tab.commandQLE.text()
            if self.tab.autocropQChB.isChecked():
                self.imgcmd += ' -trim +repage'
            rotate = self.tab.rotateQLE.text().strip()
            if rotate:
                self.imgcmd += ' -rotate {0}'.format(rotate)
            if self.tab.vflipQChB.isChecked():
                self.imgcmd += ' -flip'
            if self.tab.hflipQChB.isChecked():
                self.imgcmd += ' -flop'

    def resize_dialog(self):
        """Resize dialog"""
        height = 190 if self.frame.isVisible() else 450
        self.setMinimumSize(484, height)
        self.resize(484, height)

    def update_text_edit(self, txt):
        """Append txt to the end of current self.outputQTE's text."""
        current = self.outputQTE.toPlainText()
        self.outputQTE.setText(current+txt)
        self.outputQTE.moveCursor(QTextCursor.End)

    def manage_conversions(self):
        """
        Check whether all files have been converted.
        If not, it will allow convert_a_file() to convert the next file.
        """
        if not self.running:
            return
        if not self.files:
            sum_files = self.ok + self.error
            msg = QMessageBox(self)
            msg.setStandardButtons(QMessageBox.Ok)
            msg.setWindowTitle(self.tr("Report"))
            msg.setText(self.tr("Converted: {0}/{1}".format(self.ok,sum_files)))
            msg.setModal(False)
            msg.show()

            self.cancelQPB.setText(self.tr("Close"))

            if self.shutdownQCB.isChecked():
                if sys.platform.startswith('win'):
                    # Windows shutdown
                    subprocess.call(['shutdown', '/s', '/t', '0'])
                else:
                    if utils.is_installed('systemctl'):
                        subprocess.call(['systemctl', 'poweroff'])
                    else:
                        subprocess.call(['shutdown', '-h', 'now'])
        else:
            self.convert_a_file()

    def next_file(self):
        """
        Update progress bar value, remove converted file from self.files
        and call manage_conversions() to continue the process.
        """
        self.nowQPBar.setValue(100)
        QApplication.processEvents()
        self.files.pop(0)
        self.manage_conversions()

    def reject(self):
        """
        Use standard dialog to ask whether procedure must stop or not.
        Use the SIGSTOP to stop the conversion process while waiting for user
        to respond and SIGCONT or kill depending on user's answer.
        """
        if not self.files:
            QDialog.accept(self)
            return
        if self._type == 'AudioVideo':
            self.process.send_signal(signal.SIGSTOP)
        self.running = False
        reply = QMessageBox.question(
                self,
                'FF Multi Converter - ' + self.tr('Cancel Conversion'),
                self.tr('Are you sure you want to cancel conversion?'),
                QMessageBox.Yes|QMessageBox.Cancel
                )
        if reply == QMessageBox.Yes:
            if self._type == 'AudioVideo':
                self.process.kill()
            self.running = False
            self.thread.join()
            QDialog.reject(self)
        if reply == QMessageBox.Cancel:
            self.running = True
            if self._type == 'AudioVideo':
                self.process.send_signal(signal.SIGCONT)
            else:
                self.manage_conversions()

    def convert_a_file(self):
        """
        Update self.nowQL's text with current file's name, set self.nowQPBar
        value to zero and start the conversion procedure in a second thread
        using threading module.
        """
        if not self.files:
            return
        from_file = list(self.files[0].keys())[0]
        to_file = list(self.files[0].values())[0]

        text = os.path.basename(from_file[1:-1])
        num_file = self.num_total_files - len(self.files) + 1
        text += ' ({0}/{1})'.format(num_file, self.num_total_files)

        self.nowQL.setText(self.tr('In progress:') + ' ' + text)
        self.nowQPBar.setValue(0)

        if not os.path.exists(from_file[1:-1]):
            self.error += 1
            self.file_converted_signal.emit()
            return

        def convert():
            if self._type == 'AudioVideo':
                conv_func = self.convert_video
                params = (from_file, to_file, self.cmd)
            elif self._type == 'Images':
                conv_func = self.convert_image
                params = (from_file, to_file, self.size, self.mntaspect,
                          self.imgcmd)
            else:
                conv_func = self.convert_document
                params = (from_file, to_file)

            if conv_func(*params):
                self.ok += 1
                if self.delete and not from_file == to_file:
                    try:
                        os.remove(from_file[1:-1])
                    except OSError:
                        pass
            else:
                self.error += 1

            self.file_converted_signal.emit()

        self.thread = threading.Thread(target=convert)
        self.thread.start()

    def convert_video(self, from_file, to_file, command):
        """
        Create the ffmpeg command and execute it in a new process using the
        subprocess module. While the process is alive, parse ffmpeg output,
        estimate conversion progress using video's duration.
        With the result, emit the corresponding signal in order progress bar
        to be updated. Also emit regularly the corresponding signal in order
        an outputQTE to be updated with ffmpeg's output. Finally, save log
        information.

        Return True if conversion succeed, else False.
        """
        # note: from_file and to_file names are inside quotation marks
        in_path = from_file[1:-1] if from_file.startswith('"') and from_file.endswith('"') else from_file
        out_path = to_file[1:-1] if to_file.startswith('"') and to_file.endswith('"') else to_file

        ffmpeg = self.parent.ffmpeg_path or 'ffmpeg'

        # 'command' is a free-form string of ffmpeg args built by the UI/presets.
        extra_args = shlex.split(command, posix=not sys.platform.startswith('win')) if command else []

        args = [ffmpeg, '-y', '-i', in_path] + extra_args + [out_path]
        cmd_display = ' '.join([f'"{a}"' if (' ' in a and not a.startswith('"')) else a for a in args])
        self.update_text_edit_signal.emit(cmd_display + '\n')

        self.process = subprocess.Popen(
                args,
                stderr=subprocess.STDOUT,
                stdout=subprocess.PIPE
                )

        final_output = myline = ''
        reader = io.TextIOWrapper(self.process.stdout, encoding='utf8', errors='replace')
        while True:
            out = reader.read(1)
            if out == '' and self.process.poll() is not None:
                break
            myline += out
            if out in ('\r', '\n'):
                m = re.search("Duration: ([0-9:.]+)", myline)
                if m:
                    total = utils.duration_in_seconds(m.group(1))
                n = re.search("time=([0-9:]+)", myline)
                # time can be of format 'time=hh:mm:ss.ts' or 'time=ss.ts'
                # depending on ffmpeg version
                if n:
                    time = n.group(1)
                    if ':' in time:
                        time = utils.duration_in_seconds(time)
                    now_sec = int(float(time))
                    try:
                        self.nowQPBar.setValue(int(100 * (now_sec / total)))
                    except (UnboundLocalError, ZeroDivisionError):
                        pass
                self.update_text_edit_signal.emit(myline)
                final_output += myline
                myline = ''
        self.update_text_edit_signal.emit('\n\n')

        return_code = self.process.poll()

        log_data = {
                'command' : cmd_display,
                'returncode' : return_code,
                'type' : 'VIDEO'
                }
        log_lvl = logging.info if return_code == 0 else logging.error
        log_lvl(final_output, extra=log_data)

        return return_code == 0


    def convert_image(self, from_file, to_file, size, mntaspect, imgcmd):
        """Convert image using ImageMagick.

        On Windows we must call ImageMagick via **magick.exe** because
        Windows ships its own convert.exe.
        """
        # note: from_file and to_file names are inside quotation marks
        in_path = from_file[1:-1] if from_file.startswith('"') and from_file.endswith('"') else from_file
        out_path = to_file[1:-1] if to_file.startswith('"') and to_file.endswith('"') else to_file

        resize = ''
        if size:
            width, height = size.split('x')
            # add '!' for non-aspect preserving resize
            resize = f'-resize {width}x{height}'
            if not mntaspect:
                resize += '!'

        # Build argument list safely (avoid shlex issues on Windows)
        if sys.platform.startswith('win'):
            im_cmd = self.parent.imagemagick or 'magick'
            args = [im_cmd, 'convert', in_path]
        else:
            # Linux: allow either `convert` or `magick`
            im_cmd = self.parent.imagemagick or 'convert'
            if os.path.basename(im_cmd).lower().startswith('magick'):
                args = [im_cmd, 'convert', in_path]
            else:
                args = [im_cmd, in_path]

        if resize:
            args += resize.split()

        imgcmd = (imgcmd or '').strip()
        if imgcmd:
            # imgcmd is a free-form string typed/selected in the UI
            args += shlex.split(imgcmd, posix=not sys.platform.startswith('win'))

        args.append(out_path)

        cmd_display = ' '.join([f'"{a}"' if (' ' in a and not a.startswith('"')) else a for a in args])
        self.update_text_edit_signal.emit(cmd_display + '\n')

        child = subprocess.Popen(
                args,
                stderr=subprocess.STDOUT,
                stdout=subprocess.PIPE
                )
        child.wait()

        reader = io.TextIOWrapper(child.stdout, encoding='utf8', errors='replace')
        final_output = reader.read()
        self.update_text_edit_signal.emit(final_output + '\n\n')

        return_code = child.poll()

        log_data = {
                'command': cmd_display,
                'returncode': return_code,
                'type': 'IMAGE'
                }
        log_lvl = logging.info if return_code == 0 else logging.error
        log_lvl(final_output, extra=log_data)

        return return_code == 0

    def convert_document(self, from_file, to_file):
        """Convert documents.

        - Linux: uses unoconv (if installed)
        - Windows: uses LibreOffice directly via soffice --headless --convert-to
        """
        # note: from_file and to_file names are inside quotation marks
        in_path = from_file[1:-1] if from_file.startswith('"') and from_file.endswith('"') else from_file
        out_path = to_file[1:-1] if to_file.startswith('"') and to_file.endswith('"') else to_file

        to_dir = os.path.dirname(out_path) or os.getcwd()
        to_base = os.path.splitext(os.path.basename(out_path))[0]
        to_ext = os.path.splitext(out_path)[1].lstrip('.')

        converter = getattr(self.parent, 'doc_converter', 'unoconv')

        if converter == 'unoconv':
            args = ['unoconv', '-f', to_ext, '-o', out_path, in_path]
            cmd_display = ' '.join([f'"{a}"' if ' ' in a else a for a in args])
            self.update_text_edit_signal.emit(cmd_display + '\n')
            child = subprocess.Popen(args, stderr=subprocess.STDOUT, stdout=subprocess.PIPE)
            child.wait()
            reader = io.TextIOWrapper(child.stdout, encoding='utf8', errors='replace')
            final_output = reader.read()
            self.update_text_edit_signal.emit(final_output + '\n\n')
            return_code = child.poll()
        else:
            soffice = getattr(self.parent, 'soffice', None) or 'soffice'
            # Prefer soffice.com if present (better for console output on Windows)
            if sys.platform.startswith('win'):
                soffice = getattr(self.parent, 'soffice', None) or utils.is_installed('soffice.com') or utils.is_installed('soffice') or 'soffice'

            # LibreOffice outputs in --outdir using the input base name.
            args = [soffice, '--headless', '--nologo', '--convert-to', to_ext, '--outdir', to_dir, in_path]
            cmd_display = ' '.join([f'"{a}"' if (' ' in a and not a.startswith('"')) else a for a in args])
            self.update_text_edit_signal.emit(cmd_display + '\n')

            child = subprocess.Popen(args, stderr=subprocess.STDOUT, stdout=subprocess.PIPE)
            child.wait()
            reader = io.TextIOWrapper(child.stdout, encoding='utf8', errors='replace')
            final_output = reader.read()
            self.update_text_edit_signal.emit(final_output + '\n\n')
            return_code = child.poll()

            # Rename if LibreOffice created a different filename than requested.
            produced = os.path.join(to_dir, os.path.splitext(os.path.basename(in_path))[0] + '.' + to_ext)
            if return_code == 0 and os.path.exists(produced):
                if os.path.abspath(produced) != os.path.abspath(out_path):
                    try:
                        # If destination exists, overwrite
                        if os.path.exists(out_path):
                            os.remove(out_path)
                        os.replace(produced, out_path)
                    except OSError:
                        # If rename fails, leave the produced file in place.
                        pass

        log_data = {
                'command': cmd_display,
                'returncode': return_code,
                'type': 'DOCUMENT'
                }
        log_lvl = logging.info if return_code == 0 else logging.error
        log_lvl(final_output, extra=log_data)

        return return_code == 0
