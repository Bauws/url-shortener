from sqlalchemy.orm import Session

from app.models import Link
from app.schemas import LinkCreate


def create_link(db: Session, link_data: LinkCreate, short_code: str) -> Link:
    link = Link(long_url=link_data.long_url, short_code=short_code)
    db.add(link)
    db.commit()
    db.refresh(link)
    return link