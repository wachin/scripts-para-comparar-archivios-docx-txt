# scripts-para-comparar-archivios-docx-txt
Estos son unos scripts para comparar archivos docx y txt

### Manual de Usuario: Comparador de Archivos de Texto y Documentos `.docx`

Este manual explica cómo usar los scripts en Python para comparar archivos `.docx` o `.txt` y extraer las diferencias entre un archivo antiguo y uno reciente. Estos scripts están diseñados para facilitar la revisión y actualización de contenido.

---

## **1. Requisitos Previos**

Antes de empezar, asegúrate de cumplir con los siguientes requisitos:

### **Hardware y Software**
- **Sistema Operativo**: Linux, Windows o macOS.
- **Python**: Versión 3.6 o superior.
- **Editor de Texto**: Nano, Vim, LibreOffice Writer o cualquier otro.
- **Terminal o Consola**: Para ejecutar comandos.
- **Ver el tutorial de cómo usar pip.**: [pip no me deja instalar paquetes de python en Debian 12 OK.md](https://github.com/wachin/Facilitar-el-Software-Libre/blob/main/Tutoriales/pip/pip%20no%20me%20deja%20instalar%20paquetes%20de%20python%20en%20Debian%2012/pip%20no%20me%20deja%20instalar%20paquetes%20de%20python%20en%20Debian%2012%20OK.md)

### **Dependencias de Python**
- Instala las librerías necesarias para los scripts, en Linux necesitarás saber usar pip y posiblemente también en MAC:
  ```bash
  pip install python-docx
  ```

---

## **2. Archivos Necesarios**

1. **Archivo Antiguo**: El documento base que deseas actualizar.
2. **Archivo Reciente**: El documento más reciente que contiene cambios o contenido nuevo.

Ambos archivos pueden estar en formato:
- `.docx` (documentos de Word).
- `.txt` (archivos de texto plano).

---

## **3. Preparación de los Archivos**

1. **Para Comparar `.docx`**:
   - Coloca ambos archivos (`archivo_antiguo.docx` y `archivo_convertido.docx`) en la misma carpeta que el script.

2. **Para Comparar `.txt`**:
   - Convierte los documentos `.docx` en archivos de texto plano:
     - Abre los archivos en LibreOffice Writer o WPS Office.
     - Guarda cada archivo como `.txt` desde el menú **Archivo > Guardar como**.
   - Nómbralos `archivo_antiguo.txt` y `archivo_convertido.txt`.

---

## **4. Uso del Script para Archivos `.docx`**

1. **Guarda el Script**:
   Copia el siguiente código en un archivo llamado `comparar_docx.py`:

   ```python
   from docx import Document

   def extraer_texto(docx_file):
       doc = Document(docx_file)
       return " ".join([p.text for p in doc.paragraphs if p.text])

   antiguo = extraer_texto("archivo_antiguo.docx")
   reciente = extraer_texto("archivo_convertido.docx")

   palabras_antiguas = set(antiguo.split())
   palabras_recientes = set(reciente.split())

   diferencias = palabras_recientes - palabras_antiguas

   with open("diferencias_docx.txt", "w") as archivo_salida:
       archivo_salida.write("\n".join(diferencias))

   print("¡Las diferencias se han guardado en 'diferencias_docx.txt'!")
   ```

2. **Ejecuta el Script**:
   - Abre una terminal en la carpeta donde guardaste el script y los archivos.
   - Ejecuta:
     ```bash
     python comparar_docx.py
     ```

3. **Resultados**:
   - Revisa el archivo `diferencias_docx.txt` para ver las palabras nuevas.

---

## **5. Uso del Script para Archivos `.txt`**

1. **Guarda el Script**:
   Copia el siguiente código en un archivo llamado `comparar_txt.py`:

   ```python
   def leer_archivo(ruta):
       with open(ruta, "r", encoding="utf-8") as archivo:
           return archivo.read()

   antiguo = leer_archivo("archivo_antiguo.txt")
   reciente = leer_archivo("archivo_convertido.txt")

   palabras_antiguas = set(antiguo.split())
   palabras_recientes = set(reciente.split())

   diferencias = palabras_recientes - palabras_antiguas

   with open("diferencias_txt.txt", "w") as archivo_salida:
       archivo_salida.write("\n".join(diferencias))

   print("¡Las diferencias se han guardado en 'diferencias_txt.txt'!")
   ```

2. **Ejecuta el Script**:
   - En la terminal, ejecuta:
     ```bash
     python comparar_txt.py
     ```

3. **Resultados**:
   - Revisa el archivo `diferencias_txt.txt` para ver las palabras nuevas.


---

## **6. Preguntas Frecuentes**

1. **¿Qué hago si hay caracteres especiales en los textos?**
   - Asegúrate de que los archivos `.txt` estén codificados en UTF-8.

2. **¿Puedo usar esto para comparar idiomas diferentes?**
   - Sí, pero los scripts solo identificarán palabras basadas en espacios.

3. **¿Cómo adapto los scripts para frases completas?**
   - Cambia `split()` por otra lógica que analice frases en lugar de palabras.

