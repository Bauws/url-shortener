from datetime import datetime

from sqlalchemy import String, func
from sqlalchemy.orm import Mapped, mapped_column

from app.database import Base


class Link(Base):
    __tablename__ = "links"
    id: Mapped[int] = mapped_column(primary_key=True)
    short_code: Mapped[str] = mapped_column(String(7), unique=True, index=True)
    long_url: Mapped[str]
    created_at: Mapped[datetime] = mapped_column(server_default=func.now())
