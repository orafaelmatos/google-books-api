from fastapi import APIRouter, HTTPException, Query
from services.google_books import search_books, get_book

router = APIRouter()

@router.get("/")
async def search(
    q: str = Query(..., description="Search term"),
    author: str = None,
    publisher: str = None,
    lang: str = None,
    start_index: int = 0,
    max_results: int = 10
):
    if not q:
        raise HTTPException(status_code=400, detail="Query 'q' is required")
    return await search_books(q, author, publisher, lang, start_index, max_results)

@router.get("/{book_id}")
async def book_detail(book_id: str):
    try:
        return await get_book(book_id)
    except httpx.HTTPStatusError:
        raise HTTPException(status_code=404, detail="Book not found")
