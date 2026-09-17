from sqlalchemy.orm import Session
from sqlalchemy import select

from app.models import Link
from app.schemas import LinkCreate


def create_link(db: Session, link_data: LinkCreate, short_code: str) -> Link:
    link = Link(long_url=link_data.long_url, short_code=short_code)
    db.add(link)
    db.commit()
    db.refresh(link)
    return link

def get_link_by_short_code(db: Session, short_code: str) -> Link | None:
    return db.scalar(select(Link).where(Link.short_code == short_code))