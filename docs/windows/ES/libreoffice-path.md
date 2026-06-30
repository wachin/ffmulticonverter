### Añadir LibreOffice a las variables de entorno (PATH) para convertir archivos desde la consola Windows, ejem odt a pdf, docx a pdf, etc incluso varios (Batch)

Para la conversion de archivos odt a pdf desde la linea de comandos CMD o PowerShell de Windows con LibreOffice lo debemos tener instalado:


[https://libreoffice.org/](https://libreoffice.org/)  

lea y elija la versión que desea instalar

La primera es una versión para entusiastas en la tecnología y podría tener algún pequeño error, pero si usted lo desea usar en una empresa donde es impensable que en medio del trabajo se cuelgue el programa debe instalar la versión de abajo:

![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgngUMOzjkXZoGcZm603_8gIU-sNWKDQWppceTlbX4odv4y2hBxivZq-oXqBUQVCvUnJocYBKvMp66z83gby5z1el8K9izlZWWcQ8urhMYyNu5mU_AiY0SqgCv4QG8MDSbkFHQilDh0JZs3bOp2yCEkIzoROeqS2ITGbHVOV9gm3glir-JPWboMubzlTtDa/s16000/Descargar%20LibreOffice.png)
Después de estar instalado, estará instalado de acuerdo a la versión que instaló para su ordenador:

**64 bit**

``` 
C:\Program Files\LibreOffice
```

**32 bit**

```
C:\Program Files (x86)\LibreOffice
```

**Nota:** He visto ordenadores donde han instalado LibreOffice de 32 bits en Windows de 64 bits, esto **no** es correcto para este tutorial, lo correcto es LibreOffice de 32 bits en Windows de 32 bits y LibreOffice de 64 bits en Windows de 64 bits.  

# Añadir LibreOffice al PATH de Windows

Para poder convertir documentos odt a pdf desde la terminal primero he añadido al PATH la ruta de los ejecutables de LibreOffice tomando como ejemplo mi tutorial para añadir al PATH a FFmpeg en Windows:


## Añadir ejecutables de FFmpeg a las variables de usuario

Ahora entre en la carpeta donde esté instalado LibreOffice y busque la carpet "**program**" y entre allí:

![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEirgYW_eGeX_Zj_W2FCRU3VorLfSdt2Rv658XQrLgl0ciI5k2RGZhE9H7Pase0_oujEKl8Rn-_adENrOwA7fIViJzJSsCP7Yoj9M2Nmuc_Y8bICq_QRL6018KEWuIk7mX2ubU1WOvbY6ar2qc76HSKk76ZBD9yf1EoAiDbAIMZekQVYKyemIwKaWKun7eHh/s16000/Dónde%20está%20el%20PATH%20de%20LibreOffice.png)

allí copie esa ruta dandole clic en la barra de direcciones así:

![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg1vo7nRmpinzz2hfW5DPMTHDAgTKpBCQ89riKqBxrXqqS1a2X2jUIJ0p76dTblysR4KlfpOPZ3UKClgOqheEFpBQUS7fzs3k8Kx_m7yarDNsybefYyeXncw-xCHFUXEL9gvj1druu5C6FPdE8tQazfg1uZfOhhiIlJ5g13ROvBVVAKl9j4aYsAVnP7a1Ve/s16000/Copiando%20la%20ruta%20de%20LibreOffice%20program.png)
 
para evitar que lo que copio se le llegue a borrar peguelo en algun bloque de notas:

```
C:\Program Files\LibreOffice\program
```

esto es lo que usaremos

### **Añadir LibreOffice al PATH en Windows 10, 11**

Para Windows 10 de clic en buscar y escriba (escriba a mano letra por letra porque si copia y pega no sale):  
  
Editar las variables de entornos del sistema

![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj8ZHOIHuDsFOl4xoPKZCbrxvn6z0bRb47mjt-rG6u3CRtgXzo_qA8Ic9wyGxuepGz7mYqcQ_N2aJApXrpsmkTAUB2OR54nt1luJYZIrb_k_E_uzhUWeqdx36kAbaXtbfjueEvZh-nbLWSVh79dX-tNpeu09QPEyOA6yf0AQMunK06M2TmQtLVtrkMW34Hz/s16000/20251224-170340%20en%20Windows%2010%20escribir%20Editar%20las%20variables%20de%20entorno%20del%20sistema.png)

o puedes poner hacer así:

1. Presiona **Win + R**
2. Escribe:

```powershell
sysdm.cpl
```

3. Presiona Enter

y de clic en:

**Variables de entorno**

![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEifagbiAa8J3fdh30qh-15rqZ-rkIGerKF385FBpiTVA4XyNaYyJ6rGYfIokZcdQZnb9Fg0SNkp8EYPwzcw0ON8O6cZrpWBY1DxCczXzvX_H-RX1U3EeMyb_F1IQ3XLURKyTWRKX9ijg8q0NKiVWhMOyUSSsnc_2qEfumt0WxlJR94E94v548-tcnLcmsIx/s16000/20251026-215037%20dar%20clic%20en%20Variables%20de%20entorno.png)
  
**Editando las variables de entorno en Windows 10**

Aparece una ventana,tiene que dar clic donde dic  

**Path**  

y clic en:  

**Editar**  

![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjNhhOAgYDaZ6u3o_-fNF_iXlqmuS-U_Wp1wWznSAWCxuS2UG9Rrc22a0RD6wZjU7-j4tQIYIwjXIpdPVVFrVipEpQQGyFDVCz1jNBj8-z0HpeggDVPB-vuZIZC9OWanNCRxICLQCbq9h0WN59_wT9jZtVpvCpwotHMPhxmc1l80Qa4yc0ryrgnUtuhUpae/s16000/20251026-215820%20clic%20en%20Path%20Y%20Editar.png "path en Windows 10")

y en la ventana **"Editar variables de entorno"** dar clic en **Nuevo**:   

![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgA21JpLO9ZhLU5bG4cbUEirduI7q_oiYTRQSFn95xav2J3gGTjPteqT7WnKEyi5EyBU5r7-Pt7mNrhTp0yeMtvuzFtoIFKHQdJFbz7ajn2vTZszhF-_FZ5oy7zMBIc4TE7-jz7ETxiF1YlrKcT2cvpEd-W3hvYlZei_LQNraRBoA2htHu7uOv6_bM1dhQB/s16000/Clic%20en%20Nuevo%20al%20Editar%20las%20variables%20de%20entorno.png)

allí pegue la ruta de :  

```
C:\Program Files\LibreOffice\program
```

![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi6h2LTDrEaDSPIzE0EQk0VLgBQIk0AsFFyWDQUuZ_6agarABp8JHA8W3kRjZBdxrsRa5qXS6CS-cWhFgjYyViGdy9lYQcvWYiK8LFLudjmDzHyXpZN4_dcLbL4UVIwpgzWbPQmmZ5pDDQfZIC8YFYC2sjrqp83Wph-KS07vOIR4bvtbUxXdjd1yryYtQxN/s16000/Ruta%20de%20LibreOffie%20program%20añadida%20al%20PATH.png)

cierre la ventana, cierre la CMD o PowerShell y vuelva a abrir uno de ellos y ponga:

```powershell
soffice --help
```

![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj0SKJ0qpQktmodcw00F7Xlh8taa8H4GNN3K3s2uSub5PMy5o1nUDn_4_d44IkSl-Xyt96-k5AKoKl49BCfPVms_1a7tl7BDO6fjLWmFqO3mAP5EKqW0DVTaetY8RTC-rK3urt2cCTur-R6Imxdv87DulQslueW6uEbnO_G_C3zEbCCWEF-T9NZXQynGRSK/s16000/LibreOffice%20en%20el%20PATH.png)
  
en Windows 10 no es necesario Reiniciar el ordenador.
  

## Conversión de archivos con LibreOffice desde la terminal (Windows)

Para realizar conversiones desde la consola es recomendable usar el ejecutable:

```
soffice
```

Este permite convertir archivos de **Writer, Calc, Impress, Draw**, etc., sin necesidad de abrir la interfaz gráfica. 

En teoria desde la terminal se puede realizar cualquier conversión que puede hacer LibreOffice normalmente

**Archivo > Guardar como**

![](https://blogger.googleusercontent.com/img/a/AVvXsEh3tSmCh-G1pO8X_XpJNC-D1DRvof21rQPBJu_y-boHUM2vnGLxaytJjpSQvXi4nBGJ6aIX9TLxajN-JLmhDL3zdMB0ql7BDTCumZxKADOYBLWu1GuCUeYmSHjNP9DgNEfBGTiB4YqL4AWlipTSDFYIScTgOdRM-sEHURKgRRWrY4eaJxXT5E8L1hTjJMNS=s16000)
  
al guardar un archivo como aparece en la sub opción todos los formatos que puede usar:

![](https://blogger.googleusercontent.com/img/a/AVvXsEi1vcBluFVTQRDZ1iUtg_wpLVxy737ogsjfzeimFr7wDVJWlsGjYoxvRJuGdmtntQtys0IieIPCONpe8FPhgjOdexQuSRndGxRs_AX2KbT8owVbs7MXXeT-HY6yVXWHU-TBiOKMLsm80MP7t9FhrhenjzAZFEDLpi91TYKGmN9dwc9PIYNdGmXcwq9OTqfp=s16000)

están en Writer:   

.fodt  
.docx  
.xml  
.doc  
.rtf  
.txt

y otros.  

Y para LibreOffice Impress, y los demás así mismo revisar que formatos pueden guardar

> 💡 Consejo: En Windows es aún más recomendable usar `soffice.com` en lugar de `soffice.exe`, ya que está diseñado específicamente para ejecutarse en consola.

---

## 🔹 Convertir un archivo individual

Debe estar ubicado en la consola (CMD o PowerShell) en la carpeta donde se encuentra el archivo.

Ejemplo, si su archivo se llama:

```
El nombre de su archivo.odt
```

Para convertirlo a PDF:

```powershell
soffice --headless --convert-to pdf "El nombre de su archivo.odt"
```

Se generará automáticamente:

```
El nombre de su archivo.pdf
```

---

## 🔹 Especificar carpeta de salida

Si desea guardar el archivo convertido en otra carpeta:

```powershell
soffice --headless --convert-to pdf --outdir C:\Salida "El nombre de su archivo.odt"
```

---

## 🔹 Conversión en masa (batch conversion)

Debe ubicarse en la carpeta donde están los archivos.

### Convertir todos los ODT a PDF

```powershell
for %f in (*.odt) do (soffice --headless --convert-to pdf "%f")
```

---

## 🔹 Conversión de distintos formatos (uno a la vez)

Reemplace con el nombre real de su archivo.

### Convertir ODT a DOC

```powershell
soffice --headless --convert-to doc "03-Función Hepática.odt"
```

### Convertir ODT a DOCX

```powershell
soffice --headless --convert-to docx "03-Función Hepática.odt"
```

### Convertir ODT a TXT

```powershell
soffice --headless --convert-to txt "03-Función Hepática.odt"
```

### Convertir DOCX a ODT

```powershell
soffice --headless --convert-to odt "Archivo a convertir.docx"
```

---

## 🔹 Conversión en masa de otros formatos

Sea paciente mientras se realiza el proceso.

### ODT a DOC

```powershell
for %f in (*.odt) do (soffice --headless --convert-to doc "%f")
```

### ODT a DOCX

```powershell
for %f in (*.odt) do (soffice --headless --convert-to docx "%f")
```

### ODT a TXT

```powershell
for %f in (*.odt) do (soffice --headless --convert-to txt "%f")
```

### DOC a ODT

```powershell
for %f in (*.doc) do (soffice --headless --convert-to odt "%f")
```

### DOCX a ODT

```powershell
for %f in (*.docx) do (soffice --headless --convert-to odt "%f")
```

---

## 🔹 Conversión de hojas de cálculo (Excel / Calc)

### XLSX a PDF

```powershell
soffice --headless --convert-to pdf "archivo.xlsx"
```

### ODS a XLSX

```powershell
soffice --headless --convert-to xlsx "archivo.ods"
```

---

## 🔹 Conversión de presentaciones (PowerPoint / Impress)

### PPTX a PDF

```powershell
soffice --headless --convert-to pdf "archivo.pptx"
```

---

## 🔹 Nota importante

* `--headless` evita que se abra la interfaz gráfica.
* `soffice` funciona para todos los módulos de LibreOffice.
* Se recomienda usar esta forma en lugar de `swriter`, `scalc`, etc., para mantener compatibilidad total.

## 🔹 Consejo para quienes están comenzando en la consola (Autocompletado)

Si su archivo tiene un nombre largo, **no es necesario escribirlo completo manualmente**.

Por ejemplo, si tiene un archivo llamado:

```
mi archivo.docx
```

Usted puede escribir solamente:

```
"mi
```

y luego presionar la tecla:

```
Tab
```

La consola automáticamente completará el resto del nombre del archivo.

En PowerShell y en CMD, cuando el nombre tiene espacios, el sistema suele completar y cerrar las comillas automáticamente, quedando algo como:

```
"mi archivo.docx"
```

Esto:

- Evita errores de escritura.
- Es más rápido.
- Reduce problemas con espacios en nombres de archivos.

💡 Si hay varios archivos que comienzan con el mismo nombre (por ejemplo: `mi archivo.docx` y `mi resumen.docx`), puede presionar `Tab` varias veces para ir cambiando entre las opciones disponibles.

Este pequeño truco le ahorrará mucho tiempo cuando trabaje desde la terminal.


---

# 🔹 Sección avanzada: Forzar filtros específicos en la conversión

LibreOffice permite especificar el **filtro exacto** que se usará para exportar el archivo.

Esto es muy útil cuando:

- Quiere mayor control sobre la conversión.
- Necesita compatibilidad específica.
- El archivo convertido no queda exactamente como esperaba.
- Quiere exportar con opciones especiales (por ejemplo PDF optimizado).

La sintaxis general es:

```powershell
soffice --headless --convert-to formato:"Nombre del filtro" archivo.ext
```

---

## 🔹 Ejemplos prácticos

### Exportar DOCX a PDF usando el filtro oficial de Writer

```powershell
soffice --headless --convert-to pdf:"writer_pdf_Export" "archivo.docx"
```

Esto fuerza a que el módulo Writer sea el que realice la exportación a PDF.

---

### Exportar XLSX a PDF usando el filtro de Calc

```powershell
soffice --headless --convert-to pdf:"calc_pdf_Export" "archivo.xlsx"
```

---

### Exportar PPTX a PDF usando el filtro de Impress

```powershell
soffice --headless --convert-to pdf:"impress_pdf_Export" "archivo.pptx"
```

---

## 🔹 Forzar compatibilidad antigua (ejemplo DOC antiguo de Word)

Si necesita exportar a formato Word 97–2003:

```powershell
soffice --headless --convert-to doc:"MS Word 97" "archivo.odt"
```

---

## 🔹 ¿Cuándo usar filtros específicos?

En la mayoría de los casos, esto funciona perfectamente:

```powershell
soffice --headless --convert-to pdf archivo.docx
```

Pero si:  

* El PDF sale con errores,  
* No respeta márgenes,  
* O necesita un comportamiento específico,  

entonces es recomendable forzar el filtro.  

---

## 🔹 Nota técnica

Cada formato interno tiene un nombre de filtro específico.

Algunos comunes son:  

* writer_pdf_Export  
* calc_pdf_Export  
* impress_pdf_Export  
* MS Word 97  
* MS Excel 97  
* MS PowerPoint 97  

En uso normal no necesita saber esto, pero para automatización avanzada es muy útil.

---

# Consultas  

Tip: Convertir Documentos en la Línea de Comandos con LibreOffice  
[https://www.reddit.com/r/libreoffice/comments/10xxfqr/tip_convert_documents_on_command_line_with/](https://www.reddit.com/r/libreoffice/comments/10xxfqr/tip_convert_documents_on_command_line_with/)

File Conversion Filter Names  
[https://help.libreoffice.org/latest/en-US/text/shared/guide/convertfilters.html](https://help.libreoffice.org/latest/en-US/text/shared/guide/convertfilters.html)

