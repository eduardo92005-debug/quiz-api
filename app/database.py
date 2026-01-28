import os, time
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker, declarative_base



DATABASE_URL = os.getenv("DATABASE_URL", "mysql+pymysql://quiz:R00t1PaS1@quiz-api-mysql:3306/quizdb")

Base = declarative_base()

engine = None
last_err = None

for i in range(30):
    try:
        tmp = create_engine(
            DATABASE_URL,
            pool_pre_ping=True,
            pool_recycle=3600,
            future=True,
        )
        with tmp.connect() as conn:
            conn.execute(text("SELECT 1"))
        engine = tmp
        print("Conectado ao MySQL.")
        break
    except Exception as e:
        last_err = e
        print(f"⏳ MySQL ainda não pronto (tentativa {i+1}/30). Erro: {e}")
        time.sleep(2)

if engine is None:
    raise RuntimeError(f"Não consegui conectar ao MySQL: {last_err}")

SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False, future=True)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


