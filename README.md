# crud-project

API REST de gerenciamento de produtos com backend em FastAPI, frontend em Streamlit e banco de dados PostgreSQL, tudo orquestrado via Docker Compose.

## Tecnologias

- **Backend:** Python 3.9, FastAPI, SQLAlchemy 2.x, Pydantic 2.x
- **Frontend:** Streamlit
- **Banco de dados:** PostgreSQL
- **Infraestrutura:** Docker, Docker Compose

## Estrutura do projeto

```
crud-project/
├── backend/
│   ├── crud.py        # Operações de banco de dados
│   ├── database.py    # Configuração da conexão
│   ├── models.py      # Modelos SQLAlchemy
│   ├── router.py      # Rotas da API
│   ├── schemas.py     # Schemas Pydantic
│   └── Dockerfile
├── frontend/
│   └── Dockerfile
└── docker-compose.yml
```

## Modelo de dados

Tabela `products`:

| Campo             | Tipo     | Descrição                        |
|-------------------|----------|----------------------------------|
| id                | Integer  | Chave primária                   |
| name              | String   | Nome do produto                  |
| description       | String   | Descrição                        |
| price             | Float    | Preço (deve ser positivo)        |
| categoria         | String   | Categoria (ver lista abaixo)     |
| email_fornecedor  | String   | E-mail do fornecedor             |
| created_at        | DateTime | Data de criação (automático)     |
| updated_at        | DateTime | Data de atualização (automático) |

**Categorias válidas:** Eletrônico, Eletrodoméstico, Móveis, Roupas, Calçados

## Endpoints

| Método | Rota                    | Descrição                  |
|--------|-------------------------|----------------------------|
| POST   | `/products/`            | Cria um produto            |
| GET    | `/products/`            | Lista todos os produtos    |
| GET    | `/products/{id}`        | Busca produto por ID       |
| PUT    | `/products/{id}`        | Atualiza produto por ID    |
| DELETE | `/products/{id}`        | Remove produto por ID      |

## Como executar

**Pré-requisitos:** Docker e Docker Compose instalados.

```bash
docker-compose up --build
```

Serviços disponíveis após a inicialização:

- API: http://localhost:8000
- Documentação interativa (Swagger): http://localhost:8000/docs
- Frontend: http://localhost:8501

## Variáveis de ambiente

| Variável       | Valor padrão                                    |
|----------------|-------------------------------------------------|
| DATABASE_URL   | `postgresql://user:password@postgres/mydatabase` |
