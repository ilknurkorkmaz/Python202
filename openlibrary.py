import httpx

OPENLIBRARY_BOOK_URL = "https://openlibrary.org/isbn/{isbn}.json"
OPENLIBRARY_AUTHOR_URL = "https://openlibrary.org{key}.json"

class OpenLibraryError(Exception):
    pass

def fetch_book_by_isbn(isbn: str) -> tuple[str, str]:
    """ISBN'den (başlık, yazarlar) döndürür. Hata durumunda OpenLibraryError atar."""
    clean_isbn = isbn.replace("-", "").strip()
    try:
        with httpx.Client(timeout=10) as client:
            r = client.get(OPENLIBRARY_BOOK_URL.format(isbn=clean_isbn))
            if r.status_code == 404:
                raise OpenLibraryError("Kitap bulunamadı.")
            r.raise_for_status()
            data = r.json()
            title = data.get("title")
            authors = data.get("authors", [])
            author_names = []
            for a in authors:
                key = a.get("key")
                if not key:
                    continue
                ar = client.get(OPENLIBRARY_AUTHOR_URL.format(key=key))
                if ar.status_code == 404:
                    continue
                ar.raise_for_status()
                author_names.append(ar.json().get("name"))
            author = ", ".join([n for n in author_names if n]) or "Bilinmiyor"
            if not title:
                raise OpenLibraryError("Başlık bilgisi alınamadı.")
            return title, author
    except httpx.RequestError as e:
        raise OpenLibraryError(f"Ağ hatası: {e}") from e
    except httpx.HTTPStatusError as e:
        raise OpenLibraryError(f"HTTP hatası: {e}") from e