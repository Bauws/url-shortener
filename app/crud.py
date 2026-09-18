from sqlalchemy.orm import Session
from sqlalchemy import select

from app.models import Link
from app.schemas import LinkCreate
from app.utils import generate_short_code


def create_link(db: Session, link_data: LinkCreate, short_code: str) -> Link:
    link = Link(long_url=link_data.long_url, short_code=short_code)
    db.add(link)
    db.commit()
    db.refresh(link)
    return link

def get_link_by_short_code(db: Session, short_code: str) -> Link | None:
    return db.scalar(select(Link).where(Link.short_code == short_code))

def generate_unique_short_code(db: Session) -> str:
    while True:
        short_code = generate_short_code(7)
        if get_link_by_short_code(db, short_code) is None:
            return short_code