===============
Programação Web
===============

Este é o repositório da disciplina de Programação Web para o semestre 1/2018 na Faculdade do Gama/UnB. Este arquivo contêm informações básicas sobre a disciplina e o plano de ensino do semestre.


Informações básicas
===================

Curso: 
    Engenharia de Software
Professor: 
    Fábio Macêdo Mendes
Disciplina: 
    Programação Web
Semestre/ano: 
    01/2018
Carga horária: 
    60 h
Créditos: 
    04


Ementa
======

* Conceitos básicos de tecnologia Web
* HTML5, Javascript e CSS
* Frameworks para desenvolvimento e MVC
* Servidores de aplicação
* APIs e interoperabilidade
* Testes em aplicações Web


Horário das aulas e atendimento
===============================

Aulas teóricas e de exercícios: terças e quintas-feiras às 16h 
Atendimento e monitoria: a definir


Metodologia
===========

O método básico aplicado é o de aulas práticas em laboratório de computação voltadas à implementação de funcionalidades dentro de um projeto compartilhado port toda a turma. As aulas podem conter partes expositivas orientadas à discussão da teoria e ferramentas utilizadas. As aulas também serão complementadas com atividades de exercícios e demandas extra-classe. Os alunos devem se cadastrar no Github e acompanhar o repositório da turma (https://github.com/fabiommendes/progweb).

Este semestre (1/2018) será dedicado a implementar um microframework baseado em Django.


Critérios de avaliação
======================

Cada aluno será avaliado com uma nota numérica onde a conversão entre a pontuação e a menção final é feita da forma usual: 9,0pts+: SS, 7,0pts+: MS, 5,0pts+: MM, 3,0pts+: MI e < 3,0 pts II. A distribuição de pontos ao longo do curso segue a fórmula::

    NotaFinal = 0.15 * P1 + 0.30 * P2 + 0.15 * ME + 0.40 * MT

onde P1 e P2 consistem na nota das provas 1 e 2; ME representa a média dos exercícios individuais (feitos em casa); MT representa a média dos testes realizados em sala de aula. Os testes serão resolvidos em grupos de tamanho e composição variávies e consistem em tarefas esporádicas realizadas durante a aula e na nota da "Hackaton" de Programação Web, que será executada em duas edições.

Gamificação
-----------

O aluno poderá fazer algumas tarefas opcionais que dão direito a "poderes especiais" e outras vantagens ao longo do curso. Estes "poderes" podem modificar a nota final, abonar faltas, entre outros. Esta seção lista as tarefas disponíveis e os poderes associados.

Django girls
~~~~~~~~~~~~

O aluno que participar como *coach* do Django-Girls ganha o direito de converter a menor nota de teste em 10. Não pode ser aplicado na nota da Hackaton.


Prova substitutiva e faltas
---------------------------

O curso não inclui prova substitutiva. Caso o aluno possua uma falta justificada no dia da primeira prova, deverá apresentar um comprovante na aula seguinte à prova ou quando terminar a licença médica. Esta justificativa não abona falta, mas dá direito ao aluno utilizar a segunda prova como prova substitutiva. 

O aluno pode faltar até 7 vezes em um semestre. Faltas com justificativa médica não serão abonadas, exceto em casos excepcionais. Os alunos reprovados por falta ficarão com uma menção igual a SR.


Código de ética e conduta
-------------------------

Algumas avaliações serão realizadas com auxílio do computador no laboratório de informática. Todas as submissões serão processadas por um programa de detecção de plágio. Qualquer atividade onde for detectada a presença de plágio será anulada sem a possibilidade de substituição. Não será feita qualquer distinção entre o aluno que forneceu a resposta para cópia e o aluno que obteve a mesma.

As mesmas considerações também se aplicam às provas teóricas que serão respondidas à mão.


Informações importantes
========================

Este curso utiliza GitHub + Github Classroom e o Google classroom para gerenciar o curso. A comunicação com a turma é feita através do Google Classroom ou por issues no repositório do Github. Habilite a funcionalidade "Watch" no repositório para receber notificações sobre atualizações.

Google Classroom:
    http://classroom.google.com/ - Código de inscrição: nllue7
Github:
    http://github.com/fabiommendes/progweb/
Github Classroom:
    http://github.com/programacao-web/
    

Prepare-se
==========

Ao longo do curso abordaremos uma série de tecnologias em diferentes níveis de profundidade. Recomenda-se que cada aluno providencie a instalação de todos os pacotes o mais rapidamente o possível. O curso subentende um ambiente de desenvolvimento Linux funcional para realizar as atividades propostas no curso. É possível desenvolver em outras plataformas (ex. Windows e Mac), mas o curso assume que as entregas utilizem algum container Docker especificado pelo professor. Isto, naturalmente, exige ao menos algum nível de emulação do Linux utilizando o Docker machine, Vagrant ou similar.

Docker + docker-compose:
    O curso disponibilizará algumas imagens Docker configuradas com as ferramentas essenciais utilizadas no curso (o link segue em breve). Todos os trabalhos serão testados em containers baseados nestas imagens. Ainda que o Docker contenha as ferramentas de desenvolvimento essenciais, recomenda-se a instalação local dos pacotes abaixo. 
Python 3.6+: 
    É necessário um ambiente Python 3.6 ou superior com todos os pacotes de desenvolvimento instalados. No Ubuntu/Debian precisamos do python3-dev, python3-pip, python3-virtualenv
Node.js e npm (ou Yarn): 
    Certifique-se que é possível baixar pacotes do Node.js para o frontend. Vários desenvolvedores preferem o Yarn como alternativa ao NPM.
Sass (ou Ruby): 
    Se a distribuição não possui o pacote do Sass, instale o Ruby e digite ``sudo gem install sass``.
Nginx, Postgres:
    Servidor de arquivos e banco. Não é necessário/recomendável fazer a instalação local, mas já se adiante e para baixar a imagem do docker hub: ``sudo docker pull nginx`` e ``sudo docker pull postgres``
Git, editor de código, conta no github: 
    Kit básico ;)
Versão atualizada do Chrome:
    Algumas partes do curso poderão utilizar funcionalidades que (atualmente) estão implementadas somente no Google Chrome. Certifique que seu computador possui uma versão atualizada deste navegador.
Outros:
    Virtualenvwrapper (``sudo apt-get install virtualenvwrapper``), Pytest (``pip3 install pytest --user``), Invoke (``pip3 install invoke --user``), Webpack (``sudo npm install -g webpack``)
Sugestões de editor de código:
    Utilize o seu favorito. Caso precise de uma recomendação, seguem algumas:
    
    * PyCharm Educacional - IDE com ótimos recursos de introspecção e refatoração que adora memória RAM. Possui versão livre e versão profissional gratuita para estudantes.
    * VSCode - um bom meio termo entre uma IDE e um editor de código leve. Criado para Javascript, mas possui plugins para Python e várias outras linguagens.
    * Vi/Vim - herança dos anos 70 que nunca morre. Instale os plugins para Python e Javascript.


Cronograma de atividades
========================

+--------+-------+------------------------------------------------------------+
| Semana | Data  |                            Aula                            |
+========+=======+============================================================+
| 1      | 06/03 | Início das aulas – Apresentação do curso e tecnologias Web |
|        |       |                                                            |
|        |       | * HTML5 e XML                                              |
|        |       | * Marcação de text e hipertexto                            |
|        |       | * CSS                                                      |
|        |       | * Javascript                                               |
+--------+-------+------------------------------------------------------------+
|        | 08/03 | HTML                                                       |
|        |       |                                                            |
|        |       | * Histórico: SGML, HTML, XML, XHTML, HTML5, etc            |
|        |       | * HTML semântico                                           |
|        |       | * Estruturando um hipertexto                               |
|        |       | * Design progressivo                                       |
|        |       | * Tags personalizadas, divs e spans                        |
|        |       | * Formatos XML embutidos (SVG, MathML)                     |
+--------+-------+------------------------------------------------------------+
| 2      | 13/03 | CSS                                                        |
|        |       |                                                            |
|        |       | * Propriedades básicas                                     |
|        |       | * Seletores                                                |
|        |       | * Cascata e prioridades de seletores                       |
|        |       | * Sass e pré-compiladores CSS                              |
|        |       | * Inverse triangle e metodologias CSS                      |
+--------+-------+------------------------------------------------------------+
|        | 15/03 | Design responsivo                                          |
|        |       |                                                            |
|        |       | * Media queries                                            |
|        |       | * Flex boxes                                               |
|        |       | * “Mobile first/responsive design”                         |
|        |       | * Frameworks (e.g.: Twitter Bootstrap)                     |
+--------+-------+------------------------------------------------------------+
| 3      | 20/03 | JavaScript                                                 |
|        |       |                                                            |
|        |       | * História                                                 |
|        |       | * Sintaxe                                                  |
|        |       | * Tipos básicos e estruturas de dados                      |
|        |       | * Herança de protótipo                                     |
|        |       | * "The good parts"                                         |
+--------+-------+------------------------------------------------------------+
|        | 22/03 | Javascript no navegador                                    |
|        |       |                                                            |
|        |       | * Ferramentas de depuração e inspeção                      |
|        |       | * DOM e modelo de dados                                    |
|        |       | * APIs básicas Manipulação da DOM                          |
|        |       | * jQuery vs nativo                                         |
+--------+-------+------------------------------------------------------------+
| 4      | 27/03 | Web components                                             |
|        |       |                                                            |
|        |       | * Templates                                                |
|        |       | * Custom elements                                          |
|        |       | * Shadow DOM                                               |
|        |       | * HTML Imports                                             |
|        |       | * Bibliotecas e interpretações                             |
+--------+-------+------------------------------------------------------------+
|        | 29/03 | Stencil.js (ou outra biblioteca de Web Components)         |
|        |       |                                                            |
|        |       | * Criação de componentes e decoradores                     |
|        |       | * Typescript                                               |
|        |       | * JSX                                                      |
|        |       | * Compilação e distribuição                                |
+--------+-------+------------------------------------------------------------+
| 5      | 03/04 | Arquitetura e ferramentas Django                           |
|        |       |                                                            |
|        |       | * Preparação de ambiente                                   |
|        |       | * Ferramentas                                              |
|        |       | * Apps/Projetos (https://djangopackages.org/)              |
|        |       | * Arquitetura MVC (ou MTV)                                 |
|        |       | * Views, requests, responses e middlewares                 |
+--------+-------+------------------------------------------------------------+
|        | 05/04 | Templates vs pseudo-DOM                                    |
|        |       |                                                            |
|        |       | * Linguagens de template e views                           |
|        |       | * Jinja2 + Django                                          |
|        |       | * ELM, Hyperapp, JSX, Python bricks                        |
+--------+-------+------------------------------------------------------------+
| 6      | 10/04 | ORM do Django                                              |
|        |       |                                                            |
|        |       | * Relação com o banco de dados                             |
|        |       | * Criação/remoção de objetos                               |
|        |       | * Validação                                                |
|        |       | * Busca de elementos                                       |
+--------+-------+------------------------------------------------------------+
|        | 12/04 | Managers e QuerySets                                       |
|        |       |                                                            |
|        |       | * Querysets e SQL                                          |
|        |       | * Problema N + 1 e eficiência do ORM                       |
|        |       | * Personalizando QuerySets para um modelo                  |
+--------+-------+------------------------------------------------------------+
| 7      | 17/04 | AJAX                                                       |
|        |       |                                                            |
|        |       | * JSON                                                     |
|        |       | * Gerando JSON em Python e Javascript                      |
|        |       | * Método Fetch                                             |
|        |       | * Servindo JSON                                            |
|        |       | * Django REST Framework                                    |
+--------+-------+------------------------------------------------------------+
|        | 19/04 | Arquitetura REST                                           |
|        |       |                                                            |
|        |       | * API                                                      |
|        |       | * Verbos HTTP                                              |
|        |       | * Interface REST                                           |
|        |       | * Alternativas ao REST                                     |
+--------+-------+------------------------------------------------------------+
| 8      | 24/04 | Arquitetura microframework                                 |
|        |       |                                                            |
|        |       | * Flask                                                    |
|        |       | * Blog em Flask                                            |
+--------+-------+------------------------------------------------------------+
|        | 26/04 | Dojo - Micro Django                                        |
|        |       |                                                            |
+--------+-------+------------------------------------------------------------+
| 9      | 01/05 | *Feriado - Dia do Trabalho*                                |
|        |       |                                                            |
+--------+-------+------------------------------------------------------------+
|        | 03/05 | **Prova I**                                                |
|        |       |                                                            |
+--------+-------+------------------------------------------------------------+
| 10     | 08/05 | Testes unitários                                           |
|        |       |                                                            |
|        |       | * Biblioteca “pytest”                                      |
|        |       | * Casos de teste e classes de teste                        |
|        |       | * Fixtures e conftest.py                                   |
|        |       | * Especificidades de testes em ambiente Django/web         |
|        |       | * Utilizando dados falsos                                  |
+--------+-------+------------------------------------------------------------+
|        | 10/05 | Testes funcionais                                          |
|        |       |                                                            |
|        |       | * Selenium                                                 |
|        |       | * Controlando o navegador                                  |
|        |       | * Testes em JavaScript                                     |
+--------+-------+------------------------------------------------------------+
| 11     | 17/05 | Micro Django - views                                       |
|        |       |                                                            |
|        |       | * Tipos de rotas                                           |
|        |       | * Verbos HTTP                                              |
|        |       | * Decoradores                                              |
|        |       | * Type hints e introspecção de assinatura                  |
+--------+-------+------------------------------------------------------------+
|        | 19/05 | Micro Django - Dojo                                        |
|        |       |                                                            |
+--------+-------+------------------------------------------------------------+
| 12     | 22/05 | Docker                                                     |
|        |       |                                                            |
|        |       | * Isolamento de ambiente: containers e imagens             |
|        |       | * Sistema de arquivos                                      |
|        |       | * Dockerfile                                               |
|        |       | * Docker compose                                           |
+--------+-------+------------------------------------------------------------+
|        | 24/05 | Empacotamento e gerência de configuração                   |
|        |       |                                                            |
|        |       | * Setuptools e PIP                                         |
|        |       | * Invoke                                                   |
|        |       | * Tox e integração contínua                                |
+--------+-------+------------------------------------------------------------+
| 13     | 29/05 | Micro Django - API                                         |
|        |       |                                                            |
|        |       | * Roteadores e end-points                                  |
|        |       | * Construção automática de end-points                      |
+--------+-------+------------------------------------------------------------+
|        | 31/05 | *Feriado - Corpus Christi*                                 |
|        |       |                                                            |
+--------+-------+------------------------------------------------------------+
| 14     | 05/06 | Micro Django - ORM                                         |
|        |       |                                                            |
|        |       | * Revisitando declarações                                  |
|        |       | * Type hints                                               |
|        |       | * Metaclasses                                              |
+--------+-------+------------------------------------------------------------+
|        | 07/06 | Micro Django - Dojo                                        |
|        |       |                                                            |
+--------+-------+------------------------------------------------------------+
| 15     | 12/06 | Micro Django - QuerySet                                    |
|        |       |                                                            |
|        |       | * Revisitando a sintaxe de filtros                         |
|        |       | * API Pydata                                               |
|        |       | * Active Record: pattens e anti-patterns                   |
+--------+-------+------------------------------------------------------------+
|        | 14/06 | Micro Django - Dojo                                        |
|        |       |                                                            |
+--------+-------+------------------------------------------------------------+
| 16     | 19/06 | Permissões e autorização                                   |
|        |       |                                                            |
|        |       | * Permissões                                               |
|        |       | * Autenticação e autorização                               |
|        |       | * Django-rules                                             |
+--------+-------+------------------------------------------------------------+
|        | 21/06 | Segurança na rede                                          |
|        |       |                                                            |
|        |       | * Injeção de SQL                                           |
|        |       | * CSRF                                                     |
|        |       | * XSS                                                      |
|        |       | * DoS                                                      |
+--------+-------+------------------------------------------------------------+
| 17     | 26/06 | Formulários                                                |
|        |       |                                                            |
|        |       | * Inputs em HTML                                           |
|        |       | * GET e POST                                               |
|        |       | * Classes do tipo “Form”                                   |
|        |       | * Formulários baseados em modelos                          |
|        |       | * Apresentando um formulário                               |
+--------+-------+------------------------------------------------------------+
|        | 28/06 | **Prova II**                                               |
|        |       |                                                            |
+--------+-------+------------------------------------------------------------+
| 18     | 03/07 | Livre                                                      |
|        |       |                                                            |
+--------+-------+------------------------------------------------------------+
|        | 05/07 | Revisão de nota                                            |
|        |       |                                                            |
+--------+-------+------------------------------------------------------------+

Obs.: O cronograma está sujeito a alterações.
