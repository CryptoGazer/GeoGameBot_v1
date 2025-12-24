from app.database.base import Base

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey


class User(Base):
    ...
