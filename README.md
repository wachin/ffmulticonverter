# FF Multi Converter

FF Multi Converter is a graphical application for converting audio, video,
image and document files by combining external tools.

This repository keeps one upstream codebase with Linux and Windows support.
The Debian packaging remains Linux-focused in `debian/`.

## Runtime dependencies

Common:

- Python 3
- PyQt5
- FFmpeg
- ImageMagick

Linux document conversion:

- unoconv

Windows document conversion:

- LibreOffice, available as `soffice.com` or `soffice` in `PATH`

## Run from source

Clone or download:

[https://github.com/wachin/ffmulticonverter](https://github.com/wachin/ffmulticonverter)

### Linux:

On Debian-based distributions such as Debian, Ubuntu, and Linux Mint, install
the required runtime dependencies with:

```sh
sudo apt install python3-pyqt5 ffmpeg unoconv imagemagick
```

Then run from a terminal in the root folder:

```sh
python3 -m ffmulticonverter.ffmulticonverter
```

### Windows:

Open PowerShell

```powershell
python -m pip install -r requirements.txt
python -m ffmulticonverter.ffmulticonverter
```

## Debian packaging

The `debian/` directory is intentionally Linux-focused. It depends on the Linux
runtime tools used by the Debian package and does not install Windows binaries
or Windows-specific dependencies.

## Platform notes

On Linux, image conversion uses ImageMagick through `convert` when available,
or `magick` as a fallback. Document conversion uses `unoconv` when available,
with LibreOffice `soffice` as a fallback.

On Windows, image conversion uses `magick` because Windows has its own
`convert.exe`. Document conversion uses LibreOffice directly:

```powershell
soffice --headless --convert-to pdf --outdir "C:\Output" "file.docx"
```

Additional Windows setup notes are in `docs/windows/`.

## Format guide

FF Multi Converter is a graphical front-end. The real conversion work is done by
FFmpeg, ImageMagick, unoconv, or LibreOffice. A format may appear in the
interface but still require support in the installed external tool.

### Audio/Video tab

Use this tab for audio files, video files, animated formats, and media
containers. The `Convert to` field chooses the output container or file
extension. `Video codec` chooses how the video stream is encoded. `Audio codec`
chooses how the audio stream is encoded.

`Default` lets FFmpeg choose a suitable codec for the selected output format.
`Disable` removes that stream: disabling video creates audio-only output, while
disabling audio creates silent video.

#### Audio/Video output formats

| Format |       What it is useful for       |                  Example use                   |
| ------ | --------------------------------- | ---------------------------------------------- |
| `3g2`  | 3GPP2 mobile video container.     | Legacy mobile phone video.                     |
| `3gp`  | 3GPP mobile video container.      | Very old mobile devices.                       |
| `aac`  | AAC audio stream file.            | Extract or create AAC audio.                   |
| `ac3`  | Dolby Digital audio stream.       | DVD/home theater audio.                        |
| `aif`  | AIFF audio.                       | Uncompressed audio for audio editors.          |
| `aiff` | AIFF audio.                       | Mac/audio production workflows.                |
| `amr`  | Adaptive Multi-Rate speech audio. | Voice recordings and old phones.               |
| `ape`  | Monkey's Audio lossless audio.    | Lossless audio archiving.                      |
| `au`   | Sun/NeXT audio.                   | Legacy Unix audio files.                       |
| `avi`  | Older video container.            | Compatibility with old players.                |
| `caf`  | Core Audio Format.                | Apple audio workflows.                         |
| `dv`   | Digital Video format.             | Old camcorder footage.                         |
| `eac3` | Enhanced AC-3 audio stream.       | Modern surround audio.                         |
| `flac` | Lossless compressed audio.        | Music archiving without quality loss.          |
| `flv`  | Flash Video container.            | Legacy web video.                              |
| `gif`  | Animated GIF output.              | Short silent clips for sharing.                |
| `h264` | Raw H.264 video stream.           | Advanced workflows that need raw streams.      |
| `h265` | Raw H.265/HEVC video stream.      | Advanced HEVC workflows.                       |
| `hevc` | Raw HEVC video stream.            | Advanced HEVC workflows.                       |
| `m2ts` | Blu-ray transport stream.         | Blu-ray style video files.                     |
| `m4a`  | MPEG-4 audio-only container.      | AAC/ALAC music files.                          |
| `m4b`  | MPEG-4 audiobook container.       | Audiobooks and long spoken audio.              |
| `m4r`  | iPhone ringtone container.        | Ringtones.                                     |
| `m4v`  | MPEG-4 video container.           | Apple-compatible video.                        |
| `mka`  | Matroska audio container.         | Audio with modern codec flexibility.           |
| `mkv`  | Matroska video container.         | High-quality video with many tracks.           |
| `mov`  | QuickTime container.              | Apple/video editing workflows.                 |
| `mp2`  | MPEG Layer II audio.              | Broadcast and legacy audio.                    |
| `mp3`  | Common compressed audio.          | Music, podcasts, general compatibility.        |
| `mp4`  | Common MPEG-4 video container.    | Phones, browsers, social platforms.            |
| `mpg`  | MPEG Program Stream.              | DVD-era video compatibility.                   |
| `mts`  | AVCHD transport stream.           | Camcorder footage.                             |
| `mxf`  | Professional media container.     | Broadcast and editing systems.                 |
| `oga`  | Ogg audio.                        | Open audio container.                          |
| `ogg`  | Ogg media container.              | Vorbis/Opus audio or Ogg video.                |
| `ogv`  | Ogg video.                        | Open video distribution.                       |
| `opus` | Opus audio stream/container.      | Speech, streaming, high-quality low bitrate.   |
| `ts`   | MPEG transport stream.            | Streaming, broadcast, recovery-friendly files. |
| `vob`  | DVD video object.                 | DVD-style video.                               |
| `wav`  | Uncompressed PCM audio container. | Audio editing and maximum compatibility.       |
| `webm` | Open web video container.         | Browser-friendly VP8/VP9/AV1 video.            |
| `wma`  | Windows Media Audio.              | Windows legacy compatibility.                  |
| `wmv`  | Windows Media Video.              | Windows legacy compatibility.                  |
| `wv`   | WavPack audio.                    | Lossless or hybrid audio archiving.            |

#### Video codecs

|    Codec     |                 What it does                 |                      Example use                        |
| ------------ | -------------------------------------------- | ------------------------------------------------------- |
| `copy`       | Copies the video stream without re-encoding. | Change container from `.mkv` to `.mp4` when compatible. |
| `ffv1`       | Lossless intra-frame codec.                  | Archival masters and preservation.                      |
| `flv`        | Flash video codec.                           | Legacy `.flv` files.                                    |
| `h263`       | Older low-bitrate video codec.               | Legacy mobile/low-resolution video.                     |
| `libaom-av1` | AV1 encoder from AOM.                        | Modern open video with high compression.                |
| `libsvtav1`  | SVT-AV1 encoder.                             | Faster AV1 encoding when FFmpeg includes it.            |
| `libtheora`  | Theora video encoder.                        | Open Ogg video.                                         |
| `libvpx`     | VP8 encoder.                                 | WebM video for older browser compatibility.             |
| `libvpx-vp9` | VP9 encoder.                                 | WebM with better compression than VP8.                  |
| `libx264`    | H.264 encoder.                               | Best general choice for `.mp4` compatibility.           |
| `libx265`    | H.265/HEVC encoder.                          | Smaller files than H.264, slower encoding.              |
| `libxvid`    | Xvid/MPEG-4 ASP encoder.                     | Older DVD player compatibility.                         |
| `mpeg2video` | MPEG-2 video encoder.                        | DVD-style video.                                        |
| `mpeg4`      | MPEG-4 Part 2 encoder.                       | Older devices and simple compatibility.                 |
| `msmpeg4`    | Microsoft MPEG-4 variant.                    | Very old Windows media workflows.                       |
| `prores`     | Apple ProRes encoder.                        | Editing-friendly intermediate files.                    |
| `vp9`        | Native VP9 encoder.                          | WebM/VP9 output when available.                         |
| `wmv2`       | Windows Media Video 8 codec.                 | Legacy Windows Media output.                            |

#### Audio codecs

|    Codec     |                        What it does                         |                 Example use                 |
| ------------ | ----------------------------------------------------------- | ------------------------------------------- |
| `aac`        | Standard AAC audio encoder.                                 | Audio in `.mp4`, `.m4a`, `.m4v`.            |
| `ac3`        | Dolby Digital encoder.                                      | Surround audio for home theater.            |
| `alac`       | Apple Lossless encoder.                                     | Lossless `.m4a` music files.                |
| `copy`       | Copies the audio stream without re-encoding.                | Keep original audio while changing video.   |
| `eac3`       | Enhanced AC-3 encoder.                                      | Modern surround audio.                      |
| `flac`       | Free lossless audio codec.                                  | Music archiving.                            |
| `libfdk_aac` | High-quality AAC encoder, not present in all FFmpeg builds. | Best AAC quality when available.            |
| `libmp3lame` | MP3 encoder.                                                | Podcasts and broad device compatibility.    |
| `libopus`    | Opus encoder.                                               | Speech, streaming, Discord/WebRTC-like use. |
| `libvorbis`  | Vorbis encoder.                                             | Open `.ogg` audio.                          |
| `mp2`        | MPEG Layer II audio encoder.                                | Broadcast and old video workflows.          |
| `opus`       | Native Opus encoder.                                        | Opus audio when `libopus` is unavailable.   |
| `pcm_s16le`  | Uncompressed 16-bit PCM.                                    | `.wav` files for editing.                   |
| `wavpack`    | WavPack encoder.                                            | Lossless audio archiving.                   |
| `wmav2`      | Windows Media Audio 2.                                      | Legacy Windows audio files.                 |

#### Audio/Video examples

|                  Goal                   |   Convert to   | Video codec  | Audio codec  |                  Useful options                  |
| --------------------------------------- | -------------- | ------------ | ------------ | ------------------------------------------------ |
| Most compatible video                   | `mp4`          | `libx264`    | `aac`        | Set audio bitrate to `128` or `192`.             |
| Smaller modern video                    | `mp4`          | `libx265`    | `aac`        | Use when playback devices support HEVC.          |
| Open web video                          | `webm`         | `libvpx-vp9` | `libopus`    | Good for browser playback.                       |
| Extract audio from video                | `mp3`          | `Disable`    | `libmp3lame` | Video stream is removed.                         |
| Keep original streams, change container | `mkv` or `mp4` | `copy`       | `copy`       | Fast, no quality loss if streams are compatible. |
| Make a silent video                     | `mp4`          | `libx264`    | `Disable`    | Audio stream is removed.                         |
| Lossless archive                        | `mkv`          | `ffv1`       | `flac`       | Large files, good for preservation.              |

### Images tab

Use this tab for still images, animated images, and image-like document formats.
ImageMagick performs the conversion. On Windows this program calls `magick`,
not `convert`, because Windows includes another unrelated `convert.exe`.

#### Image output formats

| Format  |         What it is useful for         |                         Example use                         |
| ------- | ------------------------------------- | ----------------------------------------------------------- |
| `apng`  | Animated PNG.                         | Short animations with PNG-style quality.                    |
| `avif`  | Modern high-compression image format. | Small web images with good quality.                         |
| `bmp`   | Uncompressed bitmap.                  | Simple Windows compatibility.                               |
| `cgm`   | Computer Graphics Metafile.           | Technical/vector graphics workflows.                        |
| `dds`   | DirectDraw Surface.                   | Game textures.                                              |
| `dng`   | Digital Negative raw photo format.    | Photography/raw workflows.                                  |
| `dpx`   | Digital Picture Exchange.             | Film and VFX frames.                                        |
| `emf`   | Enhanced Metafile.                    | Windows vector/metafile graphics.                           |
| `eps`   | Encapsulated PostScript.              | Print and vector workflows.                                 |
| `exr`   | OpenEXR high dynamic range image.     | VFX and HDR image pipelines.                                |
| `fpx`   | FlashPix image.                       | Legacy image archives.                                      |
| `gif`   | GIF image or animation.               | Simple animations and compatibility.                        |
| `hdr`   | Radiance HDR image.                   | High dynamic range images.                                  |
| `heic`  | HEIF image using HEVC compression.    | iPhone-style photos.                                        |
| `heif`  | High Efficiency Image File format.    | Modern photo storage.                                       |
| `ico`   | Icon file.                            | Windows icons and app icons.                                |
| `j2k`   | JPEG 2000 codestream.                 | Archival or high-quality compression.                       |
| `jbig`  | JBIG bi-level image.                  | Fax/scanned monochrome documents.                           |
| `jng`   | JPEG Network Graphics.                | Legacy web image format.                                    |
| `jp2`   | JPEG 2000 container.                  | Archival images and maps.                                   |
| `jpeg`  | JPEG image.                           | Photos and broad compatibility.                             |
| `jpg`   | JPEG image, common extension.         | Photos for web, email, and documents.                       |
| `jxl`   | JPEG XL.                              | Modern image compression and archival use.                  |
| `mrsid` | MrSID geospatial image.               | GIS and map imagery.                                        |
| `p7`    | Xv thumbnail/image format.            | Legacy image workflows.                                     |
| `pdf`   | Portable Document Format.             | Export images as PDF pages.                                 |
| `picon` | Personal icon format.                 | Legacy icon workflows.                                      |
| `png`   | Portable Network Graphics.            | Screenshots, transparency, lossless images.                 |
| `ppm`   | Portable Pixmap.                      | Simple intermediate image format.                           |
| `psd`   | Photoshop document.                   | Exchange with image editors.                                |
| `rad`   | Radiance image.                       | HDR/rendering workflows.                                    |
| `svg`   | Scalable Vector Graphics.             | Vector web graphics, when ImageMagick delegates support it. |
| `tga`   | Targa image.                          | Game/video texture workflows.                               |
| `tif`   | TIFF image.                           | Scans, print, archival images.                              |
| `tiff`  | TIFF image.                           | Same as `tif`, longer extension.                            |
| `webp`  | Modern web image format.              | Small web images with or without transparency.              |
| `xpm`   | X PixMap.                             | Unix/Linux icon resources.                                  |

#### Image options

|         Option          |                       What it does                        |                                        Example                                         |
| ----------------------- | --------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `Image Size`            | Resizes the output. Both width and height must be filled. | `800 x 600` creates an 800 by 600 image.                                               |
| `Maintain aspect ratio` | Keeps the original proportions while resizing.            | Resize a 4000x3000 photo to fit a smaller box without stretching faces.                |
| `Auto-crop`             | Adds ImageMagick trim behavior to remove uniform borders. | Remove white scanner margins around a document scan.                                   |
| `Rotate`                | Rotates clockwise by the number of degrees entered.       | `90` rotates a portrait photo into landscape.                                          |
| `Vertical flip`         | Flips top to bottom.                                      | Correct an upside-down scan.                                                           |
| `Horizontal flip`       | Flips left to right.                                      | Mirror an image.                                                                       |
| `Extra options`         | Adds raw ImageMagick options to the command.              | Use it for quality, compression, colors, background, filters, and advanced operations. |

#### Image extra options examples

Put only the options, not the input or output file names.

|                  Goal                   |                Extra options                 |
| --------------------------------------- | -------------------------------------------- |
| JPEG quality 85                         | `-quality 85`                                |
| WebP quality 80                         | `-quality 80`                                |
| Strip metadata                          | `-strip`                                     |
| Convert to grayscale                    | `-colorspace Gray`                           |
| Add white background before JPEG export | `-background white -alpha remove -alpha off` |
| Sharpen slightly                        | `-sharpen 0x1`                               |
| Blur slightly                           | `-blur 0x1`                                  |
| Limit colors                            | `-colors 256`                                |
| Make PNG compression stronger           | `-define png:compression-level=9`            |
| Resize using a high-quality filter      | `-filter Lanczos`                            |

### Documents tab

Use this tab for office documents, spreadsheets, presentations, text formats,
and document exports such as PDF or EPUB. On Linux, conversion uses `unoconv`
when available. On Windows, conversion uses LibreOffice directly through
`soffice --headless --convert-to`.

LibreOffice does not support every possible conversion direction equally. For
best results, convert between related families: Writer documents to `odt`,
`docx`, `pdf`, or `epub`; spreadsheets to `ods`, `xlsx`, or `csv`;
presentations to `odp`, `pptx`, or `pdf`.

#### Document output formats

| Format  |        What it is useful for        |                 Example use                  |
| ------- | ----------------------------------- | -------------------------------------------- |
| `bib`   | BibTeX bibliography.                | Bibliography data for LaTeX workflows.       |
| `csv`   | Comma-separated values.             | Spreadsheet data exchange.                   |
| `dif`   | Data Interchange Format.            | Legacy spreadsheet exchange.                 |
| `doc`   | Older Microsoft Word format.        | Compatibility with old Word versions.        |
| `docm`  | Macro-enabled Word document.        | Word documents that may contain macros.      |
| `docx`  | Modern Microsoft Word document.     | Common editable text documents.              |
| `dot`   | Older Word template.                | Legacy Word templates.                       |
| `dotx`  | Modern Word template.               | Word document templates.                     |
| `epub`  | E-book format.                      | Export a document as an e-book.              |
| `fodp`  | Flat XML OpenDocument presentation. | Version-control-friendly presentation files. |
| `fods`  | Flat XML OpenDocument spreadsheet.  | Version-control-friendly spreadsheet files.  |
| `fodt`  | Flat XML OpenDocument text.         | Version-control-friendly text documents.     |
| `html`  | Web page document.                  | Publish document content on the web.         |
| `ltx`   | LaTeX document.                     | Academic/typesetting workflows.              |
| `odp`   | OpenDocument presentation.          | LibreOffice Impress presentations.           |
| `ods`   | OpenDocument spreadsheet.           | LibreOffice Calc spreadsheets.               |
| `odt`   | OpenDocument text.                  | LibreOffice Writer documents.                |
| `otp`   | OpenDocument presentation template. | Impress templates.                           |
| `ots`   | OpenDocument spreadsheet template.  | Calc templates.                              |
| `ott`   | OpenDocument text template.         | Writer templates.                            |
| `pdf`   | Portable Document Format.           | Final documents for sharing or printing.     |
| `pot`   | Older PowerPoint template.          | Legacy PowerPoint templates.                 |
| `potx`  | Modern PowerPoint template.         | PowerPoint templates.                        |
| `pps`   | Older PowerPoint slideshow.         | Legacy slideshow files.                      |
| `ppsx`  | Modern PowerPoint slideshow.        | Click-to-run presentation files.             |
| `ppt`   | Older PowerPoint presentation.      | Legacy presentation compatibility.           |
| `pptx`  | Modern PowerPoint presentation.     | Common editable presentation files.          |
| `rtf`   | Rich Text Format.                   | Simple formatted text exchange.              |
| `sdc`   | Older StarOffice spreadsheet.       | Legacy StarOffice files.                     |
| `sdw`   | Older StarOffice Writer document.   | Legacy StarOffice text files.                |
| `txt`   | Plain text.                         | Extract text without formatting.             |
| `xls`   | Older Microsoft Excel spreadsheet.  | Legacy Excel compatibility.                  |
| `xlsm`  | Macro-enabled Excel spreadsheet.    | Excel spreadsheets that may contain macros.  |
| `xlsx`  | Modern Microsoft Excel spreadsheet. | Common editable spreadsheet files.           |
| `xlt`   | Older Excel template.               | Legacy spreadsheet templates.                |
| `xltx`  | Modern Excel template.              | Excel spreadsheet templates.                 |
| `xhtml` | XHTML web document.                 | Structured web export.                       |
| `xml`   | XML document/data.                  | Structured interchange when supported.       |

#### Document examples

|                          Goal                          | Convert to |
| ------------------------------------------------------ | ---------- |
| Edit a Word file in LibreOffice format                 | `odt`      |
| Share a document without letting others edit it easily | `pdf`      |
| Create an e-book from a Writer document                | `epub`     |
| Convert an Excel file to LibreOffice format            | `ods`      |
| Export spreadsheet rows for another program            | `csv`      |
| Convert a PowerPoint file to LibreOffice format        | `odp`      |
| Create a slideshow file from a presentation            | `ppsx`     |
| Extract simple text from a document                    | `txt`      |


## License

FF Multi Converter is distributed under the GNU GPL v3 or later. See `COPYING`.
