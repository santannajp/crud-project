# 📦 CRUD Project — Gerenciamento de Produtos

API REST completa para gerenciamento de produtos, com **backend em FastAPI**, **frontend em Streamlit** e **banco de dados PostgreSQL**, totalmente containerizada com **Docker Compose**.

---

## 🛠️ Tecnologias Utilizadas

| Camada         | Tecnologia                                      |
|----------------|--------------------------------------------------|
| **Backend**    | Python 3.9 · FastAPI · Uvicorn · SQLAlchemy · Pydantic |
| **Frontend**   | Python 3.9 · Streamlit · Pandas · Requests       |
| **Banco de Dados** | PostgreSQL 16                                |
| **Infra**      | Docker · Docker Compose                          |

---

## 📁 Estrutura do Projeto

```
crud-project/
├── backend/
│   ├── main.py            # Entrypoint da API (cria app FastAPI e registra rotas)
│   ├── router.py          # Definição dos endpoints REST
│   ├── crud.py            # Operações de banco de dados (CRUD)
│   ├── models.py          # Modelo SQLAlchemy (tabela products)
│   ├── schemas.py         # Schemas Pydantic (validação de dados)
│   ├── database.py        # Configuração da engine e sessão do banco
│   ├── requirements.txt   # Dependências do backend
│   └── Dockerfile         # Imagem Docker do backend
│
├── frontend/
│   ├── app.py             # Aplicação Streamlit (interface do usuário)
│   ├── logo.png           # Logo exibida no frontend
│   ├── requirements.txt   # Dependências do frontend
│   ├── Dockerfile         # Imagem Docker do frontend
│   ├── .dockerignore      # Arquivos ignorados no build Docker
│   └── .streamlit/
│       └── config.toml    # Tema e configurações visuais do Streamlit
│
├── docker-compose.yml     # Orquestração dos 3 serviços
├── pyproject.toml         # Metadados do projeto (Poetry)
├── poetry.lock            # Lock de dependências
├── .gitignore
└── README.md
```

---

## 🗄️ Modelo de Dados

### Tabela `products`

| Campo              | Tipo       | Descrição                                    |
|--------------------|------------|----------------------------------------------|
| `id`               | Integer    | Chave primária (auto-incremento)             |
| `name`             | String     | Nome do produto                              |
| `description`      | String     | Descrição do produto                         |
| `price`            | Float      | Preço (deve ser positivo)                    |
| `categoria`        | String     | Categoria (validada via enum)                |
| `email_fornecedor` | String     | E-mail do fornecedor (padrão: `americans@contact.com`) |
| `created_at`       | DateTime   | Data de criação (automático — `func.now()`)  |
| `updated_at`       | DateTime   | Data de atualização (automático — `onupdate`)|

### Categorias Válidas

```
Eletrônico · Eletrodoméstico · Móveis · Roupas · Calçados
```

---

## 🔌 Endpoints da API

| Método   | Rota                     | Descrição                        | Request Body       |
|----------|--------------------------|----------------------------------|--------------------|
| `POST`   | `/products/`             | Cria um novo produto             | `ProductCreate`    |
| `GET`    | `/products/`             | Lista todos os produtos          | —                  |
| `GET`    | `/products/{product_id}` | Busca um produto pelo ID         | —                  |
| `PUT`    | `/products/{product_id}` | Atualiza um produto (parcial)    | `ProductUpdate`    |
| `DELETE` | `/products/{product_id}` | Remove um produto pelo ID        | —                  |

### Schemas

**ProductCreate** (campos obrigatórios para criação):

```json
{
  "name": "string",
  "description": "string | null",
  "price": 99.90,
  "categoria": "Eletrônico",
  "email_fornecedor": "email@exemplo.com"
}
```

**ProductUpdate** (todos os campos são opcionais):

```json
{
  "name": "string | null",
  "description": "string | null",
  "price": 99.90,
  "categoria": "Roupas",
  "email_fornecedor": "novo@email.com"
}
```

---

## 🖥️ Frontend (Streamlit)

A interface web oferece as seguintes funcionalidades via painéis expansíveis:

| Painel                            | Funcionalidade                                                 |
|-----------------------------------|----------------------------------------------------------------|
| **Adicionar um Novo Produto**     | Formulário completo com validação de categoria e e-mail        |
| **Visualizar Produtos**           | Tabela com todos os produtos cadastrados                       |
| **Obter Detalhes de um Produto**  | Busca por ID e exibe os dados em tabela                        |
| **Deletar Produto**               | Remove um produto informando o ID                              |
| **Atualizar Produto**             | Formulário de edição parcial (atualiza somente campos preenchidos) |

O tema visual é personalizado via `.streamlit/config.toml` com paleta de cores inspirada em e-commerce.

---

## 🚀 Como Executar

### Pré-requisitos

- [Docker](https://docs.docker.com/get-docker/) instalado
- [Docker Compose](https://docs.docker.com/compose/install/) instalado

### Subindo os serviços

```bash
docker-compose up --build
```

### Acessando a aplicação

| Serviço                | URL                          |
|------------------------|------------------------------|
| **API (FastAPI)**      | http://localhost:8000        |
| **Swagger UI (docs)**  | http://localhost:8000/docs   |
| **ReDoc**              | http://localhost:8000/redoc  |
| **Frontend (Streamlit)** | http://localhost:8501      |

### Parando os serviços

```bash
docker-compose down
```

Para remover também os volumes (dados do PostgreSQL):

```bash
docker-compose down -v
```

---

## ⚙️ Variáveis de Ambiente

| Variável         | Serviço   | Valor padrão                                       |
|------------------|-----------|-----------------------------------------------------|
| `DATABASE_URL`   | Backend   | `postgresql://user:password@postgres/mydatabase`    |
| `POSTGRES_DB`    | Postgres  | `mydatabase`                                        |
| `POSTGRES_USER`  | Postgres  | `user`                                              |
| `POSTGRES_PASSWORD` | Postgres | `password`                                        |

---

## 🏗️ Arquitetura

```
┌────────────────┐       HTTP        ┌────────────────┐      SQLAlchemy     ┌────────────────┐
│                │  ◄──────────────► │                │  ◄────────────────► │                │
│   Streamlit    │    porta 8501     │    FastAPI      │     porta 5432     │  PostgreSQL 16 │
│   (Frontend)   │                   │    (Backend)    │                    │   (Banco)      │
│                │                   │                │                     │                │
└────────────────┘                   └────────────────┘                     └────────────────┘
       :8501                                :8000                         volume: postgres_data
```

Os três serviços se comunicam pela rede Docker interna `mynetwork`. O frontend faz requisições HTTP para `http://backend:8000` usando o nome do serviço como hostname.

---

## 📝 Licença

Projeto de estudo — uso livre.
