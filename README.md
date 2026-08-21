# CRUD de Usuários

Aplicação de gerenciamento de usuários desenvolvida em Python utilizando SQLite.

O projeto implementa as operações básicas de um sistema CRUD (Create, Read, Update e Delete), permitindo cadastrar, consultar, atualizar e excluir usuários através de uma interface interativa no terminal.

## Funcionalidades

* Cadastro de usuários
* Listagem de usuários cadastrados
* Atualização de dados
* Exclusão de usuários
* Armazenamento dos dados em banco SQLite
* Interface interativa através do terminal

## Tecnologias

* Python
* SQLite
* SQL

## Estrutura do Projeto

```text
CRUD/
│
├── main.py
├── crud.py
├── database.py
└── README.md
```

### main.py

Responsável pelo fluxo principal da aplicação e pela interação com o usuário através do terminal.

### crud.py

Contém as operações de criação, leitura, atualização e exclusão dos registros.

### database.py

Responsável pela configuração e comunicação com o banco de dados SQLite.

## Como Executar

### 1. Clone o repositório

```bash
git clone https://github.com/Saboyyya/CRUD.git
```

### 2. Acesse a pasta

```bash
cd CRUD
```

### 3. Execute a aplicação

```bash
python main.py
```

## Conceitos Aplicados

Este projeto foi desenvolvido para praticar conceitos fundamentais de desenvolvimento de software, incluindo:

* Operações CRUD
* Banco de dados relacional
* SQL
* SQLite
* Separação de responsabilidades
* Organização de código em diferentes módulos
* Entrada e processamento de dados
* Lógica de programação

## Objetivo

O objetivo do projeto é aplicar conceitos de programação em Python e integração com banco de dados, criando uma aplicação simples capaz de realizar operações completas de persistência de dados.

## Próximas Melhorias

* [ ] Implementar validação dos dados de entrada
* [ ] Adicionar tratamento de exceções
* [ ] Criar uma interface gráfica
* [ ] Adicionar busca de usuários
* [ ] Implementar testes automatizados
* [ ] Melhorar a organização das camadas da aplicação

## Autor

**Júlio César Saboya**

Estudante de Sistemas de Informação e desenvolvedor interessado em desenvolvimento web e desenvolvimento de software.

[GitHub](https://github.com/Saboyyya)
