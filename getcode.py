import os

# Папка источника (SOURCE)
SOURCE = "W:\\Study\\Code\\Python_projects\\time_tracker"

# Список исключений (например, папки и файлы, которые не нужно обрабатывать)
exclude_list = [".idea", ".gitignore", "__pycache__", "venv", ".pytest_cache", ".env"]


def extract_code_from_file(file_path):
    with open(file_path, encoding='utf-8') as file:
        return file.read()


def should_exclude(path):
    return any(exclude in path for exclude in exclude_list)


def process_directory(source_path, output_file):
    with open(output_file, 'w', encoding='utf-8') as out_file:
        for root, dirs, files in os.walk(source_path):
            print(f"Обрабатывается папка: {root}")
            dirs[:] = [d for d in dirs if not should_exclude(os.path.join(root, d))]
            for file in files:
                file_path = os.path.join(root, file)
                if should_exclude(file_path):
                    print(f"Пропущено (исключение): {file_path}")
                    continue
                try:
                    code = extract_code_from_file(file_path)
                    print(f"Чтение файла: {file_path}")
                    out_file.write(f"# ==== {file_path} ====\n")
                    out_file.write(code + "\n\n")
                except Exception as e:
                    print(f"Ошибка при чтении файла {file_path}: {e}")
                    out_file.write(f"# Ошибка при чтении файла {file_path}: {e}\n\n")


# Запуск
process_directory(SOURCE, "code.txt")
