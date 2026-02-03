from fastapi import APIRouter

router = APIRouter(prefix="/api/test", tags=["Test"])
dsadsadsadsad
@router.get("/ping")
def ping():
    return {"message": "meu novo teste vai"}

