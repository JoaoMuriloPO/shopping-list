
# Guia de Desenvolvimento: Lista de Compras (CRUD)

Este documento vai te guiar passo a passo na criação do projeto **Lista de Compras** usando **ReactJS (Frontend)** e **Python (Backend)** com **SQLite**.

---

## 🎯 Objetivo do Projeto
Criar uma aplicação web que permita:
- Adicionar produtos a uma lista de compras.
- Editar ou remover produtos.
- Definir **quantidade** e **valor unitário** para cada item.
- Calcular automaticamente o **total da compra**.

---

## 🗂️ Estrutura de Pastas - Primeira Etapa

Dentro do seu projeto principal, crie duas pastas principais:

```
/meu-projeto/
  ├── frontend/   → aqui ficará todo o código ReactJS
  ├── backend/    → aqui ficará todo o código Python (API + banco de dados)
```

### Explicação:
- **frontend/**: tudo relacionado à interface do usuário (ReactJS).
- **backend/**: tudo relacionado à API que vai conversar com o banco de dados.

---

## 🛠️ Preparando o Backend (Python + SQLite)

### 1. Criar e ativar o ambiente virtual
No terminal, dentro da pasta `backend/`:

```bash
python -m venv venv
# Ativar no Windows:
venv\Scripts\activate
# Ativar no Linux/Mac:
source venv/bin/activate
```

### 2. Instalar bibliotecas necessárias
Ainda dentro do `backend/` com o ambiente virtual ativo:

```bash
pip install fastapi uvicorn sqlite3
```

⚠️ **Obs**: o `sqlite3` já vem instalado com o Python, mas incluí para você lembrar que o banco é esse.

### 3. Como instalar/usar o SQLite
O **SQLite** já vem embutido no Python, então não é preciso instalar nada extra.

Mas, caso queira um **visualizador gráfico** para gerenciar os dados, você pode instalar:

- [DB Browser for SQLite](https://sqlitebrowser.org/)

Com esse programa você poderá abrir o arquivo `.db` que vamos criar no backend e visualizar os produtos direto no banco.

---

## 🗂️ Estrutura de Pastas - Terceira Etapa

Depois que já tivermos criado o **backend** e o **frontend** básicos, sua pasta ficará mais ou menos assim:

```
/meu-projeto/
  ├── frontend/
  │     ├── public/
  │     ├── src/
  │     │     ├── components/   → componentes React (inputs, cards, lista)
  │     │     ├── pages/        → páginas principais
  │     │     ├── services/     → comunicação com a API (backend)
  │     │     └── App.jsx       → ponto de entrada da aplicação React
  │     └── package.json
  │
  ├── backend/
  │     ├── app/
  │     │     ├── models/       → definição das tabelas (Produto, etc)
  │     │     ├── routes/       → rotas CRUD da API
  │     │     ├── database.py   → conexão com SQLite
  │     │     └── main.py       → ponto de entrada da API
  │     └── requirements.txt    → bibliotecas usadas no backend
  │
  └── README.md
```

---

## 🚀 Conclusão
Esse é o esqueleto inicial do seu projeto.  
No **próximo passo**, você vai aprender a:
- Criar a tabela `produtos` no SQLite.
- Implementar as rotas **CRUD** no backend (FastAPI).
- Conectar o frontend ReactJS com o backend.

Assim, você terá uma aplicação de lista de compras totalmente funcional 🚀
