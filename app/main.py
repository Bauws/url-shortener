from fastapi import Depends, FastAPI, HTTPException
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session

from app.crud import create_link, generate_unique_short_code, get_link_by_short_code
from app.database import get_db
from app.schemas import LinkCreate, LinkResponse

app = FastAPI()

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/links", response_model=LinkResponse)
def create_short_link(link_data: LinkCreate, db: Session = Depends(get_db)):
    short_code = generate_unique_short_code(db)
    link = create_link(db, link_data, short_code)
    return link

@app.get("/a/{short_code}")
def get_long_url(short_code: str, db: Session = Depends(get_db)):
    link = get_link_by_short_code(db=db, short_code=short_code)
    if link is None:
        raise HTTPException(status_code=404, detail="No target URL found")
    return RedirectResponse(link.long_url, status_code=307)
    