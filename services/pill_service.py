from dataclasses import dataclass
from repositories import PillRepository
from schemas import PillSchema, PillCreateSchema
from exceptions import PillNotFoundException, PillNotCreated


@dataclass
class PillService:
    pill_repository: PillRepository

    def ping_db(self) -> dict:
        return self.pill_repository.ping_db()

    def get_pills(self) -> list[PillSchema]:
        pills = [PillSchema.model_validate(pill) for pill in self.pill_repository.get_pills()]
        return pills

    def get_pill(self, pill_id: int) -> PillSchema | None:
        pill = self.pill_repository.get_pill(pill_id=pill_id)
        if pill:
            return PillSchema.model_validate(pill)
        raise PillNotFoundException

    def create_pill(self, body: PillCreateSchema) -> int:
        pill_id = self.pill_repository.create_pill(pill=body)
        if pill_id:
            return pill_id
        raise PillNotCreated

    def delete_pill(self, pill_id: int):
        self.pill_repository.delete_pill(pill_id=pill_id)
