# Sistema de Gerenciamento de Tarefas

Sistema completo de gerenciamento de tarefas com backend em Python (FastAPI) e frontend em Next.js.

## Estrutura do Projeto

```
├── app/                      # Backend (FastAPI)
│   ├── api/                  # Endpoints da API
│   │   └── v1/
│   │       ├── endpoints/
│   │       │   ├── auth.py
│   │       │   └── tasks.py
│   │       └── api.py
│   ├── core/                 # Configurações, segurança
│   │   ├── config.py
│   │   └── security.py
│   ├── db/                   # Banco de dados
│   │   ├── base_class.py
│   │   └── session.py
│   ├── models/               # Modelos do banco de dados
│   │   ├── task.py
│   │   └── user.py
│   ├── schemas/              # Esquemas Pydantic
│   └── main.py
├── frontend/                 # Frontend (Next.js)
│   ├── src/
│   │   ├── app/              # Páginas e layouts
│   │   ├── components/       # Componentes React
│   │   ├── lib/              # Utilitários e API
│   │   └── types/            # Tipos TypeScript
├── tests/
│   ├── conftest.py
│   └── test_tasks.py
├── docker-compose.yml
├── Dockerfile
├── requirements.txt
└── README.md
```

## Tecnologias Utilizadas

### Backend
- **Python 3.8+**
- **FastAPI**: Framework web
- **SQLAlchemy**: ORM para banco de dados
- **Pydantic**: Validação de dados
- **JWT**: Autenticação

### Frontend
- **Next.js**: Framework React
- **TypeScript**: Superset tipado de JavaScript
- **Tailwind CSS**: Framework CSS utilitário
- **shadcn/ui**: Componentes de UI reutilizáveis
- **React Hook Form**: Gerenciamento de formulários
- **Zod**: Validação de esquemas
- **Axios**: Cliente HTTP

## Como Executar

### Backend

1. Instale as dependências:
```bash
pip install -r requirements.txt
```

2. Execute o servidor:
```bash
uvicorn app.main:app --reload
```

O servidor estará disponível em: http://localhost:8000

### Frontend

1. Navegue para a pasta do frontend:
```bash
cd frontend
```

2. Instale as dependências:
```bash
npm install
```

3. Execute o servidor de desenvolvimento:
```bash
npm run dev
```

O frontend estará disponível em: http://localhost:3000

## Funcionalidades

- **Autenticação de Usuários**:
  - Registro
  - Login
  - Perfil do usuário

- **Gerenciamento de Tarefas**:
  - Criar tarefas
  - Listar tarefas
  - Atualizar tarefas
  - Excluir tarefas
  - Filtrar tarefas por status e prioridade
  - Marcar tarefas como concluídas

## API Endpoints

### Autenticação
- `POST /api/v1/auth/register`: Registrar novo usuário
- `POST /api/v1/auth/login`: Login de usuário
- `GET /api/v1/auth/me`: Obter perfil do usuário atual

### Tarefas
- `GET /api/v1/tasks`: Listar tarefas do usuário
- `POST /api/v1/tasks`: Criar nova tarefa
- `GET /api/v1/tasks/{task_id}`: Obter tarefa específica
- `PUT /api/v1/tasks/{task_id}`: Atualizar tarefa
- `DELETE /api/v1/tasks/{task_id}`: Excluir tarefa

## Documentação da API

A documentação da API está disponível em:
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## Testes

Para executar os testes:
```bash
docker-compose exec web pytest
```

## Requisitos

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