Testes e manutenção
===================

Trabalho: EP2
Nota: 0,5 pts
Integrantes: trabalho individual
Data de entrega: 17/05/2017


Descrição
---------

O trabalho consiste em montar uma suite de testes + integração contínua para um 
projeto Django simples. Idealmente, o projeto escolhido deve ser o mesmo do EP1,
mas você pode mudar de projeto se achar adequado.

O aplicativo deve implementar as funcionalidades abaixo:

* 0,1 pts - Implementação de alguns (5+) testes unitários (recomendo utilizar o 
            pytest, mas vocês podem utilizar outra biblioteca, se preferirem).
* 0,1 pts - Implementar pelo menos 2 testes de aceitação alguma biblioteca de
            automação como o Selenium, Letuce, ou Sulfur. 
* 0,1 pts - Uso de factories (Factory Boy, Model Mommy, Mommy's Boy, etc)
* 0,1 pts - Configuração do tox + análise de estilo (ex.: flake8)
* 0,1 pts - Cobertura de testes com mais de 85%. (70% ou mais para 0.05 pts).

Cada aspecto será avaliado como bom (0,1 pts), médio (0,05 pts) ou ruim (0,0 pts).
Os aplicativos devem ser impementados nas últimas versões do Django (1.10+) e em 
Python 3. Todos os trabalhos serão públicos no respositório da disciplina.


Pontuação extra (estrelas)
--------------------------

* 1 estrela  - pré-hook de comit que impeça comit de código que quebre algum 
               teste. Qualquer pré-hook vale a estrela, mas a boa prática diz 
               para apenas rodar a parte *rápida* da sua suite de
               testes. Isto normalmente exclui as partes que interagem com banco
               de dados e certamente exclui a parte com os testes de aceitação.
* 2 estrelas - Zero erros do flake8 (pode ignorar testes, migrações e arquivos 
               __init__.py que façam apenas imports).
* 1 estrela  - Utilizar a biblioteca Mock para evitar consultas desnecessárias
               ao banco de dados. Deve conter pelo menos 3 testes com mocks.

Entrega
-------

A entrega será feita em conjunto no Moodle, Github. Cada aluno deve possuir uma
nestes três serviços. O código deve estar disponível em 
um repositório público do Github e executando no PythonAnywhere. O README do 
repositório deve conter a badge do Travis e Codecov (ou serviços equivalentes). 
O Moodle é utilizado apenas para registrar a entrega do trabalho e apontar os links para
o repositório do Github e o endereço no PythonAnywhere.

