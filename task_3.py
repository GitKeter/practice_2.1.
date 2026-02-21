import csv
import os

FILENAME = "resource/products.csv"

INITIAL_DATA = [
    ["Название", "Цена", "Количество"],
    ["Яблоки", "100", "50"],
    ["Бананы", "80", "30"],
    ["Молоко", "120", "20"],
    ["Хлеб", "40", "100"]
]

def initialize_file():
    if not os.path.exists(FILENAME):
        with open(FILENAME, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerows(INITIAL_DATA)
        print(f"Создан новый файл '{FILENAME}' с начальными данными.")

def read_products():
    with open(FILENAME, 'r', newline='', encoding='utf-8') as f:
        reader = csv.reader(f)
        data = list(reader)
    return data

def write_products(data):
    with open(FILENAME, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerows(data)

def add_product():
    print("\n--- Добавление нового товара ---")
    name = input("Введите название товара: ").strip()
    if not name:
        print("Ошибка: Название не может быть пустым.")
        return

    try:
        price = float(input("Введите цену товара (число): ").strip())
        quantity = int(input("Введите количество товара (целое число): ").strip())
    except ValueError:
        print("Ошибка: Цена должна быть числом, а количество — целым числом.")
        return

    products = read_products()
    products.append([name, str(price), str(quantity)])
    write_products(products)
    print(f"Товар '{name}' успешно добавлен.")

def search_product():
    print("\n--- Поиск товара ---")
    query = input("Введите название товара для поиска: ").strip().lower()
    if not query:
        print("Ошибка: Введите название для поиска.")
        return

    products = read_products()
    if len(products) <= 1:
        print("В базе нет товаров для поиска.")
        return

    header = products[0]
    found = False
    for row in products[1:]:
        if len(row) >= 1 and row[0].strip().lower() == query:
            print(f"\nНайден товар:")
            print(f"  {header[0]}: {row[0]}")
            print(f"  {header[1]}: {row[1]}")
            print(f"  {header[2]}: {row[2]}")
            found = True
            break

    if not found:
        print(f"Товар с названием '{query}' не найден.")

def calculate_total_value():
    print("\n--- Расчет общей стоимости склада ---")
    products = read_products()

    if len(products) <= 1:
        print("В базе нет товаров для расчета.")
        return

    total = 0.0
    print("Участвующие в расчете товары:")
    for row in products[1:]:
        if len(row) >= 3:
            try:
                name = row[0]
                price = float(row[1])
                quantity = int(row[2])
                item_total = price * quantity
                total += item_total
                print(f"  {name}: {price} x {quantity} = {item_total:.2f}")
            except (ValueError, IndexError):
                print(f"  Пропущена некорректная строка: {row}")

    print(f"\nОбщая стоимость всех товаров на складе: {total:.2f}")

def show_menu():
    print("\n" + "="*40)
    print("      УПРАВЛЕНИЕ СКЛАДОМ (products.csv)")
    print("="*40)
    print("1. Добавить новый товар")
    print("2. Поиск товара по названию")
    print("3. Расчет общей стоимости склада")
    print("4. Выйти из программы")
    print("-"*40)
    choice = input("Выберите действие (1-4): ").strip()
    return choice

def main():
    initialize_file()

    while True:
        choice = show_menu()

        if choice == '1':
            add_product()
        elif choice == '2':
            search_product()
        elif choice == '3':
            calculate_total_value()
        elif choice == '4':
            print("Выход из программы. До свидания!")
            break
        else:
            print("Неверный ввод. Пожалуйста, выберите 1, 2, 3 или 4.")

        input("\nНажмите Enter, чтобы продолжить...")

if __name__ == "__main__":
    main()