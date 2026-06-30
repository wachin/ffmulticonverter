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

## Run from source

Linux:

```sh
python3 -m ffmulticonverter.ffmulticonverter
```

Windows:

```powershell
python -m pip install -r requirements.txt
python -m ffmulticonverter.ffmulticonverter
```

## Debian packaging

The `debian/` directory is intentionally Linux-focused. It depends on the Linux
runtime tools used by the Debian package and does not install Windows binaries
or Windows-specific dependencies.

## License

FF Multi Converter is distributed under the GNU GPL v3 or later. See `COPYING`.

