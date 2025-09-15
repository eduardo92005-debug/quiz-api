from fastapi import APIRouter

router = APIRouter(prefix="/api/quiz", tags=["Test"])

# Verbos HTTP:
# GET -> Obter informacao
# POST -> Criar nova informacao
# DELETE -> Deletar informacao
# PUT -> Atualizar informacao
# CRUD = Create, Read, Update, Delete
# Precisamos criar rotas que me permita fazer essas
# operacoes de crud
# /index -> ela eh responsavel por listar todos os itens
# registrados desse modelo
# /api/quiz/{id}/delete
# /api/quiz/{id}/update
# /api/quiz/{id} [DELETE,PUT/PATCH,POST] VERBO HTTP

# As perguntas associadas a sua conta
@router.get("/index")
def ping():
    return {"message": "meu novo teste vai"}
