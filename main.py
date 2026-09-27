from pathlib import Path
from datetime import datetime
import shutil


folder = Path(r"C:\Users\leman\Desktop\Automation Factory\File-organizer")


categories = {
    "Imagens": [".jpg", ".jpeg", ".png", ".gif"],
    "Documentos": [".pdf", ".doc", ".docx", ".txt"],
    "Planilhas": [".xls", ".xlsx", ".csv"],
    "Apresentacoes": [".ppt", ".pptx"],
    "Musicas": [".mp3", ".wav", ".flac"],
    "Videos": [".mp4", ".avi", ".mkv", ".mov"],
    "Compactados": [".zip", ".rar", ".7z"],
}

def write_log(folder, message):

    log_file = folder / "organizer.log"

    with open(log_file, "a", encoding="utf-8") as log:

        timestamp = datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"
        )

        log.write(f"{timestamp} | {message}\n")


def get_unique_path(destination, filename):

    target = destination / filename

    if not target.exists():
        return target

    counter = 1

    while True:

        new_name = f"{target.stem}_{counter}{target.suffix}"
        new_target = destination / new_name

        if not new_target.exists():
            return new_target

        counter += 1

def get_category(extension, categories):
    for category, extensions in categories.items():
        if extension in extensions:
            return category

    return "Outros"

def create_destination(folder, category):
    destination = folder / category
    destination.mkdir(exist_ok=True)

    return destination

def move_file(file, destination):

    try:

        target = get_unique_path(destination, file.name)

        shutil.move(file, target)

        return target

    except OSError as error:

        print(f"Erro ao mover {file.name}: {error}")

        return None

def organize_folder(folder, categories, dry_run=False):

    processed = 0
    moved = 0
    errors = 0


    for file in folder.iterdir():

        if not file.is_file():
            continue

        processed += 1

        extension = file.suffix.lower()

        category = get_category(extension, categories)

        destination = create_destination(folder, category)


        if dry_run:

            target = destination / file.name

            print(
                f"[DRY RUN] "
                f"{file.name} → {category}"
            )

            write_log(
              folder,
              f"[DRY RUN] {file.name} → {target}"
            )

        else:

            target = move_file(file, destination)

            if target:

                moved += 1

                print(
                    f"{file.name} → {category}"
                )

                write_log(
                    folder,
                    f"{file.name} → {target}"
                )

            else:

                errors += 1

                write_log(
                    folder,
                    f"ERRO ao mover: {file.name}"
                )
                



    print()
    print("=" * 40)
    print("RELATÓRIO")
    print("=" * 40)

    print(f"Arquivos encontrados: {processed}")

    if dry_run:

        print("Modo simulação: nenhum arquivo foi movido.")

    else:

        print(f"Movidos com sucesso: {moved}")
        print(f"Erros: {errors}")

    print()

    log_path = folder / "organizer.log"

    print(f"Log: {log_path.resolve()}")


if not folder.exists():

    print("A pasta não existe.")

else:

    organize_folder(folder, categories)