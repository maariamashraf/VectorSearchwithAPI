from fastapi import APIRouter
from api_models import SearchQuery
from search_service import perform_search

router = APIRouter()

@router.get("/search/{query}")
def search_get(query: str):
    return {"results": perform_search(query)}

@router.get("/health")
def health_check():
    return {"status": "ok"}
