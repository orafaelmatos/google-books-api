import httpx

GOOGLE_BOOKS_API_URL = "https://www.googleapis.com/books/v1/volumes"

async def search_books(query: str, author: str = None, publisher: str = None, lang: str = None, start_index: int = 0, max_results: int = 10):
    params = {"q": query, "startIndex": start_index, "maxResults": max_results}
    if author:
        params["q"] += f"+inauthor:{author}"
    if publisher:
        params["q"] += f"+inpublisher:{publisher}"
    if lang:
        params["langRestrict"] = lang

    async with httpx.AsyncClient() as client:
        resp = await client.get(GOOGLE_BOOKS_API_URL, params=params)
        resp.raise_for_status()
        return resp.json()

async def get_book(book_id: str):
    async with httpx.AsyncClient() as client:
        resp = await client.get(f"{GOOGLE_BOOKS_API_URL}/{book_id}")
        resp.raise_for_status()
        return resp.json()
