from fastapi import APIRouter, status
from fixtures import pills
from schemas import PillSchema

router = APIRouter(prefix="/pills", tags=["pills"])


@router.get("/")
async def get_pills() -> list[PillSchema]:
    return pills


@router.get("/{pill_id}", response_model=PillSchema)
async def get_pill(pill_id: int) -> dict | None:
    if 1 <= pill_id <= len(pills):
        return pills[pill_id - 1]
    return None


@router.post("/")
async def create_pill(pill: PillSchema):
    pills.append(pill)
    return status.HTTP_200_OK


@router.patch("/{pill_id}")
async def change_pill_name(pill_id: int, name: str):
    if 1 <= pill_id <= len(pills):
        pills[pill_id-1]["name"] = name
        return status.HTTP_200_OK
    return status.HTTP_304_NOT_MODIFIED


@router.delete("/{pill_id}")
async def delete_pill(pill_id: int):
    if 1 <= pill_id <= len(pills):
        del pills[pill_id - 1]
        return status.HTTP_204_NO_CONTENT
