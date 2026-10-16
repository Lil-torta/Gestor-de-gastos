<<<<<<< HEAD
# Organizador de archivos

Script hecho en python el cual tiene como objetivo analizar una carpeta y mueve cada archivo a una subcarpeta defiriendo de su extension. Por defecto **solo simula**: no mueve nada hasta que se lo pidas

## Requisitos

- Python 3.9 o superior
- Solo usa la biblioteca estandar (`pathlib`, `shutil`, `argparse`, `logging`). no hay nada que instalar

## Uso

```bash
# Simulacion (seguro no mueve nada)
python script.py <carpeta>

# Mover archivos de verdad
python script.py <carpeta> --ejecutar

# Ver ayuda
python script.py --help
```

Ejemplo en Windows:

```powershell
python script.py C:\Users\tu_usuario\Downloads --ejecutar
```
> consejo: Pruebra siempre en una carpeta segura antes de ejecutar.

## Categorias

| Carpeta | Extensiones |
|---|---|
| Documentos | .pdf, .docx |
| Imagenes | .jpg, .jpeg, .png |
| Comprimidos | .zip |
| Programas | .exe |
| Web | .html |
| Otros | todo lo demás |

Para agregar un tipo nuevo, basta con añadir una línea al diccionario `CATEGORIAS` en el script.



Readme · MD
# Organizador de archivos
 
Script en Python que revisa una carpeta (por ejemplo, Descargas) y mueve cada archivo a una subcarpeta según su extensión. Por defecto **solo simula**: no mueve nada hasta que se lo pides.
 
## Requisitos
 
- Python 3.9 o superior
- Solo usa la biblioteca estándar (`pathlib`, `shutil`, `argparse`, `logging`). No hay nada que instalar.
## Uso
 
```bash
# Simulación (seguro, no mueve nada)
python script.py <carpeta>
 
# Mover archivos de verdad
python script.py <carpeta> --ejecutar
 
# Ver ayuda
python script.py --help
```
 
Ejemplo en Windows:
 
```powershell
python script.py C:\Users\tu_usuario\Downloads --ejecutar
```
 
> 💡 Prueba siempre primero sin `--ejecutar` y, si puedes, en una carpeta de prueba.
 
## Categorías
 
| Carpeta | Extensiones |
|---|---|
| Documentos | .pdf, .docx |
| Imagenes | .jpg, .jpeg, .png |
| Comprimidos | .zip |
| Programas | .exe |
| Web | .html |
| Otros | todo lo demás |
 
Para agregar un tipo nuevo, basta con añadir una línea al diccionario `CATEGORIAS` en el script.
 
## Cómo funciona
 
- **Clasificación por extensión** con un diccionario (`.get()` con `'Otros'` como valor por defecto).
- **Extensiones en minúscula** con `.lower()`, así `FOTO.JPG` y `foto.jpg` se tratan igual.
- **Duplicados:** si ya existe un archivo con el mismo nombre en el destino, se renombra a `nombre_1.ext`, `nombre_2.ext`, etc., sin sobrescribir nada.
- **Solo archivos del primer nivel:** ignora subcarpetas, así que correrlo varias veces no reprocesa lo ya organizado (es idempotente).
- **Modo simulación por defecto**, para evitar accidentes.
- **Logging** con niveles `INFO` y `ERROR`; si un archivo no se puede mover (permisos, archivo en uso), el script lo registra y continúa con el resto.

## Estructura
 
```
Scrip-organizador-de-archivos/
├── script.py
└── README.md
```
 
## Qué aprendí
 
- Manejo de rutas con `pathlib` en lugar de strings.
- Separar datos (diccionario) de lógica (funciones).
- Crear una herramienta de terminal con `argparse`.
- Reemplazar `print` por `logging`.
- Diseñar para que lo seguro sea el comportamiento por defecto.
- Que un solo carácter (`.jpeg` vs `.jpg`) puede fallar en silencio.


## Posibles mejoras
 
- [ ] Guardar el log en un archivo (`organizador.log`) para poder deshacer movimientos.
- [ ] Detectar duplicados por contenido con `hashlib`.
- [ ] Mostrar una advertencia (`WARNING`) cuando una extensión cae en `Otros`.
- [ ] Pruebas automáticas con `pytest`.
- [ ] Cargar las categorías desde un archivo de configuración (JSON).
=======
# Gestor-de-gastos
Repositorio que trata sobre un gestor de gastos
>>>>>>> c3f3036b44d005c2f042e1ffecc7eed9605b2b07
