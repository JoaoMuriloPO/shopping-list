
# Guia de Desenvolvimento: Lista de Compras (CRUD)

Este documento vai te guiar passo a passo na criação do projeto **Lista de Compras** usando **ReactJS (Frontend)** e **Python (Backend)**.

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
  ├── backend/    → aqui ficará todo o código Python (API)
```

### Explicação:
- **frontend/**: tudo relacionado à interface do usuário (ReactJS).
- **backend/**: tudo relacionado à API que vai conversar com o banco de dados.

---

## 🛠️ Preparando o Backend (Python)

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


1. Inicialização do projeto React

No terminal, vá até a pasta frontend (que você já criou) e rode:
# dentro da pasta do projeto principal
cd frontend

# cria um projeto React com Vite (mais leve que CRA)
npm create vite@latest . 

# escolha as opções:
# > Project name: frontend
# > Framework: React
# > Variant: JavaScript

# instala dependências do projeto
npm install

# inicia o servidor
npm run dev


2. Organização correta das páginas

A ideia é estruturar as páginas e os componentes de forma clara, para que seu CRUD de lista de compras fique organizado.

📂 Estrutura recomendada:
frontend/
│── public/                # arquivos estáticos
│── src/
│   ├── assets/            # imagens, ícones
│   ├── components/        # componentes reutilizáveis
│   │   ├── Header.jsx     # cabeçalho
│   │   ├── ProductCard.jsx# card de produto
│   │   └── InputForm.jsx  # formulário para adicionar itens
│   ├── pages/             # páginas principais
│   │   ├── Home.jsx       # página inicial com a lista
│   │   └── About.jsx      # exemplo de outra página
│   ├── services/          # requisições para o backend (Python API)
│   │   └── api.js
│   ├── App.jsx            # componente raiz
│   ├── main.jsx           # ponto de entrada do React
│── package.json
Assim, cada parte do projeto fica separada:

components/ → peças reutilizáveis (cards, formulários, botões)

pages/ → telas principais

services/ → conexão com backend

🟦 3. Dependências que você deve baixar

Além do que o Vite já instala, precisamos de algumas libs para CRUD + navegação:
# React Router DOM → para navegação entre páginas
npm install react-router-dom

# Axios → para conectar com a API em Python (backend)
npm install axios

# PropTypes → (opcional) validação de props nos componentes
npm install prop-types

📌 Com isso você já terá:

React Router → Home, About, etc.

Axios → comunicação com backend Python.

PropTypes → segurança básica de dados nos componentes.
