from pydantic import BaseModel

class BandeiraCreate(BaseModel):
    nome: str
    tarifa: int

class BandeiraRead(BaseModel):
    nome: str
    tarifa: int

class BandeiraUpdate(BaseModel):
    nome: str
    tarifa: int

class BandeiraReadList(BaseModel):
    nome: str
    tarifa: int