from database import get_db_session
from fastapi import Depends
from sqlalchemy.orm import Session

from repositories import PillRepository


def get_pill_repository(db_session: Session = Depends(get_db_session)) -> PillRepository:
    return PillRepository(db_session)
