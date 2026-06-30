### Add LibreOffice to the environment variables (PATH) to convert files from the Windows console, e.g. odt to pdf, docx to pdf, etc. even several files (Batch)

To convert odt files to pdf from the Windows CMD or PowerShell command line with LibreOffice, we must have it installed:


[https://libreoffice.org/](https://libreoffice.org/)  

read and choose the version you want to install

The first one is a version for technology enthusiasts and could have some small bug, but if you want to use it in a company where it is unthinkable for the program to hang in the middle of work, you should install the version below:

![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgngUMOzjkXZoGcZm603_8gIU-sNWKDQWppceTlbX4odv4y2hBxivZq-oXqBUQVCvUnJocYBKvMp66z83gby5z1el8K9izlZWWcQ8urhMYyNu5mU_AiY0SqgCv4QG8MDSbkFHQilDh0JZs3bOp2yCEkIzoROeqS2ITGbHVOV9gm3glir-JPWboMubzlTtDa/s16000/Descargar%20LibreOffice.png)
After it is installed, it will be installed according to the version you installed for your computer:

**64 bit**

``` 
C:\Program Files\LibreOffice
```

**32 bit**

```
C:\Program Files (x86)\LibreOffice
```

**Note:** I have seen computers where they installed 32-bit LibreOffice on 64-bit Windows, this is **not** correct for this tutorial; the correct thing is 32-bit LibreOffice on 32-bit Windows and 64-bit LibreOffice on 64-bit Windows.  

# Add LibreOffice to the Windows PATH

To be able to convert odt documents to pdf from the terminal, I first added the path to the LibreOffice executables to the PATH, using my tutorial for adding FFmpeg to the PATH in Windows as an example:


## Add FFmpeg executables to the user variables

Now go into the folder where LibreOffice is installed and look for the "**program**" folder and enter it:

![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEirgYW_eGeX_Zj_W2FCRU3VorLfSdt2Rv658XQrLgl0ciI5k2RGZhE9H7Pase0_oujEKl8Rn-_adENrOwA7fIViJzJSsCP7Yoj9M2Nmuc_Y8bICq_QRL6018KEWuIk7mX2ubU1WOvbY6ar2qc76HSKk76ZBD9yf1EoAiDbAIMZekQVYKyemIwKaWKun7eHh/s16000/Dónde%20está%20el%20PATH%20de%20LibreOffice.png)

there copy that path by clicking the address bar like this:

![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg1vo7nRmpinzz2hfW5DPMTHDAgTKpBCQ89riKqBxrXqqS1a2X2jUIJ0p76dTblysR4KlfpOPZ3UKClgOqheEFpBQUS7fzs3k8Kx_m7yarDNsybefYyeXncw-xCHFUXEL9gvj1druu5C6FPdE8tQazfg1uZfOhhiIlJ5g13ROvBVVAKl9j4aYsAVnP7a1Ve/s16000/Copiando%20la%20ruta%20de%20LibreOffice%20program.png)
 
to avoid losing what you copied, paste it into some notepad:

```
C:\Program Files\LibreOffice\program
```

this is what we will use

### **Add LibreOffice to the PATH in Windows 10, 11**

For Windows 10 click search and type (type it by hand letter by letter because if you copy and paste it does not appear):  
  
Edit the system environment variables

![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj8ZHOIHuDsFOl4xoPKZCbrxvn6z0bRb47mjt-rG6u3CRtgXzo_qA8Ic9wyGxuepGz7mYqcQ_N2aJApXrpsmkTAUB2OR54nt1luJYZIrb_k_E_uzhUWeqdx36kAbaXtbfjueEvZh-nbLWSVh79dX-tNpeu09QPEyOA6yf0AQMunK06M2TmQtLVtrkMW34Hz/s16000/20251224-170340%20en%20Windows%2010%20escribir%20Editar%20las%20variables%20de%20entorno%20del%20sistema.png)

or you can do it like this:

1. Press **Win + R**
2. Type:

```powershell
sysdm.cpl
```

3. Press Enter

and click on:

**Environment variables**

![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEifagbiAa8J3fdh30qh-15rqZ-rkIGerKF385FBpiTVA4XyNaYyJ6rGYfIokZcdQZnb9Fg0SNkp8EYPwzcw0ON8O6cZrpWBY1DxCczXzvX_H-RX1U3EeMyb_F1IQ3XLURKyTWRKX9ijg8q0NKiVWhMOyUSSsnc_2qEfumt0WxlJR94E94v548-tcnLcmsIx/s16000/20251026-215037%20dar%20clic%20en%20Variables%20de%20entorno.png)
  
**Editing the environment variables in Windows 10**

A window appears, you have to click where it says  

**Path**  

and click on:  

**Edit**  

![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjNhhOAgYDaZ6u3o_-fNF_iXlqmuS-U_Wp1wWznSAWCxuS2UG9Rrc22a0RD6wZjU7-j4tQIYIwjXIpdPVVFrVipEpQQGyFDVCz1jNBj8-z0HpeggDVPB-vuZIZC9OWanNCRxICLQCbq9h0WN59_wT9jZtVpvCpwotHMPhxmc1l80Qa4yc0ryrgnUtuhUpae/s16000/20251026-215820%20clic%20en%20Path%20Y%20Editar.png "path in Windows 10")

and in the **"Edit environment variables"** window click **New**:   

![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgA21JpLO9ZhLU5bG4cbUEirduI7q_oiYTRQSFn95xav2J3gGTjPteqT7WnKEyi5EyBU5r7-Pt7mNrhTp0yeMtvuzFtoIFKHQdJFbz7ajn2vTZszhF-_FZ5oy7zMBIc4TE7-jz7ETxiF1YlrKcT2cvpEd-W3hvYlZei_LQNraRBoA2htHu7uOv6_bM1dhQB/s16000/Clic%20en%20Nuevo%20al%20Editar%20las%20variables%20de%20entorno.png)

there paste the path of:  

```
C:\Program Files\LibreOffice\program
```

![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi6h2LTDrEaDSPIzE0EQk0VLgBQIk0AsFFyWDQUuZ_6agarABp8JHA8W3kRjZBdxrsRa5qXS6CS-cWhFgjYyViGdy9lYQcvWYiK8LFLudjmDzHyXpZN4_dcLbL4UVIwpgzWbPQmmZ5pDDQfZIC8YFYC2sjrqp83Wph-KS07vOIR4bvtbUxXdjd1yryYtQxN/s16000/Ruta%20de%20LibreOffie%20program%20añadida%20al%20PATH.png)

close the window, close CMD or PowerShell and open one of them again and type:

```powershell
soffice --help
```

![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj0SKJ0qpQktmodcw00F7Xlh8taa8H4GNN3K3s2uSub5PMy5o1nUDn_4_d44IkSl-Xyt96-k5AKoKl49BCfPVms_1a7tl7BDO6fjLWmFqO3mAP5EKqW0DVTaetY8RTC-rK3urt2cCTur-R6Imxdv87DulQslueW6uEbnO_G_C3zEbCCWEF-T9NZXQynGRSK/s16000/LibreOffice%20en%20el%20PATH.png)
  
in Windows 10 it is not necessary to restart the computer.
  

## File conversion with LibreOffice from the terminal (Windows)

To perform conversions from the console it is recommended to use the executable:

```
soffice
```

This allows you to convert files from **Writer, Calc, Impress, Draw**, etc., without needing to open the graphical interface. 

In theory, from the terminal you can perform any conversion that LibreOffice can normally do

**File > Save As**

![](https://blogger.googleusercontent.com/img/a/AVvXsEh3tSmCh-G1pO8X_XpJNC-D1DRvof21rQPBJu_y-boHUM2vnGLxaytJjpSQvXi4nBGJ6aIX9TLxajN-JLmhDL3zdMB0ql7BDTCumZxKADOYBLWu1GuCUeYmSHjNP9DgNEfBGTiB4YqL4AWlipTSDFYIScTgOdRM-sEHURKgRRWrY4eaJxXT5E8L1hTjJMNS=s16000)
  
when saving a file as, all the formats you can use appear in the sub-option:

![](https://blogger.googleusercontent.com/img/a/AVvXsEi1vcBluFVTQRDZ1iUtg_wpLVxy737ogsjfzeimFr7wDVJWlsGjYoxvRJuGdmtntQtys0IieIPCONpe8FPhgjOdexQuSRndGxRs_AX2KbT8owVbs7MXXeT-HY6yVXWHU-TBiOKMLsm80MP7t9FhrhenjzAZFEDLpi91TYKGmN9dwc9PIYNdGmXcwq9OTqfp=s16000)

they are in Writer:   

.fodt  
.docx  
.xml  
.doc  
.rtf  
.txt

and others.  

And for LibreOffice Impress, and the others, likewise check what formats they can save

> 💡 Tip: On Windows it is even more recommended to use `soffice.com` instead of `soffice.exe`, since it is specifically designed to run in the console.

---

## 🔹 Convert an individual file

You must be located in the console (CMD or PowerShell) in the folder where the file is located.

Example, if your file is called:

```
El nombre de su archivo.odt
```

To convert it to PDF:

```powershell
soffice --headless --convert-to pdf "El nombre de su archivo.odt"
```

It will automatically generate:

```
El nombre de su archivo.pdf
```

---

## 🔹 Specify output folder

If you want to save the converted file in another folder:

```powershell
soffice --headless --convert-to pdf --outdir C:\Salida "El nombre de su archivo.odt"
```

---

## 🔹 Mass conversion (batch conversion)

You must be located in the folder where the files are.

### Convert all ODT to PDF

```powershell
for %f in (*.odt) do (soffice --headless --convert-to pdf "%f")
```

---

## 🔹 Conversion of different formats (one at a time)

Replace with the real name of your file.

### Convert ODT to DOC

```powershell
soffice --headless --convert-to doc "03-Función Hepática.odt"
```

### Convert ODT to DOCX

```powershell
soffice --headless --convert-to docx "03-Función Hepática.odt"
```

### Convert ODT to TXT

```powershell
soffice --headless --convert-to txt "03-Función Hepática.odt"
```

### Convert DOCX to ODT

```powershell
soffice --headless --convert-to odt "Archivo a convertir.docx"
```

---

## 🔹 Mass conversion of other formats

Be patient while the process is being performed.

### ODT to DOC

```powershell
for %f in (*.odt) do (soffice --headless --convert-to doc "%f")
```

### ODT to DOCX

```powershell
for %f in (*.odt) do (soffice --headless --convert-to docx "%f")
```

### ODT to TXT

```powershell
for %f in (*.odt) do (soffice --headless --convert-to txt "%f")
```

### DOC to ODT

```powershell
for %f in (*.doc) do (soffice --headless --convert-to odt "%f")
```

### DOCX to ODT

```powershell
for %f in (*.docx) do (soffice --headless --convert-to odt "%f")
```

---

## 🔹 Spreadsheet conversion (Excel / Calc)

### XLSX to PDF

```powershell
soffice --headless --convert-to pdf "archivo.xlsx"
```

### ODS to XLSX

```powershell
soffice --headless --convert-to xlsx "archivo.ods"
```

---

## 🔹 Presentation conversion (PowerPoint / Impress)

### PPTX to PDF

```powershell
soffice --headless --convert-to pdf "archivo.pptx"
```

---

## 🔹 Important note

* `--headless` prevents the graphical interface from opening.
* `soffice` works for all LibreOffice modules.
* It is recommended to use this form instead of `swriter`, `scalc`, etc., to maintain full compatibility.

## 🔹 Tip for those starting with the console (Autocomplete)

If your file has a long name, **it is not necessary to type it completely by hand**.

For example, if you have a file called:

```
mi archivo.docx
```

You can type only:

```
"mi
```

and then press the key:

```
Tab
```

The console will automatically complete the rest of the file name.

In PowerShell and CMD, when the name has spaces, the system usually completes and closes the quotation marks automatically, resulting in something like:

```
"mi archivo.docx"
```

This:

- Avoids typing errors.
- Is faster.
- Reduces problems with spaces in file names.

💡 If there are several files that begin with the same name (for example: `mi archivo.docx` and `mi resumen.docx`), you can press `Tab` several times to cycle between the available options.

This little trick will save you a lot of time when working from the terminal.


---

# 🔹 Advanced section: Force specific filters in the conversion

LibreOffice allows you to specify the **exact filter** that will be used to export the file.

This is very useful when:

- You want more control over the conversion.
- You need specific compatibility.
- The converted file does not look exactly as expected.
- You want to export with special options (for example optimized PDF).

The general syntax is:

```powershell
soffice --headless --convert-to formato:"Nombre del filtro" archivo.ext
```

---

## 🔹 Practical examples

### Export DOCX to PDF using the official Writer filter

```powershell
soffice --headless --convert-to pdf:"writer_pdf_Export" "archivo.docx"
```

This forces the Writer module to perform the export to PDF.

---

### Export XLSX to PDF using the Calc filter

```powershell
soffice --headless --convert-to pdf:"calc_pdf_Export" "archivo.xlsx"
```

---

### Export PPTX to PDF using the Impress filter

```powershell
soffice --headless --convert-to pdf:"impress_pdf_Export" "archivo.pptx"
```

---

## 🔹 Force old compatibility (old Word DOC example)

If you need to export to Word 97-2003 format:

```powershell
soffice --headless --convert-to doc:"MS Word 97" "archivo.odt"
```

---

## 🔹 When to use specific filters?

In most cases, this works perfectly:

```powershell
soffice --headless --convert-to pdf archivo.docx
```

But if:  

* The PDF comes out with errors,  
* It does not respect margins,  
* Or you need specific behavior,  

then it is recommended to force the filter.  

---

## 🔹 Technical note

Each internal format has a specific filter name.

Some common ones are:  

* writer_pdf_Export  
* calc_pdf_Export  
* impress_pdf_Export  
* MS Word 97  
* MS Excel 97  
* MS PowerPoint 97  

In normal use you do not need to know this, but for advanced automation it is very useful.

---

# Queries  

Tip: Convert Documents on the Command Line with LibreOffice  
[https://www.reddit.com/r/libreoffice/comments/10xxfqr/tip_convert_documents_on_command_line_with/](https://www.reddit.com/r/libreoffice/comments/10xxfqr/tip_convert_documents_on_command_line_with/)

File Conversion Filter Names  
[https://help.libreoffice.org/latest/en-US/text/shared/guide/convertfilters.html](https://help.libreoffice.org/latest/en-US/text/shared/guide/convertfilters.html)

