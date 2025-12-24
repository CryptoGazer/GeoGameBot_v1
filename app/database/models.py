from app.database.base import Base

from sqlalchemy.orm import Mapped, mapped_column, relationship, MappedColumn
from sqlalchemy import ForeignKey, BigInteger, Identity


def default_int_mapped_column() -> MappedColumn:
    return mapped_column(
        nullable=False,
        default=0
    )


class User(Base):
    __tablename__ = 'Users'

    id: Mapped[int] = mapped_column(
        BigInteger,
        primary_key=True,
        nullable=False
    )

    total_games_played: Mapped[int] = default_int_mapped_column()
    total_accuracy_scores: Mapped[int] = default_int_mapped_column()
    best_accuracy: Mapped[int] = default_int_mapped_column()
    average_accuracy: Mapped[float] = default_int_mapped_column()

