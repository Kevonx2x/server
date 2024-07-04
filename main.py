# from fastapi import FastAPI, HTTPException
# from pydantic import BaseModel
# from typing import Optional, List

# app = FastAPI()

# # Define a Book model using Pydantic
# class Book(BaseModel):
#     id: int
#     title: str
#     author: str
#     description: Optional[str] = None

# # In-memory storage for books
# books = []

# @app.post("/books/", response_model=Book)
# async def add_book(book: Book):
#     # Check if book ID already exists
#     for b in books:
#         if b.id == book.id:
#             raise HTTPException(status_code=400, detail="Book with this ID already exists")
#     books.append(book)
#     return book

# @app.get("/books/{book_id}", response_model=Book)
# async def get_book(book_id: int):
#     for book in books:
#         if book.id == book_id:
#             return book
#     raise HTTPException(status_code=404, detail="Book not found")

# @app.get("/books/", response_model=List[Book])
# async def list_books():
#     return books

# @app.delete("/books/{book_id}", response_model=Book)
# async def delete_book(book_id: int):
#     for book in books:
#         if book.id == book_id:
#             books.remove(book)
#             return book
#     raise HTTPException(status_code=404, detail="Book not found")

# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="127.0.0.1", port=8000, reload=True)
