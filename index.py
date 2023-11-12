from gtts import gTTS
import PyPDF2


# Ruta del archivo PDF que deseas convertir a texto
pdf_file_path = r'D:\Users\Mario\Downloads\Proyectos\PYTHON\pdf_to_mp3\documents\estimados_amigos.pdf'

# Abre el archivo PDF en modo lectura binaria

try:
    pdf_file = open(pdf_file_path, 'rb')
except FileNotFoundError:
    print("El archivo no se encuentra en la ubicación especificada.")
except Exception as e:
    print("Ocurrió un error inesperado:", e)

# Crea un objeto PDFReader
pdf_reader = PyPDF2.PdfReader(pdf_file)

# Inicializa una cadena vacía para almacenar el texto extraído
text = ''

# Itera a través de cada página del PDF y extrae el texto
for page_num in range(len(pdf_reader.pages)):
    page = pdf_reader.pages[page_num]  # Utiliza pdf_reader.pages en lugar de pdf_reader.getPage()
    text += page.extract_text()

# Cierra el archivo PDF
pdf_file.close()

# Imprime o almacena el texto extraído
print(text)

#Velocidad de audio
velocidad= 1.5

# Generar un audio de la frase "Hola, mundo"
tts = gTTS(text, lang="es")
  
ruta_guardado = "D:/Users/Mario/Downloads/Proyectos/PYTHON/pdf_to_mp3/audios/estimados_amigos.mp3"

# # Guardar el audio en un archivo
tts.save(ruta_guardado)


















