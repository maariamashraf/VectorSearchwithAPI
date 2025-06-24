from pydantic import BaseModel

class SearchQuery(BaseModel):
    query: str

class SearchResult(BaseModel):
    title: str
    date: str
    source: str
    summary: str