# Projeto de Gerenciamento de Tarefas e Registro de Tempo

Este projeto é uma aplicação web para gerenciamento de tarefas e registros de tempo, construída com duas partes principais:

- **Backend**: Utiliza Django e Django Rest Framework para criar uma API que gerencia as operações de tarefas e registros de tempo.
- **Frontend**: Utiliza React para fornecer uma interface interativa onde os usuários podem visualizar e interagir com suas tarefas e registros.

## Estrutura de Usuários

**A estrutura de usuários foi criada para permitir um controle geral do sistema, possibilitando a visualização e o gerenciamento de tarefas e registros de tempo de todos os usuários para cada grupo. Isso atende à necessidade de realizar filtros de usuários conforme descrito no desafio. Caso prefira, pode criar os próprios usuários e vinculá-los aos grupos existentes no sistema pelo Django Admin. Abaixo estarão alguns usuários para testes.**

Para fins de teste, foram criados os seguintes usuários do grupo Funcionários:

| Nome de Usuário | Senha |
| --------------- | ----- |
| rhuannoronha1   | 123   |
| rhuannoronha2   | 123   |

Além disso, foi criado um usuário do grupo Administradores:

| Nome de Usuário | Senha |
| --------------- | ----- |
| admin           | 123   |

Os usuários do grupo Funcionários têm acesso limitado e podem visualizar e gerenciar apenas suas próprias tarefas e registros de tempo. Os administradores, por outro lado, têm permissões para visualizar e gerenciar todas as tarefas e registros de tempo de todos os usuários.

## Pré-requisitos

Antes de começar, você precisa ter as seguintes ferramentas instaladas:

- **Python**: 3.8 ou superior
  - Para verificar a versão instalada:
    ```bash
    python --version
    ```
- **Node.js**: 14 ou superior
  - Para verificar a versão instalada:
    ```bash
    node --version
    ```
- **npm**: Node Package Manager
  - Para verificar a versão instalada:
    ```bash
    npm --version
    ```

## Configuração do Backend (Django)

### 1. Clonar o Repositório

```bash
git clone https://github.com/RhuanBorgesnr/task_manager.git
cd task_manager/backend
```

### 2. Criar um ambiente virtual.

```bash
  python3.8 -m venv ./venv
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

### 5. Crie um superusuário.

```bash
python manage.py createsuperuser
```

### 6. Inicie o servidor de desenvolvimento.

```bash
python manage.py runserver
```

**Acesse o backend em** http://localhost:8000.

## Configuração do Frontend

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
**Acesse o frontend em** http://localhost:3000.


## Executando os Testes

### Backend (Django)

```bash
python manage.py test
