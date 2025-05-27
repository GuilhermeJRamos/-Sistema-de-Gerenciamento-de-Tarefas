# Sistema de Gerenciamento de Tarefas

API REST para gerenciamento de tarefas com autenticação JWT, desenvolvida em FastAPI.

## Funcionalidades

- CRUD completo de tarefas
- Autenticação JWT
- Filtros por status e prioridade
- Banco de dados PostgreSQL
- Testes automatizados com Pytest
- Deploy com Docker

## Requisitos

- Python 3.11+
- Docker e Docker Compose
- PostgreSQL

## Instalação

1. Clone o repositório:
```bash
git clone <url-do-repositorio>
cd task-manager
```

2. Construa e inicie os containers:
```bash
docker-compose up --build
```

A API estará disponível em `http://localhost:8000`

## Documentação da API

A documentação interativa da API está disponível em:
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## Testes

Para executar os testes:
```bash
docker-compose exec web pytest
```

## Endpoints

### Autenticação
- POST `/api/v1/auth/register` - Registrar novo usuário
- POST `/api/v1/auth/login` - Login e obtenção do token JWT
- GET `/api/v1/auth/me` - Obter informações do usuário atual

### Tarefas
- POST `/api/v1/tasks/` - Criar nova tarefa
- GET `/api/v1/tasks/` - Listar tarefas (com filtros)
- GET `/api/v1/tasks/{task_id}` - Obter detalhes de uma tarefa
- PUT `/api/v1/tasks/{task_id}` - Atualizar tarefa
- DELETE `/api/v1/tasks/{task_id}` - Deletar tarefa

## Estrutura do Projeto

```
task-manager/
├── app/
│   ├── api/
│   │   └── v1/
│   │       ├── endpoints/
│   │       │   ├── auth.py
│   │       │   └── tasks.py
│   │       └── api.py
│   ├── core/
│   │   ├── config.py
│   │   └── security.py
│   ├── db/
│   │   ├── base_class.py
│   │   └── session.py
│   ├── models/
│   │   ├── task.py
│   │   └── user.py
│   ├── schemas/
│   │   ├── task.py
│   │   └── user.py
│   └── main.py
├── tests/
│   ├── conftest.py
│   └── test_tasks.py
├── docker-compose.yml
├── Dockerfile
├── requirements.txt
└── README.md
```
from fastapi.middleware.cors import CORSMiddleware

# ... (código existente)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # URL do frontend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)# Sistemas-Tarefas-Fullstack
# Sistemas-Tarefas-Fullstack
# Sistema-de-Tarefas-Fullstack
