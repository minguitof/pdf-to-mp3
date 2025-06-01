# PDF to MP3 🔊📄 → 🎧

[![MIT License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.7%2B-blue)](https://www.python.org/)
[![Build](https://img.shields.io/badge/build-passing-brightgreen)](https://github.com/minguitof/pdf-to-mp3/actions)

Convierte cualquier archivo **PDF** en un archivo de audio **MP3** usando Python y la tecnología de **Google Text-to-Speech** (TechSpeed/gTTS).

Este proyecto hace que escuchar documentos sea tan fácil como ejecutarlo con un PDF. Ideal para estudiar, aprovechar el tiempo o facilitar el acceso a personas con dificultades visuales.

---

## 🚀 ¿Para qué sirve?

- Escuchar libros, artículos o apuntes mientras haces otras actividades.
- Mejorar la accesibilidad para personas con baja visión.
- Repasar documentos largos sin leerlos directamente.
- Transformar PDFs en audiolibros personales.

---

## 🛠️ Tecnologías utilizadas

- [Python](https://www.python.org/) 3.7+
- [gTTS (Google Text-to-Speech)](https://pypi.org/project/gTTS/)
- [PyPDF2](https://pypi.org/project/PyPDF2/)

---

## 📦 Instalación

1. Clona el repositorio:

```bash
git clone https://github.com/minguitof/pdf-to-mp3.git
cd pdf-to-mp3
```

2. Instala las dependencias:

```
pip install -r requirements.txt
```
🧪 Requiere Python 3.7 o superior.

### Uso
```
python main.py archivo.pdf
```
Esto generará archivo.mp3 en el mismo directorio.

✨ Ejemplo
Supongamos que tienes un archivo llamado documento.pdf. Solo necesitas ejecutar:

```bash
python main.py documento.pdf
```
Y automáticamente se creará documento.mp3 listo para reproducir.

⚠️ Notas
Este script extrae texto directamente del PDF. No funciona con imágenes escaneadas (usa OCR previamente en esos casos).

Convierte todo el contenido del documento. En el futuro podrías adaptar el script para seleccionar páginas específicas.

----------

#### 🧩 Posibles mejoras futuras

Selección de páginas o rangos.

Interfaz gráfica simple.

Conversión por lotes de múltiples archivos.

Soporte para diferentes idiomas y voces.

#### 📄 Licencia
Este proyecto está licenciado bajo la MIT License.
Siéntete libre de usarlo, modificarlo o mejorarlo 🙌

----------

#### 🤝 Contribuciones
¡Los PRs, ideas o sugerencias son más que bienvenidos!
Abre un issue o haz un fork para proponer mejoras.
