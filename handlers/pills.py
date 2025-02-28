from fastapi import APIRouter, status, Depends
from fixtures import pills
from schemas import PillSchema, PillCreateSchema
from typing import Annotated
from services import PillService
from dependencies import get_pill_service

router = APIRouter(prefix="/pills", tags=["pills"])


@router.get("/")
async def get_pills(
        pill_service: Annotated[PillService, Depends(get_pill_service)]
) -> list[PillSchema]:
    return pill_service.get_pills()


@router.get("/{pill_id}", response_model=PillSchema)
async def get_pill(pill_id: int,
                   pill_service: Annotated[PillService, Depends(get_pill_service)]
                   ) -> PillSchema | None:
    return pill_service.get_pill(pill_id=pill_id)


@router.post("/")
async def create_pill(body: PillCreateSchema,
                      pill_service: Annotated[PillService, Depends(get_pill_service)]
                      ) -> int:
    return pill_service.create_pill(body=body)


@router.delete("/{pill_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_pill(pill_id: int,
                      pill_service: Annotated[PillService, Depends(get_pill_service)]
                      ):
    pill_service.delete_pill(pill_id=pill_id)
