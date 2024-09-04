from pydantic import BaseModel, Field


class ResidenciaCreate(BaseModel):
    proprietario: str


class ResidenciaRead(BaseModel):
    id: int
    proprietario: str

class ResidenciaUpdate(BaseModel):
    id: int
    proprietario: str