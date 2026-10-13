from pathlib import Path
import shutil
import argparse
import logging

SIMULAR = False   

CATEGORIAS = {
    '.pdf': 'Documentos',
    '.docx': 'Documentos',
    '.jpg': 'Imagenes',
    '.png': 'Imagenes',
    '.jpeg': 'Imagenes',
    '.zip': 'Comprimidos',
    '.exe': 'Programas',
    '.html': 'Web',
    '.htm': 'Web',
    '.py': 'Python'
}

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s',
)
log = logging.getLogger(__name__)
filename ='organizadpr.log'


def manejar_duplicados(destino: Path) -> Path:
    if not destino.exists():
        return destino

    contador = 1
    while True:
        nueva = destino.with_name(f'{destino.stem}_{contador}{destino.suffix}')
        if not nueva.exists():
            return nueva
        contador += 1


def organizar(carpeta: Path, ejecutar: bool) -> None:
    movidos = 0
    for archivo in carpeta.iterdir():
        if not archivo.is_file():
            continue

        categoria = CATEGORIAS.get(archivo.suffix.lower(), 'Otros')
        carpeta_destino = carpeta / categoria
        destino = manejar_duplicados(carpeta_destino / archivo.name)

        log.info('%s -> %s/%s', archivo.name, categoria, destino.name)

        if ejecutar:
            try:
                carpeta_destino.mkdir(exist_ok=True)
                shutil.move(archivo, destino)
                movidos += 1
            except OSError as e:
                log.error('No se pudo mover %s: %s', archivo.name, e)


    modo = 'movidos' if ejecutar else 'Simulados (usa --ejecutar para mover)'
    log.info('%s: %d archivos', modo, movidos)

def leer_argumentos() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description='Organiza una carpeta moviendo archivos por tipo.'
    )
    parser.add_argument('carpeta', type=Path, help='Carpeta a organizar')
    parser.add_argument('--ejecutar', action='store_true',
                        help='Mueve los archivos (por defecto solo simula)')
    return parser.parse_args()

if __name__ == '__main__':
    args = leer_argumentos()
    if not args.carpeta.is_dir():
        log.error('%s no es una carpeta valida', args.carpeta)
    else:
        organizar(args.carpeta, args.ejecutar)