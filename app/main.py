from fastapi import FastAPI
from app.database import engine, Base
#from app.models import user, quiz, question, answer  # importa models para criar tabelas
#from app.routes import quiz as quiz_router, user as user_router, answer as answer_router
from app.routes import test as test_routes

app = FastAPI(title="Quiz API", version="1.0.0")
Base.metadata.create_all(bind=engine)

app.include_router(test_routes.router)
#app.include_router(quiz_router.router)
#app.include_router(user_router.router)
#app.include_router(answer_router.router)