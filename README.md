# Formulário com Django

Django REST API de clientes  
Deploy no Heroku

## 🔨 Funcionalidades do projeto

Registrar clientes [nome, email, cps, rg, celular, ativo]  
Validação dos campos cadastrados  
Filtros de campo, ordenação e pesquisa  
Paginação e autenticação básica implementada  
Métodos permitidos autenticado: GET, POST, PUT e DELETE  
Quando não autenticado: GET e POST

## ✔️ Técnicas e tecnologias utilizadas

- `Python`
- `Django`
- `Django REST Framework`

## 🛠️ Abrir e rodar o projeto

Para abrir e rodar o projeto, execute os comandos:
- python -m venv venv
- venv/scripts/activate
- pip install -r requirements.txt
- py populate_script.py
- py manage.py makemigrations
- py manage.py migrate
- py manage.py createsuperuser
- py manage.py runserver
