from app.database.models import User

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import delete, and_, select


class Database:
    ...