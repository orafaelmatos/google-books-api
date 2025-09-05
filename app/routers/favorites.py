from fastapi import APIRouter, HTTPException
from typing import List
import httpx

router = APIRouter()
favorites: List[str] = []

GOOGLE_BOOKS_URL = "https://www.googleapis.com/books/v1/volumes/{}"

@router.get("/")
async def list_favorites():
    books = []
    async with httpx.AsyncClient() as client:
        for book_id in favorites:
            resp = await client.get(GOOGLE_BOOKS_URL.format(book_id))
            if resp.status_code == 200:
                data = resp.json()
                volume_info = data.get("volumeInfo", {})
                books.append({
                    "id": book_id,
                    "title": volume_info.get("title", "Unknown Title"),
                    "authors": volume_info.get("authors", []),
                    "publisher": volume_info.get("publisher", "Unknown Publisher"),
                    "publishedDate": volume_info.get("publishedDate", "Unknown")
                })
            else:
                books.append({"id": book_id, "title": "Failed to fetch"})
    return books

@router.post("/{book_id}")
def add_favorite(book_id: str):
    if book_id in favorites:
        raise HTTPException(status_code=400, detail="Book already in favorites")
    favorites.append(book_id)
    return {"message": "Book added to favorites"}

@router.delete("/{book_id}")
def remove_favorite(book_id: str):
    if book_id not in favorites:
        raise HTTPException(status_code=404, detail="Book not in favorites")
    favorites.remove(book_id)
    return {"message": "Book removed from favorites"}
