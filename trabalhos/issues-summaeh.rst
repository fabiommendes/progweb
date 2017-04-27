Issues summaeh
==============

Lista de issues para o projeto do Summaeh (não está necessariamente na ordem 
correta).

* Criar apps básicos: accounts, events, videos
* Modelos básicos nos apps correspondentes: Vídeo, Evento, User, +?
* Esturtura de testes: unitários, integração, aceitação
* Git flow e definição de boas práticas com o git (https://danielkummer.github.io/git-flow-cheatsheet/)
* Configurar admin do Django para editar modelos
* Estrutura básica da página (componentes/frontend): 
    - header
    - nav bar
    - footer 
    - caixa de busca
    - vídeos recentes (carrossel)
    - detalhes do vídeo
    - vídeos reposta
    - lista de vídeos
        - item para lista de vídeos
    - profile
    - componente de paginação
    - lista de eventos
    - detalhes do evento
* Usuários podem postar novos vídeos (sem acesso ao admin)
* Integração contínua
* Docker de dev
* Docker de produção


Mudanças importantes:
* Todos vídeos serão atrelados a um evento
* Um vídeo-resposta é automaticamente vinculado a um vídeo
* Busca procura automaticamente em qualquer campo



Issues Codeschool/Sparta
========================

Existe um grupo de GPP/MDS que fará um app Android para o trezentos. Eles 
traçaram algumas especificações e podemos reaproveitá-las e usá-las como guia.

https://github.com/fga-gpp-mds/2017.1-Trezentos/wiki/Documento-de-Vis%C3%A3o

Cada instância consiste em uma página sob a página principal da
sala de aula. Normalmente a atividade Sparta será associada ao resultado de uma
prova. Assumimos que o professor é um admin e pode editar sua sala e 
todas as páginas abaixo dela. 


Modelos:
    - Modelo de SpartaActivity (subclasse de codeschool.lms.activities.Activity)
    - Lista de professores, estudantes vem do modelo de sala de aula.
    - Subclasses p/ SpartaProgress, SpartaSubmission, SpartaFeedback
    - Group -- grupo de estudantes com papéis definidos como tutor ou aprendiz
    - Role -- papel que cada usuário possui naquela atividade do sparta
    - Task -- uma tarefa criada pelos tutores
    - TutorForm, LearnerForm -- formulários de avaliação dos tutores
      e aprendizes. 
    - ...?


Papéis:
    - Professor (teacher)
    - Tutor (tutor)
    - Aprendiz (learner)


* Criar e gerenciar atividades do 300.
    Professor cria uma sala e passa um arquivo CSV com as notas de cada
    estudante para que o aplicativo monte automaticamente os grupos.
    
    - Professor define o tamanho de cada grupo e a nota de corte para definir 
      o papel de tutor vs aprendiz. App monta grupos do tamanho
      desejado casando as melhores notas com as piores, tentando manter o tamanho
      de cada grupo equilibrado.
    - Cada atividade tem um prazo e pode estar no estado ativo ou inativo.

* Os tutores podem recomendar a resolução de determinados exercícios já 
  disponíveis no Codeschool.
* Aprendizes podem rastrear quais exercícios já foram resolvidos e quais ainda 
  não foram.
* Membros de um grupo podem visualizar e-mail de todos outros membros e trocar
  mensagens num estilo perguntas e respostas
* Cada membro de um grupo pode avaliar os demais anonimamente
* Professor pode ver progresso de cada aluno, por grupo
* Professor pode salvar lista de notas da reaplicação e aplicação fecha as 
  notas finais

 

