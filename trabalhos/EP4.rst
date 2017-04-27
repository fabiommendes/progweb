Tecnologias de cliente
======================

Trabalho: EP4
Nota: 0,5 pts
Integrantes: individual
Data de entrega: 30/06/2017


Descrição
---------

O trabalho consiste em fazer o empacotamento para implantação do sistema 
desenvolvido no EP1/EP2. Faremos um container Docker e a integração com um 
serviço de integração contínua.

O tutorial será avaliado de acordo com os critérios:

* 0,1 pts - Cadastro em um serviço de integração contínua (ex. Travis, Circle-Ci, 
            Appveyor). Não precisa incluir os testes de aceitação. 
* 0,1 pts - Criação de um container de desenvolvimento utilizando apenas o 
            Docker.
* 0,1 pts - Criação e articulação de containers para implantação utilizando o 
            Docker compose.
* 0,1 pts - Container de demonstração registrado no Docker compose.
* 0,1 pts - Boas práticas + otimização das imagens criadas
 

Cada aspecto será avaliado como bom (0,1 pts), médio (0,05 pts) ou ruim (0,0 pts).
Todos os trabalhos serão públicos no respositório da disciplina.


Pontuação extra (estrelas) 
--------------------------

Cada membro receberá estrelas extra em função da tecnologia adotada para 
o tutorial.
 
* 1 estrela  - Cobertura de código contínua com algum serviço como Codecov, 
               Coveralls, etc.
* 1 estrela  - Análise de qualidade de código contínua. Configuração em algum 
               serviço como o Codeclimate, Quantified code, etc.
* 1 estrela  - Cadastro no PyPI com uma instalação funcional
* 1 estrela  - Subir o container de demonstração para o Docker hub.


Entrega
-------

A entrega será feita em conjunto no Moodle e Github. Os dockerfiles devem estar
presentes no respositório da aplicação.
