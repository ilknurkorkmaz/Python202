from fastapi import FastAPI, HTTPException
from library import Library
from models import BookModel, IsbnIn
from openlibrary import OpenLibraryError

app = FastAPI(title="Library API", version="1.0.0")
lib = Library()

@app.get("/books", response_model=list[BookModel])
def get_books():
    return lib.list_books()

@app.post("/books", response_model=BookModel, status_code=201)
def add_book(isbn_in: IsbnIn):
    try:
        book = lib.add_book_by_isbn(isbn_in.isbn)
        return book
    except ValueError as e:
        raise HTTPException(status_code=409, detail=str(e))
    except OpenLibraryError as e:
        raise HTTPException(status_code=404, detail=str(e))

@app.delete("/books/{isbn}")
def delete_book(isbn: str):
    if lib.remove_book(isbn):
        return {"ok": True}
    raise HTTPException(status_code=404, detail="Kitap bulunamadı.")