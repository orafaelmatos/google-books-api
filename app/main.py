from fastapi import FastAPI
from routers import books, favorites, history

app = FastAPI(
    title="Book Finder API",
    version="1.0.0",
    description="Search books using Google Books API"
)

app.include_router(books.router, prefix="/books", tags=["Books"])
app.include_router(favorites.router, prefix="/favorites", tags=["Favorites"])
app.include_router(history.router, prefix="/history", tags=["Search History"])

@app.get("/")
def root():
    return {"message": "Welcome to the Book Finder API 📚"}
