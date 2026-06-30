FF Multi Converter
====================

FF Multi Converter is a simple graphical application which enables you
to convert audio, video, image and document files between all popular formats,
by utilizing and combining other programs. It uses ffmpeg for audio/video files,
unoconv or LibreOffice for document files and ImageMagick for image file
conversions.

Project homepage: https://sites.google.com/site/ffmulticonverter/

Dependencies
-------------
python3
pyqt5

Optional dependencies
----------------------
ffmpeg
imagemagick
unoconv
LibreOffice (soffice, used for document conversion on Windows and as fallback)

The program does NOT require the optional dependencies to run.
e.g. you can run the application even if you don't have ImageMagick installed,
but you will be able to convert any other types except image files.

Installation
-------------
From application's directory run as root:
    python3 setup.py install

On Windows, install Python dependencies with:
    python -m pip install -r requirements.txt

and run:
    python -m ffmulticonverter.ffmulticonverter

Uninstall
----------
Run the uninstall.sh script as root to delete all project files from your
system.

Run without installing
-----------------------
You can even launch the application without installing it, by running the
launcher script. This option has not been extensively tested for everyday use
though, and you may experience unexpected issues.
