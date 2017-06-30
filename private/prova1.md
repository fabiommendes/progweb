Prova 1 - Programação Web
=========================

<center>UnB/Gama - 10/05/2017</center>

**Nome:**
**Matrícula:**

## Questão 1

Um dos principais elementos do Django é o seu ORM (Object Relational Mapper) que abstrai o banco de dados e expõe as linhas de uma tabela no banco como um objeto Python. Os modelos abaixo implementam uma aplicação simples do tipo "Twitter"

```python
from django.db import models

class User(models.Model):
    name = models.CharField(max_size=50)
    email = models.EmailField()

class Tweet(models.Model):
    user = models.ForeignKey(User, related_name='tweets')
    text = models.TextField()
    created = models.DateTimeField()
```

Responda:

1. Faça um esboço de como seriam as tabelas criadas no banco de dados para os dois modelos acima. Coloque alguns exemplos de usuários e tweets.
2. O que significa o campo ForeignKey() utilizado no objeto Tweet? Discuta as vantagens/desvantagens em se utilizar uma chave estrangeira em comparação a uma referência manual ao índice de User utilizando IntegerField, por exemplo.


## Questão 2

Responda as questões a respeito de busca em banco de dados:

1. O que são os `QuerySets` no Django?
2. Como seria a busca de todos os tweets produzidos por um determinado usuário? (Assuma que o usuário em questão é conhecido e salvo na variável `user`.)
3. Como seria uma busca por todos os tweets de um determinado usuário a partir de uma determinada data? Explique a notação utilizada para fazer isto no Django. (Assuma que tanto o usuário quanto a data já estão disponíveis nas variáveis `user` e `datetime`.)


## Questão 3

Acesso ao banco de dados é um dos principais fatores que influenciam na performance de uma aplicação Web. Suponha que queremos extrair os nomes dos autores e textos dos tweets para cada tweet do banco. As duas buscas abaixo realizam esta operação, mas possuem características de performance diferentes. Discuta qual é a mais eficiente e porquê.

```python
# Query 1
L = [(tweet.user.name, tweet.text) for tweet in Tweet.objects.all()]

# Query 2
L = list(Tweet.objects.values_list('user__name', 'text'))
```


## Questão 4

Explique o que são as "views" do Django e como elas se relacionam com as URLs de sua aplicação. Esboce uma view típica que extrai um objeto do banco de dados e renderize uma página correspondente em HTML.


## Questão 5

Uma requisição HTTP é formada por uma linha de verbo + url, cabeçalhos e corpo da mensagem. Explique a distinção entre os verbos GET e POST e descreva algumas situações onde é preferível utilizar um ao outro.


## Questão 6

Defina e explique sucintamente o que são cada uma das tecnologias abaixo e como elas são utilizadas no desenvolvimento de uma aplicação Web.

1. HTML
2. CSS
3. JavaScript
4. HTTP e HTTPS
5. SQL


## Questão 7

O que são testes unitários? Descreva os principais desafios de escrever testes unitários para aplicações Web. 