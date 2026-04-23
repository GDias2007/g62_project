#g62_project

Introdução 
Este projeto foi desenvolvido no âmbito da Unidade Curricular de Programação de Computadores II. O objetivo é a criação de um sistema de gestão de dados bancários, integrando conceitos de Programação Orientada a Objetos em Python com a persistência de dados em SQLite.

O sistema permite a gestão de bancos, agências, cartões e clientes, processando transações financeiras a partir de fontes de dados externas (CSV).


Elementos do Grupo
Benedita Lima – up202504086

Gonçalo Dias – up202506658

Maria Teresa Teixeira – up202504649

Teresa Carvalho – up202504860


Estrutura da Pasta do Projeto
* classes: Pasta que contém as definições das classes (bank.py, branch.py, card.py, customer.py, transaction.py). Cada ficheiro implementa a lógica de negócio e herda as funcionalidades da Gclass.
* data: Pasta destinada ao armazenamento da base de dados SQLite (g62_database.db).
* diagrama: Diagrama de Classes UML que representa o modelo de dados e as relações entre as entidades (incluindo a relação Muitos-para-Muitos).
* README: Este ficheiro de documentação e introdução ao projeto.
