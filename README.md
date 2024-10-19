# Projeto de Gerenciamento de Tarefas e Registro de Tempo

Este projeto é uma aplicação web para gerenciamento de tarefas e registros de tempo, construída com duas partes principais:

- **Backend**: Utiliza Django e Django Rest Framework para criar uma API que gerencia as operações de tarefas e registros de tempo.
- **Frontend**: Utiliza React para fornecer uma interface interativa onde os usuários podem visualizar e interagir com suas tarefas e registros.

## Pré-requisitos

- Python 3.8 ou superior
- Node.js 14 ou superior
- npm (Node Package Manager)

## Configuração do Backend (Django)

### 1. Clonar o Repositório

```bash
git clone https://github.com/RhuanBorgesnr/task_manager.git
cd task_manager/backend
```

### 2. Crie ative um ambiente virtual.

```bash
  python3 -m venv ./venv
  source venv/bin/activate # Para Linux/Mac
  venv\Scripts\activate     # Para Windows
```

### 3. Instale as dependências necessárias.

```bash
pip install -r requirements.txt
```

### 4. Para criar o banco de dados, execute:

```bash
python manage.py migrate
```

### 5. Crie um superusuário

```bash
python manage.py createsuperuser
```

### 5. Inicie o servidor de desenvolvimento.

```bash
python manage.py runserver
```

## 2. Configuração do Frontend

### 1. Em um novo terminal, acesse a pasta do frontend.

```bash
cd task_manager/frontend
```

### 2. Instale as dependências.

```bash
npm install
```

### 3. Inicie o servidor de desenvolvimento.

```bash
npm start
```
