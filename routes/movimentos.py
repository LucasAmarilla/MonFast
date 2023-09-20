from fastapi import APIRouter

from models.movimentos import Movimento
from config.db import conn
from schemas.movimentos import movimentoEntity, movimentosEntity
from bson import ObjectId
movimento = APIRouter()


@movimento.get('/')
async def find_all_movimentos():
    return movimentosEntity(conn.scc.movimento.find())


@movimento.get('/{id}')
async def find_all_movimentos():
    return movimentoEntity(conn.scc.movimento.find_one({"_id": ObjectId(id)}))


@movimento.post('/')
async def create_movimento(movimento: Movimento):
    conn.scc.movimento.insert_one(dict(movimento))
    return movimentosEntity(conn.scc.movimento.find())


@movimento.put('/{id}')
async def create_movimento(id, movimento: Movimento):
    conn.scc.movimento.find_one_and_update(
        {"_id": ObjectId(id)}, {"$set": dict(movimento)})
    return movimentoEntity(conn.scc.movimento.find_one({"_id": ObjectId(id)}))


@movimento.delete('/{id}')
async def create_movimento(id, movimento: Movimento):
    return movimentoEntity(conn.scc.movimento.find_one_and_delete({"_id": ObjectId(id)}))
