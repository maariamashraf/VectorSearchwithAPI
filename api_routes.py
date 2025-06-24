from fastapi import APIRouter
from api_models import SearchQuery
from search_service import perform_search

router = APIRouter()

@router.post("/search")
def search_post(payload: SearchQuery):
    return {"results": perform_search(payload.query)}

@router.get("/health")
def health_check():
    return {"status": "ok"}
