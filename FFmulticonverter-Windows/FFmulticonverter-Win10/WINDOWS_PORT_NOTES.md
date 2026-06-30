# Windows Port Notes

This folder contains a Windows-oriented port of FF Multi Converter 1.8.1.

The original project was written for Linux and expected tools such as `ffmpeg`,
`unoconv`, and ImageMagick's `convert` command to be available in a Unix-like
environment. This port keeps the original application structure but adjusts the
external command usage for Windows.

## Main Windows Changes

- Audio/video conversion uses `ffmpeg` from the Windows PATH.
- Document conversion uses LibreOffice directly with `soffice.com` or `soffice`.
- Image conversion uses ImageMagick 7 through `magick`.
- The Windows `convert.exe` command is avoided because it is a system utility,
  not ImageMagick.
- Subprocess calls use argument lists in the Windows-sensitive conversion paths
  so filenames with spaces and accents are handled more reliably.
- LibreOffice output is decoded with the local Windows encoding when needed, so
  accented filenames appear correctly in the conversion details.

## Required External Programs

Open a new PowerShell window after installing these tools and verify:

```powershell
ffmpeg -version
soffice --version
magick --version
```

If all three commands respond, the external conversion tools are available.

## Run

From this folder:

```powershell
python -m ffmulticonverter.ffmulticonverter
```

If Python reports that PyQt5 is missing:

```powershell
python -m pip install -r requirements.txt
```

## Notes for Future Maintenance

- Keep using `magick` on Windows, not `convert`.
- Prefer `soffice.com` on Windows when available because it is console-friendly.
- Test conversions with filenames that contain spaces and accents.
- Test at least one image, one document, and one audio/video file after changing
  command construction code.
