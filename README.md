# Google Books API 📚

**Book Finder API** is a FastAPI project that interacts with the **Google Books API**. It allows you to search for books, add them to your favorites, and retrieve detailed information about your favorite books.

---

## Features

- Search books by keywords using Google Books API.
- Add books to a favorites list.
- Retrieve detailed information about favorite books, including:
  - Title  
  - Authors  
  - Publisher  
  - Published date
- Remove books from favorites.

---

## Project Structure
```
.
├── Dockerfile
├── requirements.txt
├── app
│ ├── main.py
│ ├── books.py
│ ├── favorites.py
│ └── history.py
└── README.md
```

---


## Installation & Running Locally

1. Clone the repository:

```bash
git clone https://github.com/orafaelmatos/google-books-api.git
cd google-books-api
```

2. Build the Docker image:

```bash
docker build -t book-finder-api .
```

3. Run the container:

```bash
docker run -p 8000:8000 book-finder-api
```

4. Access the API documentation at:
```bash
http://localhost:8000/docs

```
---
## Api Endpoints

- `GET /books` - Search books by query
- `GET /favorites` - List favorite books
- `POST /favorites/{id}` - Add a book to favorites
- `DELETE /favorites/{id}` - Remove a book from favorites


