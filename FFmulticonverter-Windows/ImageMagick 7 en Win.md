### Como instalar ImageMagick 7 en Windows y dejarlo funcionando en el PATH

ImageMagick sirve para convertir imagenes desde la linea de comandos. En FFmulticonverter para Windows es importante usar **ImageMagick 7** con el comando:

```powershell
magick
```

No conviene usar directamente:

```powershell
convert
```

porque Windows ya trae un programa llamado `convert.exe` en:

```powershell
C:\Windows\System32\convert.exe
```

Ese `convert.exe` de Windows no es ImageMagick, sino una herramienta del sistema para convertir sistemas de archivos. Por eso puede causar conflicto si un programa intenta llamar `convert` para convertir imagenes.

# Descargar ImageMagick 7

Entre en la pagina oficial:

[https://imagemagick.org/download/#gsc.tab=0](https://imagemagick.org/download/#gsc.tab=0)

![](imagenes/01-imagemagick%207-download.png)

Baje hasta la seccion:

**Version binaria de Windows**

En Windows 64 bits recomiendo descargar la version:

```text
ImageMagick-7.x.x-xx-Q16-HDRI-x64-dll.exe
```

Por ejemplo:

```text
ImageMagick-7.1.2-26-Q16-HDRI-x64-dll.exe
```

Esta es la version para Windows de 64 bits, con librerias dinamicas DLL, 16 bits por pixel y soporte HDRI.

# Opciones recomendadas en el instalador

Cuando llegue a la pantalla **Select Additional Tasks**, deje marcado:

```text
Add application directory to your system path
```

![](imagenes/02-imagemagick-7-por-defecto-en-el-path.png)
Y deje desmarcadas estas opciones:

```text
Install legacy utilities (e.g. identify)
Install development headers for C and C++
Install PerlMagick for Strawberry Perl
```

La opcion importante es **Add application directory to your system path**, porque eso permite usar `magick` desde PowerShell o CMD sin escribir la ruta completa del programa.

La opcion **Install legacy utilities** no es necesaria para FFmulticonverter. Ademas, en Windows es mejor evitar depender de comandos antiguos como `convert`, porque el nombre puede confundirse con el `convert.exe` del sistema.

# Verificar que ImageMagick funciona

Despues de terminar la instalacion, cierre todas las ventanas de PowerShell o CMD que estaban abiertas.

Esto es necesario porque las terminales que ya estaban abiertas antes de instalar ImageMagick no recargan automaticamente las variables de entorno. Aunque el instalador haya agregado ImageMagick al PATH, una PowerShell vieja puede no reconocer el comando `magick`.

Abra una PowerShell nueva y escriba:

```powershell
magick --version
```

Si todo esta bien, debe aparecer algo parecido a:

```text
Version: ImageMagick 7.1.2-26 Q16-HDRI x64
Copyright: (C) 1999 ImageMagick Studio LLC
License: https://imagemagick.org/license/
```

Con eso ImageMagick 7 ya esta instalado correctamente en el PATH.

# Prueba rapida de conversion

Para probar una conversion desde PowerShell, entre a una carpeta donde tenga una imagen PNG y ejecute:

```powershell
magick "imagen.png" "imagen.jpg"
```

Tambien puede probar con rutas completas:

```powershell
magick "C:\Users\wachi\Pictures\imagen.png" "C:\Users\wachi\Pictures\imagen.jpg"
```

Si se crea el archivo `.jpg`, ImageMagick esta funcionando correctamente.

# Nota para FFmulticonverter en Windows

Para FFmulticonverter en Windows deben funcionar estos tres comandos desde una PowerShell nueva:

```powershell
ffmpeg -version
soffice --version
magick --version
```

Si los tres responden, FFmulticonverter puede usar:

- FFmpeg para audio y video.
- LibreOffice para documentos.
- ImageMagick 7 para imagenes.

Recordatorio importante:

```text
En Windows use magick, no convert.
```
