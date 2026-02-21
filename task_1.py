filename = "resource/text.txt"

lines_to_write = [
    "Первая строка текста.",
    "Вторая строка, которая немного длиннее первой.",
    "Короткая строка",
    "А это четвертая строка, и она самая длинная в нашем примере, чтобы проверить поиск максимума.",
    "Пятая строка, финальная."
]

with open(filename, 'w', encoding='utf-8') as file:
    for line in lines_to_write:
        file.write(line + '\n')
    print(f"Файл '{filename}' успешно создан и заполнен.")

print("-" * 30)

try:
    with open(filename, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    line_count = len(lines)
    print(f"1. Количество строк в файле: {line_count}")

    word_count = 0
    for line in lines:
        words = line.strip().split()
        word_count += len(words)
    print(f"2. Количество слов в файле: {word_count}")

    longest_line = ""
    max_length = 0
    for line in lines:
        current_line = line.rstrip('\n')
        current_length = len(current_line)
        if current_length > max_length:
            max_length = current_length
            longest_line = current_line

    print(f"3. Самая длинная строка (длина {max_length} симв.):")
    print(f"   \"{longest_line}\"")

except FileNotFoundError:
    print(f"Ошибка: Файл '{filename}' не найден.")
except Exception as e:
    print(f"Произошла непредвиденная ошибка: {e}")