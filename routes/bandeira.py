from fastapi import FastAPI, APIRouter

from models.bandeira import BandeiraDB
from schemas.bandeira import (
    BandeiraCreate,
    BandeiraRead,
    BandeiraReadList,
    BandeiraUpdate,

)

router = APIRouter(prefix="/bandeiras", tags=["BANDEIRAS"])

@router.post("/bandeira", response_model=BandeiraRead)
def criar_bandeira(nova_bandeira: BandeiraCreate):
    bandeira = BandeiraDB.create(**nova_bandeira.model_dump())
    return bandeira

@router.get("", response_model=BandeiraReadList)
def list_bandeira():
    bandeira = BandeiraDB.select()
    return {"bandeira": bandeira}

@router.get("/bandeira/{id}", response_model=BandeiraRead)
def read_bandeira(id: int):
    bandeira = BandeiraDB.get_or_none(BandeiraDB.id == bandeira_id)
    return bandeira

@router.put("/{bandeira_id}", response_model=BandeiraRead)
def atualizar_bandeira(bandeira_id: int, comodo_atualizado: BandeiraUpdate):
    bandeira = BandeiraDB.get_or_none(BandeiraDB.id == bandeira_id)
    bandeira.tarifa = comodo_atualizado.tarifa
    bandeira.nome = comodo_atualizado.nome
    bandeira.save()
    return bandeira

@router.delete("/bandeira_id", response_model=BandeiraRead)
def excluir_bandeira(bandeira_id: int):
    bandeira = BandeiraDB.get_or_none(BandeiraDB.id == bandeira_id)
    bandeira.delete_instance()
    return bandeira
