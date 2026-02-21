input_filename = "resource/students.txt"
output_filename = "resource/result.txt"

students_avg = {}

try:
    with open(input_filename, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    print(f"Файл '{input_filename}' успешно прочитан.")

    for line in lines:
        line = line.strip()
        if not line:
            continue

        parts = line.split(':', 1)

        if len(parts) != 2:
            print(f"Предупреждение: пропущена строка с некорректным форматом: {line}")
            continue

        name = parts[0].strip()
        grades_str = parts[1].strip()

        try:
            grades = [int(grade.strip()) for grade in grades_str.split(',') if grade.strip()]
        except ValueError:
            print(f"Предупреждение: у студента {name} оценки содержат нечисловые значения. Строка пропущена.")
            continue

        if not grades:
            print(f"Предупреждение: у студента {name} нет оценок. Строка пропущена.")
            continue

        average_grade = sum(grades) / len(grades)

        students_avg[name] = average_grade

    with open(output_filename, 'w', encoding='utf-8') as outfile:
        outfile.write("Студенты со средним баллом выше 4.0:\n")
        outfile.write("-" * 40 + "\n")

        for name, avg in students_avg.items():
            if avg > 4.0:
                outfile.write(f"{name}: {avg:.2f}\n")

    print(f"Результаты сохранены в файл '{output_filename}'.")
    print("-" * 40)

    if students_avg:
        best_student = max(students_avg, key=students_avg.get)
        best_avg = students_avg[best_student]

        print(f"Студент с наивысшим средним баллом:")
        print(f"   {best_student} ({best_avg:.2f})")
    else:
        print("Не удалось обработать ни одного студента из файла.")

except FileNotFoundError:
    print(f"Ошибка: Файл '{input_filename}' не найден. Убедитесь, что он находится в папке с программой.")
except Exception as e:
    print(f"Произошла непредвиденная ошибка: {e}")