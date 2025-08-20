from library import Library
from models import BookModel
from openlibrary import OpenLibraryError

MENU = '''
1. Kitap Ekle (ISBN ile)
2. Kitap Sil
3. Kitapları Listele
4. Kitap Ara (ISBN)
5. Çıkış
Seçiminiz: '''

def run():
    lib = Library()
    while True:
        choice = input(MENU).strip()
        if choice == "1":
            isbn = input("ISBN: ").strip()
            try:
                book = lib.add_book_by_isbn(isbn)
                print(f"Eklendi: {book.title} - {book.author} (ISBN: {book.isbn})")
            except OpenLibraryError as e:
                print(f"Hata: {e}")
            except ValueError as e:
                print(f"Hata: {e}")
        elif choice == "2":
            isbn = input("Silinecek ISBN: ").strip()
            if lib.remove_book(isbn):
                print("Silindi.")
            else:
                print("Bulunamadı.")
        elif choice == "3":
            books = lib.list_books()
            if not books:
                print("Kütüphane boş.")
            for b in books:
                print(f"- {b.title} - {b.author} (ISBN: {b.isbn})")
        elif choice == "4":
            isbn = input("Aranan ISBN: ").strip()
            b = lib.find_book(isbn)
            if b:
                print(f"Bulundu: {b.title} - {b.author} (ISBN: {b.isbn})")
            else:
                print("Bulunamadı.")
        elif choice == "5":
            print("Güle güle!")
            break
        else:
            print("Geçersiz seçim.")

if __name__ == "__main__":
    run()