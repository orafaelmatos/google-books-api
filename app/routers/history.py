from fastapi import APIRouter
from typing import List

router = APIRouter()
search_history: List[str] = []

@router.post("/")
def add_query(q: str):
    search_history.append(q)
    return {"message": "Query added to history"}

@router.get("/")
def get_history():
    return search_history
