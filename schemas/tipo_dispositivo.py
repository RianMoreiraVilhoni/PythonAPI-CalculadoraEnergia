from pydantic import BaseModel

class TipoDispositivoCreate(BaseModel):
    nombre: str

class TipoDispositivoUpdate(BaseModel):
    nombre: str

class TipoDispositivoRead(BaseModel):
    id: int
    nombre: str

class TipoDispositivoReadList(BaseModel):
    tipos_dispositivo: list[TipoDispositivoRead]