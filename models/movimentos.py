from pydantic import BaseModel


class Movimento(BaseModel):
    tipo: str
    valor: float
    desc: str
    caixa: str
    usr: str
