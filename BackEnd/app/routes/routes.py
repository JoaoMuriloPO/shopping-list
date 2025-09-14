from fastapi import APIRouter, HTTPException
from app.database import get_db_connection
from app.models.produto import Produto

router = APIRouter()

@router.get("/produtos/")
def read_produtos():
    conn = get_db_connection()
    produtos = conn.execute('SELECT * FROM produtos').fetchall()
    conn.close()
    return produtos

@router.post("/produtos/")
def create_produto(produto: Produto):
    conn = get_db_connection()
    conn.execute('INSERT INTO produtos (nome, quantidade, valor_unitario) VALUES (?, ?, ?)',
                 (produto.nome, produto.quantidade, produto.valor_unitario))
    conn.commit()
    conn.close()
    return produto

@router.put("/produtos/{produto_id}")
def update_produto(produto_id: int, produto: Produto):
    conn = get_db_connection()
    conn.execute('UPDATE produtos SET nome = ?, quantidade = ?, valor_unitario = ? WHERE id = ?',
                 (produto.nome, produto.quantidade, produto.valor_unitario, produto_id))
    conn.commit()
    conn.close()
    return produto

@router.delete("/produtos/{produto_id}")
def delete_produto(produto_id: int):
    conn = get_db_connection()
    conn.execute('DELETE FROM produtos WHERE id = ?', (produto_id,))
    conn.commit()
    conn.close()
    return {"message": "Produto deleted successfully"}