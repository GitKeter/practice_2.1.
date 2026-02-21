import json
import os

LIBRARY_FILE = "resource/library.json"
AVAILABLE_BOOKS_FILE = "resource/available_books.txt"

INITIAL_BOOKS = [
    {
        "id": 1,
        "title": "Мастер и Маргарита",
        "author": "Булгаков",
        "year": 1967,
        "available": True
    },
    {
        "id": 2,
        "title": "Преступление и наказание",
        "author": "Достоевский",
        "year": 1866,
        "available": False
    }
]

def load_books():
    if not os.path.exists(LIBRARY_FILE):
        save_books(INITIAL_BOOKS)
        return INITIAL_BOOKS.copy()

    try:
        with open(LIBRARY_FILE, 'r', encoding='utf-8') as f:
            books = json.load(f)
        return books
    except (json.JSONDecodeError, FileNotFoundError) as e:
        print(f"Ошибка при чтении {LIBRARY_FILE}: {e}. Будет создан новый файл.")
        save_books(INITIAL_BOOKS)
        return INITIAL_BOOKS.copy()

def save_books(books):
    try:
        with open(LIBRARY_FILE, 'w', encoding='utf-8') as f:
            json.dump(books, f, ensure_ascii=False, indent=2)
    except Exception as e:
        print(f"Ошибка при сохранении в {LIBRARY_FILE}: {e}")

def get_next_id(books):
    if not books:
        return 1
    return max(book['id'] for book in books) + 1

def display_books(books):
    if not books:
        print("\n📚 Библиотека пуста.")
        return

    print("\n" + "="*100)
    print(f"{'ID':<4} {'Название':<40} {'Автор':<25} {'Год':<6} {'Статус':<12}")
    print("-"*100)
    for book in books:
        status = "Доступна" if book['available'] else "Выдана"
        title = book['title'][:38] + '..' if len(book['title']) > 38 else book['title']
        author = book['author'][:23] + '..' if len(book['author']) > 23 else book['author']
        print(f"{book['id']:<4} {title:<40} {author:<25} {book['year']:<6} {status}")
    print("="*100)

def search_books(books):
    print("\n--- Поиск книг ---")
    query = input("Введите автора или название для поиска: ").strip().lower()
    if not query:
        print("Поисковый запрос не может быть пустым.")
        return

    found_books = []
    for book in books:
        if query in book['title'].lower() or query in book['author'].lower():
            found_books.append(book)

    if found_books:
        print(f"\nНайдено книг: {len(found_books)}")
        display_books(found_books)
    else:
        print("Книги по вашему запросу не найдены.")

def add_book(books):
    print("\n--- Добавление новой книги ---")
    title = input("Введите название книги: ").strip()
    if not title:
        print("Название не может быть пустым.")
        return

    author = input("Введите автора книги: ").strip()
    if not author:
        print("Автор не может быть пустым.")
        return

    try:
        year = int(input("Введите год издания (число): ").strip())
    except ValueError:
        print("Год должен быть целым числом.")
        return

    new_book = {
        "id": get_next_id(books),
        "title": title,
        "author": author,
        "year": year,
        "available": True
    }

    books.append(new_book)
    save_books(books)
    print(f"Книга '{title}' успешно добавлена с ID {new_book['id']}.")

def change_status(books):
    print("\n--- Изменение статуса книги ---")
    try:
        book_id = int(input("Введите ID книги: ").strip())
    except ValueError:
        print("ID должен быть целым числом.")
        return

    for book in books:
        if book['id'] == book_id:
            print(f"\nНайдена книга: '{book['title']}' {book['author']}")
            current_status = "доступна" if book['available'] else "выдана"
            print(f"Текущий статус: {current_status}")

            book['available'] = not book['available']
            new_status = "доступна" if book['available'] else "выдана"
            save_books(books)
            print(f"Статус изменён на: {new_status}")
            return

    print(f"Книга с ID {book_id} не найдена.")

def delete_book(books):
    print("\n--- Удаление книги ---")
    try:
        book_id = int(input("Введите ID книги для удаления: ").strip())
    except ValueError:
        print("ID должен быть целым числом.")
        return

    for i, book in enumerate(books):
        if book['id'] == book_id:
            print(f"Найдена книга: '{book['title']}' {book['author']}")
            confirm = input("Вы уверены, что хотите её удалить? (да/нет): ").strip().lower()
            if confirm in ('да', 'yes', 'y', 'д'):
                deleted_book = books.pop(i)
                save_books(books)
                print(f"Книга '{deleted_book['title']}' удалена.")
            else:
                print("Удаление отменено.")
            return

    print(f"Книга с ID {book_id} не найдена.")

def export_available_books(books):
    print("\n--- Экспорт доступных книг ---")
    available_books = [book for book in books if book['available']]

    if not available_books:
        print("Нет доступных книг для экспорта.")
        return

    try:
        with open(AVAILABLE_BOOKS_FILE, 'w', encoding='utf-8') as f:
            f.write("СПИСОК ДОСТУПНЫХ КНИГ\n")
            f.write("="*60 + "\n")
            for book in available_books:
                f.write(f"ID: {book['id']}\n")
                f.write(f"Название: {book['title']}\n")
                f.write(f"Автор: {book['author']}\n")
                f.write(f"Год: {book['year']}\n")
                f.write("-"*30 + "\n")

        print(f"Экспорт завершён. Найдено доступных книг: {len(available_books)}")
        print(f"Результат сохранён в файл: {AVAILABLE_BOOKS_FILE}")
    except Exception as e:
        print(f"Ошибка при экспорте: {e}")

def show_menu():
    print("\n" + "="*60)
    print("            СИСТЕМА УЧЁТА КНИГ")
    print("="*60)
    print("1. Просмотр всех книг")
    print("2. Поиск по автору/названию")
    print("3. Добавление новой книги")
    print("4. Изменение статуса доступности")
    print("5. Удаление книги по ID")
    print("6. Экспорт списка доступных книг")
    print("7. Выход")
    print("-"*60)

def main():
    books = load_books()

    while True:
        show_menu()
        choice = input("Выберите действие (1-7): ").strip()

        if choice == '1':
            display_books(books)
        elif choice == '2':
            search_books(books)
        elif choice == '3':
            add_book(books)
        elif choice == '4':
            change_status(books)
        elif choice == '5':
            delete_book(books)
        elif choice == '6':
            export_available_books(books)
        elif choice == '7':
            print("Выход из программы. До свидания!")
            break
        else:
            print("Неверный выбор. Пожалуйста, выберите 1-7.")

        input("\nНажмите Enter, чтобы продолжить...")

if __name__ == "__main__":
    main()