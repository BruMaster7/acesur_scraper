# 🛠️ Repuestos Scraper

> Proyecto en Python para extraer datos públicos de repuestos desde el sitio `acesur.com.uy`, incluyendo productos y códigos equivalentes (equivalencias).

---

## 📝 El scraper realiza lo siguiente:

1. Inicia el cronómetro.

2. Instancia RepuestoScraper con la URL base.

3. Ejecuta scrape_all(max_pages=10):

4. Recorre páginas del sitio objetivo.

5. Extrae enlaces de productos.

6. Procesa cada producto en paralelo usando múltiples hilos.

7. Extrae información del producto y equivalencias.

8. Guarda los resultados en repuestos.json y equivalencias.json.

9. Imprime el tiempo total transcurrido.
---
## 🚀 Cómo Funciona
Este scraper está organizado como un proyecto gestionado con uv, por lo que la instalación y ejecución se realizan desde pyproject.toml usando las herramientas modernas que ofrece:

1. Inicialización del proyecto
Con el repositorio clonado, ejecutá:
```bash
uv init
```
Esto crea un entorno virtual (.venv), el archivo pyproject.toml, uv.lock, el archivo .python-version y deja listo el proyecto para ejecutarse
2. Agregar dependencias
Instalá las librerías necesarias ejecutando:
```bash
uv sync
```
3. Sincronización y lockeo
uv gestiona la resolución de todas las dependencias (directas e indirectas) y crea un archivo uv.lock que garantiza reproducibilidad.

Cada vez que ejecutás un comando (como uv run main.py), uv sincroniza el entorno con las dependencias bloqueadas, asegurando que el entorno esté siempre actualizado 
Heuristic Pedals

4. Ejecución del scraper
Para ejecutar el scraping (dentro de la carpeta src), usás:
```bash
uv run main.py
```
---

## 🧪 Ejemplo de uso y salida
```bash
📄 Scrapeando página 1...
📄 Scrapeando página 2...
...
✅ Datos guardados en 'repuestos.json'.
✅ Datos guardados en 'equivalencias.json'.
⏱️ Tiempo total de ejecución: 0:02:35
```
Los archivos JSON resultantes contendrán estructuras como:
Productos:
```json
[
  {
    "codigo": "ABC123",
    "nombre": "Repuesto X",
    "descripcion": "...",
    "marca": "...",
    "tipo": "...",
    "precio": 123.45,
    "stock": 0,
    "ubicacion": "",
    "imagen_path": "http://..."
  }
]
```

Equivalencias:
```json
[
  {
    "codigo": "ABC123",
    "equivalentes": ["DEF456", "GHI789"]
  }
]
```


## 📄 Licencia
The MIT License (MIT)
Copyright © 2025 [BruMaster7]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the “Software”), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies
of the Software, and to permit persons to whom the Software is furnished to do so,
subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED,
INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A
PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

