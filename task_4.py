import os
from datetime import datetime

LOG_FILE = "resource/calculator.log"

def read_last_operations(n=5):
    if not os.path.exists(LOG_FILE):
        return []

    try:
        with open(LOG_FILE, 'r', encoding='utf-8') as f:
            lines = [line.rstrip('\n') for line in f.readlines()]

        return lines[-n:]
    except Exception as e:
        print(f"Ошибка при чтении лог-файла: {e}")
        return []

def write_to_log(entry):
    try:
        with open(LOG_FILE, 'a', encoding='utf-8') as f:
            f.write(entry + '\n')
    except Exception as e:
        print(f"Ошибка при записи в лог-файл: {e}")

def clear_log_file():
    try:
        with open(LOG_FILE, 'w', encoding='utf-8') as f:
            pass
        print(f"Лог-файл '{LOG_FILE}' успешно очищен.")
    except Exception as e:
        print(f"Ошибка при очистке лог-файла: {e}")

def get_number(prompt):
    while True:
        try:
            value = input(prompt).strip().replace(',', '.')
            return float(value)
        except ValueError:
            print("Ошибка: Пожалуйста, введите корректное число.")

def calculate():
    print("\n--- НОВОЕ ВЫЧИСЛЕНИЕ ---")
    num1 = get_number("Введите первое число: ")
    num2 = get_number("Введите второе число: ")

    operations = {'+': 'сложение', '-': 'вычитание', '*': 'умножение', '/': 'деление'}
    op = ''
    while op not in operations:
        op = input("Введите операцию (+, -, *, /): ").strip()
        if op not in operations:
            print("Ошибка: Неверная операция. Используйте +, -, *, /")

    result = None
    error_msg = None
    try:
        if op == '+':
            result = num1 + num2
        elif op == '-':
            result = num1 - num2
        elif op == '*':
            result = num1 * num2
        elif op == '/':
            if num2 == 0:
                error_msg = "Ошибка: деление на ноль!"
                result = "undefined"
            else:
                result = num1 / num2
    except Exception as e:
        error_msg = f"Неожиданная ошибка: {e}"
        result = "error"

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    if error_msg:
        log_entry = f"[{timestamp}] {num1} {op} {num2} = {result} ({error_msg})"
        print(f"\n{error_msg}")
    else:
        log_entry = f"[{timestamp}] {num1} {op} {num2} = {result}"
        print(f"\nРезультат: {num1} {op} {num2} = {result}")

    write_to_log(log_entry)
    print("Операция записана в лог.")

def main():
    while True:
        print("\n" + "="*50)
        print("         КАЛЬКУЛЯТОР С ЛОГИРОВАНИЕМ")
        print("="*50)

        print("\n--- Последние операции ---")
        last_ops = read_last_operations(5)
        if last_ops:
            for line in last_ops:
                print(line)
        else:
            print("Лог-файл пуст или ещё не создан.")
        print("-" * 50)

        print("\nВыберите действие:")
        print("1. Выполнить новое вычисление")
        print("2. Очистить лог-файл")
        print("3. Выйти")

        choice = input("Ваш выбор (1-3): ").strip()

        if choice == '1':
            calculate()
        elif choice == '2':
            confirm = input("Вы уверены, что хотите очистить лог-файл? (да/нет): ").strip().lower()
            if confirm in ('да', 'yes', 'y', 'д'):
                clear_log_file()
            else:
                print("Очистка отменена.")
        elif choice == '3':
            print("Выход из программы. До свидания!")
            break
        else:
            print("Неверный выбор. Пожалуйста, выберите 1, 2 или 3.")

        input("\nНажмите Enter, чтобы продолжить...")

if __name__ == "__main__":
    main()