from typing import List
from fastapi import FastAPI

from database import create_start_app_handler
from models import Book
from schemas import BookCreate, BookPublic

def get_application():

    # start the application.
    app = FastAPI()

    # Connect to database.
    app.add_event_handler("startup", create_start_app_handler(app))

    return app

app = get_application()


@app.post("/", response_model=BookPublic)
async def home(data: BookCreate):
    b = await Book.create(
        **data.dict(exclude_unset=True)
    )
    return b

@app.get("/", response_model=List[BookPublic])
async def home(data: BookCreate):
    return await Book.all()
