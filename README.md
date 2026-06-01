# G62 - Sistema de Gestão Bancária

## Introdução
Este projeto foi desenvolvido no âmbito da Unidade Curricular de **Programação de Computadores II**.

O objetivo é a criação de um sistema de gestão de dados bancários, integrando conceitos de Programação Orientada a Objetos em Python com persistência de dados em SQLite e uma interface web desenvolvida com Flask.

O sistema permite gerir bancos, agências, cartões, clientes e transações financeiras, processando dados a partir de fontes externas (CSV) e expondo-os através de uma aplicação web com autenticação de utilizadores.

---

## Elementos do Grupo
| Nome | Número de Aluno |
|---|---|
| Benedita Lima | up202504086 |
| Gonçalo Dias | up202506658 |
| Maria Teresa Teixeira | up202504649 |
| Teresa Carvalho | up202504860 |
| Francisca Pinho | up202506272 |

---

## Estrutura do Projeto
```
g62_project/
├── classes/
│   ├── gclass.py        # Classe genérica base
│   ├── bank.py          # Classe Bank
│   ├── branch.py        # Classe Branch
│   ├── card.py          # Classe Card
│   ├── customer.py      # Classe Customer
│   ├── transaction.py   # Classe Transaction
│   └── userlogin.py     # Classe Userlogin
├── data/
│   ├── Bancos.db        # Base de dados principal
│   └── business.db      # Base de dados de utilizadores
├── subs/
│   ├── apps_gform.py    # Módulo Flask para formulários
│   └── apps_userlogin.py# Módulo Flask para utilizadores
├── templates/
│   ├── base.html        # Template base com menu de navegação
│   ├── index.html       # Página inicial
│   ├── gform.html       # Formulário genérico (CRUD)
│   ├── login.html       # Página de login
│   └── userlogin.html   # Gestão de utilizadores
├── static/
│   └── css/
│       └── main.css     # Estilos da aplicação
├── app.py               # Ficheiro principal Flask
├── datafile.py          # Configuração do caminho da base de dados
└── README.md            # Este ficheiro
```

---

## Modelo de Dados

O sistema é composto por 5 entidades principais:

- **Bank** — banco (id, designação, data de fundação)
- **Branch** — agência bancária (id, morada, banco)
- **Card** — cartão bancário (id, nome, tipo, banco)
- **Customer** — cliente (id, nome, NIF, email, banco)
- **Transaction** — transação financeira (id, data, montante, cartão)

---

## Tecnologias Utilizadas
- **Python 3**
- **Flask** — framework web
- **SQLite** — base de dados
- **Pandas** — importação e processamento de dados CSV
- **HTML / CSS** — interface web

---

## Como Instalar e Correr

**1. Instalar as dependências:**
```bash
pip install flask bcrypt
```

**2. Correr a aplicação:**
```bash
python app.py
```

**3. Abrir no browser:**
```
http://127.0.0.1:5000
```

---

## Repositório GitHub
[https://github.com/GDias2007/g62_project]
