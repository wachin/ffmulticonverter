
# FF Multi Converter (esta versión) en Windows 10

FF Multi Converter es una aplicacion grafica para convertir archivos de audio, video, imagenes y documentos usando herramientas externas:

Este proyecto fue preparado originalmente para Linux. 

Esta carpeta contiene una version de **FF Multi Converter 1.8.1** adaptada para funcionar en Windows.

Esta variante añade compatibilidad para **Windows 10** usando:

- **FFmpeg** (audio/video)
- **LibreOffice** (documentos) vía `soffice --headless --convert-to`
- **ImageMagick 7** (imágenes) vía `magick` (IMPORTANTE en Windows)

## 1) Requisitos (ya los tienes instalados)
Verifica en PowerShell:

```powershell
ffmpeg -version
soffice --help
magick --version
```

> Nota: en Windows **NO** se debe usar `convert` directamente porque Windows trae su propio `convert.exe`.
> Por eso este proyecto usa `magick ...`.

## 2) Ejecutar directamente

Si Python ya tiene instalado PyQt5, no hace falta crear un entorno virtual.

Abra PowerShell en la carpeta del proyecto, donde esta `setup.py`, y ejecute:

```powershell
python -m ffmulticonverter.ffmulticonverter
```

Tambien puede entrar primero a la carpeta desde PowerShell:

```powershell
cd "C:\D\AI-Win\FFmul-Win\FFmulticonverter-Win10"
python -m ffmulticonverter.ffmulticonverter
```

Si aparece un error diciendo que falta `PyQt5`, instalelo en el Python que esta usando:

```powershell
python -m pip install -r requirements.txt
```

Si prefieres el script tipo Linux:

```powershell
python .\bin\ffmulticonverter
```

## 3) Opcion para desarrolladores: crear entorno virtual

Esto es opcional. Sirve si desea aislar las dependencias de este proyecto y no instalarlas en el Python principal.

En la carpeta del proyecto, cree un venv:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -U pip
python -m pip install -r requirements.txt
python -m ffmulticonverter.ffmulticonverter
```

### Problema en Windows 10 al activar el entorno virtual (.venv)

Si te ducede lo siguiente que al intentar activar el entorno virtual en PowerShell con:

```powershell
.\.venv\Scripts\Activate.ps1
```

Puede aparecer este error:

```
No se puede cargar el archivo Activate.ps1 porque la ejecución de scripts está deshabilitada en este sistema.
```

**¿Por qué ocurre esto?.-** Pasa poque Windows PowerShell tiene una política de seguridad llamada **Execution Policy** (Política de ejecución).

Por defecto, en muchos sistemas Windows, esta política está configurada como:

```
Restricted
```

Eso significa que **no se permite ejecutar ningún script `.ps1`**, ni siquiera los creados localmente por Python (como el script que activa el entorno virtual).

Esto no es un error de Python ni del programa.
Es una medida de seguridad de Windows para evitar que se ejecuten scripts maliciosos descargados de internet.

**Solución recomendada (segura para uso personal).-** Ejecutar el siguiente comando en PowerShell:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

Cuando pregunte:

```
¿Quieres cambiar la directiva de ejecución?
```

Responder:

```
S
```

---

**¿Qué hace exactamente este comando?.-** Desglose:

* `Set-ExecutionPolicy` → Cambia la política de ejecución.
* `RemoteSigned` →

  * Permite ejecutar scripts creados localmente (como los de Python).
  * Exige firma digital solo a scripts descargados de internet.
* `-Scope CurrentUser` →

  * Aplica el cambio solo a tu usuario.
  * No afecta a otros usuarios.
  * No requiere permisos de administrador.

Es una configuración **segura y recomendada** para desarrolladores.

**¿Es seguro?**

Sí.

* No desactiva la seguridad.
* No pone el sistema en modo inseguro.
* Solo permite ejecutar scripts locales sin firmar.
* Mantiene protección contra scripts descargados sin firma.

Es la configuración más común para desarrolladores en Windows.

---

**Alternativa temporal (sin cambiar configuración permanente).-** Si no deseas cambiar la política permanentemente, puedes usar:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

Esto solo afecta la sesión actual de PowerShell y se restablece al cerrarla.

**Alternativa sin usar PowerShell.-** También puedes activar el entorno virtual usando **CMD** (Símbolo del sistema):

```cmd
.venv\Scripts\activate.bat
```

CMD no tiene esta restricción.

**Recomendación final.-** Para usuarios que trabajarán con Python frecuentemente en Windows, se recomienda usar:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

porque evita este problema en futuros proyectos.

---

## 4) Si falla la conversión de documentos

Este fork usa LibreOffice con:

```powershell
soffice --headless --convert-to pdf --outdir "C:\Salida" "archivo.docx"
```

Asegúrate de poder correr ese comando manualmente.

## 5) Logs / presets

En Windows la configuración se guarda en:

```
%USERPROFILE%\.config\ffmulticonverter\
```

(igual que en Linux, pero dentro de tu carpeta de usuario).

## 6) Notas del port para Windows

Este proyecto fue escrito originalmente para Linux y esperaba herramientas como `ffmpeg`, `unoconv` e ImageMagick con el comando `convert` en un entorno tipo Unix.

Pagina historica del proyecto original:

[https://sites.google.com/site/ffmulticonverter/](https://sites.google.com/site/ffmulticonverter/)

Esta variante mantiene la estructura original de la aplicacion, pero ajusta los comandos externos para Windows.

Cambios principales:

- La conversion de audio/video usa `ffmpeg` desde el PATH de Windows.
- La conversion de documentos usa LibreOffice directamente con `soffice.com` o `soffice`.
- La conversion de imagenes usa ImageMagick 7 mediante `magick`.
- Se evita usar `convert.exe` en Windows porque es una herramienta del sistema, no ImageMagick.
- Las rutas de archivos se pasan a los procesos externos de forma mas segura para manejar espacios y tildes.
- La salida de LibreOffice se decodifica usando la codificacion local de Windows cuando hace falta, para que los nombres con tildes se vean bien en los detalles de conversion.

Para mantenimiento futuro:

- Mantener `magick` en Windows, no `convert`.
- Preferir `soffice.com` en Windows cuando este disponible, porque funciona mejor en consola.
- Probar conversiones con nombres de archivo que tengan espacios y tildes.
- Despues de cambiar codigo de comandos externos, probar al menos una imagen, un documento y un archivo de audio/video.


## Licencia

Este proyecto conserva la licencia original GPL. Vea [COPYING](COPYING).