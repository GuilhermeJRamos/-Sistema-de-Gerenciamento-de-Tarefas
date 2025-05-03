from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import settings
from app.api.v1.api import api_router
from app.db.base_class import Base
from app.db.session import engine
from app.db.init_db import init_db
from app.db.session import SessionLocal

app = FastAPI(title="Task Manager API")

# Configuração CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Criar tabelas
Base.metadata.create_all(bind=engine)

# Inicializar banco de dados
db = SessionLocal()
init_db(db)
db.close()

# Incluir rotas da API
app.include_router(api_router, prefix="/api/v1")

@app.get("/")
async def root():
    return {"message": "Bem-vindo à API de Gerenciamento de Tarefas"} 