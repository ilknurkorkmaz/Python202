from __future__ import annotations
import json
from pathlib import Path
from typing import List, Optional

from models import BookModel
from openlibrary import fetch_book_by_isbn, OpenLibraryError

class Library:
    def __init__(self, storage_path: str = "library.json"):
        self.storage = Path(storage_path)
        self.books: List[BookModel] = []
        self.load_books()

    # ---- Persistence ----
    def load_books(self) -> None:
        if self.storage.exists():
            try:
                data = json.loads(self.storage.read_text(encoding="utf-8"))
                self.books = [BookModel(**item) for item in data]
            except Exception:
                # bozuk dosya durumunda yumuşak başlat
                self.books = []
        else:
            self.books = []

    def save_books(self) -> None:
        data = [b.model_dump() for b in self.books]
        self.storage.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")

    # ---- Core operations ----
    def add_book(self, book: BookModel) -> None:
        if any(b.isbn == book.isbn for b in self.books):
            raise ValueError("Bu ISBN zaten mevcut.")
        self.books.append(book)
        self.save_books()

    def add_book_by_isbn(self, isbn: str) -> BookModel:
        title, author = fetch_book_by_isbn(isbn)
        book = BookModel(title=title, author=author, isbn=isbn.replace("-", "").strip())
        self.add_book(book)
        return book

    def remove_book(self, isbn: str) -> bool:
        clean = isbn.replace("-", "").strip()
        before = len(self.books)
        self.books = [b for b in self.books if b.isbn != clean]
        changed = len(self.books) != before
        if changed:
            self.save_books()
        return changed

    def list_books(self) -> List[BookModel]:
        return list(self.books)

    def find_book(self, isbn: str) -> Optional[BookModel]:
        clean = isbn.replace("-", "").strip()
        for b in self.books:
            if b.isbn == clean:
                return b
        return None