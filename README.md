# CadastroDeLivros
Este é um exemplo de aplicação CRUD (Create, Read, Update, Delete) de livros usando Python com o framework Django. A aplicação permite que os usuários realizem operações básicas de gerenciamento de livros, incluindo adicionar novos livros, visualizar detalhes de livros existentes, editar informações de livros e excluir livros do sistema. 

  

**Pré-requisitos**
Certifique-se de ter o Python e o Django instalados em seu sistema antes de prosseguir. 

  

**Instalação**

Clone este repositório para o seu ambiente de desenvolvimento local 

Navegue até o diretório do projeto 

Instale as dependências do projeto utilizando o pip e Execute as migrações do banco de dados para criar as tabelas necessárias: 

python manage.py migrate 

Inicie o servidor de desenvolvimento: 

python manage.py runserver 

Acesse a aplicação em seu navegador web utilizando o seguinte URL: 
**http://127.0.0.1:8000/livro_list/**

 

**Funcionalidades** 

Listar Livros: Visualize todos os livros cadastrados no sistema. 

Adicionar Livro: Adicione novos livros fornecendo informações como título, autor, gênero, etc. 

Visualizar Detalhes do Livro: Visualize os detalhes de um livro específico, incluindo todas as informações disponíveis. 

Editar Livro: Edite as informações de um livro existente, como título, autor, gênero, etc. 

Excluir Livro: Remova um livro do sistema. 

 

**Estrutura do Projeto**

A estrutura do projeto é organizada da seguinte forma:  

manage.py: Arquivo de gerenciamento do Django. 

djangoproject/: Diretório principal da aplicação. 

models.py: Define os modelos de dados para os livros. 

views.py: Define as views para manipulação das requisições HTTP. 

urls.py: Define as rotas URL para as views. 

templates/: Diretório contendo os templates HTML da aplicação. 

static/: Diretório contendo arquivos estáticos como CSS, JavaScript, etc. 

migrations/: Diretório contendo as migrações do banco de dados. 

**Licença**

Este projeto está licenciado sob a MIT License. 

 
