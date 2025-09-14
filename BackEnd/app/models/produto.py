from pydantic import BaseModel

class Produto(BaseModel):
    id: int
    nome: str
    quantidade: int
    valor_unitario: float