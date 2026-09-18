from fastapi import Depends, FastAPI
from app.database import get_db
from app.schemas import LinkCreate, LinkResponse
from app.crud import generate_unique_short_code, create_link
from sqlalchemy.orm import Session


app = FastAPI()

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/links", response_model=LinkResponse)
def create_short_link(link_data: LinkCreate, db: Session = Depends(get_db)):
    short_code = generate_unique_short_code(db)
    link = create_link(db, link_data, short_code)
    return link