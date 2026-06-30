import os


#-----general data

home = os.path.expanduser("~")
config_dir = os.path.join(home, '.config/ffmulticonverter/')

default_ffmpeg_cmd = ''
default_imagemagick_cmd = ''

#-----log data

log_dir = os.path.join(config_dir, 'logs/')
log_file = os.path.join(log_dir, 'history.log')
log_format  = '%(asctime)s : %(levelname)s - %(type)s\n' +\
              'Command: %(command)s\n' +\
              'Return code: %(returncode)s\n%(message)s\n'
log_dateformat = '%Y-%m-%d %H:%M:%S'

#-----presets data

presets_file_name = 'presets.xml'
presets_file = os.path.join(config_dir, presets_file_name)
presets_lookup_dirs = ["/usr/local/share/", "/usr/share/"]
presets_lookup_virtenv = 'share'
# prefix for old presets when synchronizing
presets_old = '__OLD'

#-----audiovideo data

video_codecs = [
        'copy', 'ffv1', 'flv', 'h263', 'libaom-av1', 'libsvtav1', 'libtheora',
        'libvpx', 'libvpx-vp9', 'libx264', 'libx265', 'libxvid',
        'mpeg2video', 'mpeg4', 'msmpeg4', 'prores', 'vp9', 'wmv2'
        ]

audio_codecs = [
        'aac', 'ac3', 'alac', 'copy', 'eac3', 'flac', 'libfdk_aac', 'libmp3lame',
        'libopus', 'libvorbis', 'mp2', 'opus', 'pcm_s16le', 'wavpack', 'wmav2'
        ]

video_formats = [
        '3g2', '3gp', 'aac', 'ac3', 'aif', 'aiff', 'amr', 'ape', 'au', 'avi',
        'caf', 'dv', 'eac3', 'flac', 'flv', 'gif', 'h264', 'h265', 'hevc',
        'm2ts', 'm4a', 'm4b', 'm4r', 'm4v', 'mka', 'mkv', 'mov', 'mp2', 'mp3',
        'mp4', 'mpg', 'mts', 'mxf', 'oga', 'ogg', 'ogv', 'opus', 'ts', 'vob',
        'wav', 'webm', 'wma', 'wmv', 'wv'
        ]

video_frequency_values = [
        '22050', '44100', '48000'
        ]

video_bitrate_values = [
        '32', '96', '112', '128', '160', '192', '256', '320'
        ]

#-----image data

image_formats = [
        'apng', 'avif', 'bmp', 'cgm', 'dds', 'dng', 'dpx', 'emf', 'eps', 'exr',
        'fpx', 'gif', 'hdr', 'heic', 'heif', 'ico', 'j2k', 'jbig', 'jng',
        'jp2', 'jpeg', 'jpg', 'jxl', 'mrsid', 'p7', 'pdf', 'picon', 'png',
        'ppm', 'psd', 'rad', 'svg', 'tga', 'tif', 'tiff', 'webp', 'xpm'
        ]

image_extra_formats = [
        'bmp2', 'bmp3', 'dib', 'epdf', 'epi', 'eps2', 'eps3', 'epsf', 'epsi',
        'icon', 'jpe', 'jpt', 'j2c', 'pgm', 'png24', 'png32', 'pnm', 'ps',
        'ps2', 'ps3', 'sid'
        ]

#-----document data

document_formats = [
        'bib', 'csv', 'dif', 'doc', 'docm', 'docx', 'dot', 'dotx', 'epub',
        'fodp', 'fods', 'fodt', 'html', 'ltx', 'odp', 'ods', 'odt', 'otp',
        'ots', 'ott', 'pdf', 'pot', 'potx', 'pps', 'ppsx', 'ppt', 'pptx',
        'rtf', 'sdc', 'sdw', 'txt', 'xls', 'xlsm', 'xlsx', 'xlt', 'xltx',
        'xhtml', 'xml'
        ]


#-----misc
translators = [
        ['[bg] Bulgarian', 'Vasil Blagoev'],
        ['[ca] Catalan', 'David Sabadell i Ximenes'
                  '\n     Toni Estévez'],
        ['[cs] Czech', 'Petr Simacek'],
        ['[de_DE] German (Germany)', 'Stefan Wilhelm'],
        ['[el] Greek', 'Ilias Stamatis'],
        ['[es] Spanish', 'Miguel Ángel Rodríguez Muíños'
                  '\n     Toni Estévez'],
        ['[fr] French', 'Rémi Mercier'
                 '\n     Lebarhon'],
        ['[gl] Galician', 'Miguel Anxo Bouzada'],
        ['[gl_ES] Galician (Spain)', 'Miguel Anxo Bouzada'],
        ['[hu] Hungarian', 'Farkas Norbert'],
        ['[it] Italian', 'Fabio Boccaletti'],
        ['[ms_MY] Malay (Malaysia)', 'abuyop'],
        ['[pl_PL] Polish (Poland)', 'Lukasz Koszy'
                             '\n     Piotr Surdacki'],
        ['[pt] Portuguese', 'Sérgio Marques'
                     '\n     Paulo Braz'
                     '\n     Nuno Duarte'],
        ['[pt_BR] Portuguese (Brasil)', 'José Humberto A Melo'],
        ['[ro_RO] Romanian (Romania)', 'Angelescu Constantin'],
        ['[ru] Russian', 'Andrew Lapshin'],
        ['[tu] Turkish', 'Tayfun Kayha'],
        ['[vi] Vietnamese', 'Anh Phan'],
        ['[zh_CN] Chinese (China)', 'Dianjin Wang'
                             '\n     Ziyun Lin'],
        ['[zh_TW] Chinese (Taiwan)', 'Taijuin Lee'
                              '\n     Jeff Huang'],
        ]
