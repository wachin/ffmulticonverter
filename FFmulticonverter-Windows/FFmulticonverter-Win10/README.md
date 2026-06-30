# FF Multi Converter para Windows

Esta carpeta contiene una version de **FF Multi Converter 1.8.1** adaptada para funcionar en Windows.

FF Multi Converter es una aplicacion grafica para convertir archivos de audio, video, imagenes y documentos usando herramientas externas:

- **FFmpeg** para audio y video.
- **LibreOffice** para documentos.
- **ImageMagick 7** para imagenes.

## Requisitos

Instale estos programas y asegurese de que funcionen desde una PowerShell nueva:

```powershell
ffmpeg -version
soffice --version
magick --version
```

En Windows se debe usar ImageMagick 7 con el comando `magick`. No conviene depender de `convert`, porque Windows trae su propio `convert.exe` en `C:\Windows\System32`.

## Dependencias Python

Este proyecto usa PyQt5:

```powershell
python -m pip install -r requirements.txt
```

## Ejecutar sin instalar

Desde esta carpeta:

```powershell
python -m ffmulticonverter.ffmulticonverter
```

Tambien puede usar:

```powershell
python .\bin\ffmulticonverter
```

## Documentacion de Windows

Para instrucciones mas detalladas, vea:

- [README_WINDOWS.md](README_WINDOWS.md)
- [WINDOWS_PORT_NOTES.md](WINDOWS_PORT_NOTES.md)

## Notas del proyecto original

El proyecto original fue creado para Linux y usaba:

- `ffmpeg` para archivos de audio/video.
- `unoconv` para documentos.
- ImageMagick para conversiones de imagenes.

Pagina historica del proyecto original:

[https://sites.google.com/site/ffmulticonverter/](https://sites.google.com/site/ffmulticonverter/)

## Licencia

Este proyecto conserva la licencia original GPL. Vea [COPYING](COPYING).
