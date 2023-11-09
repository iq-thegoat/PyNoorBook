from pydantic import BaseModel
from typing import Optional
import datetime

class Book(BaseModel):
    """
    Pydantic model for representing information about a book.
    """

    title: Optional[str] = None
    rating: Optional[int] = None
    author: Optional[str] = None
    category: Optional[str] = None
    language: Optional[str] = None
    publisher: Optional[str] = None
    ISBN: Optional[int] = None
    release_date: Optional[datetime.date] = None
    pages_count: Optional[int] = None
    raters_count: Optional[int] = None
    shortened_url: Optional[str] = None
    file_size: Optional[float] = None
    file_type: Optional[str] = None
    img_url: Optional[str] = None

class SearchResult(BaseModel):
    """
    Pydantic model for representing search results of books.
    """

    title: Optional[str] = None
    url: Optional[str] = None
