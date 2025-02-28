from database import get_db_session
from fastapi import Depends
from sqlalchemy.orm import Session
from services import PillService
from repositories import PillRepository


def get_pill_repository(db_session: Session = Depends(get_db_session)) -> PillRepository:
    return PillRepository(db_session)


def get_pill_service(
        pill_repository: PillRepository = Depends(get_pill_repository)
) -> PillService:
    return PillService(pill_repository=pill_repository)
