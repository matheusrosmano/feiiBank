# Feiibank

> Não leve a sério o nome do projeto e nem sua descrição

## Conteúdo

* [Sobre](#Sobre)
* [Requisitos](#requisitos)
* [Desenvolvimento](#desenvolvimento)
* [Api](#Api)

## Sobre

Sejam bem-vindos ao banco criado para os feios, o `Feiibank`. O `Feiibank` surgiu da necessidade dos feios poderem ter
uma conta bancária sem ser descriminados por serem feios.

Conta 100% digital e gratuita, cujo objetivo é atender aqueles que desejam entrar no mundo digital.

## Requisitos

Certifique-se de que em sua máquina esteja instalado os seguintes programas:

1. python3
1. python3-pip
1. python3-devel
1. git

## Desenvolvimento

**obs**: O pip usado em comandos é o pip3, e o python é o python3. O que foi feito é somente um link simbolico para
agilizar o comando

1. Crie o ambiente virtual
    ```
    python -m venv venv
    ```
1. Ative o ambiente virtual
    ```
    source venv/bin/activate
    ```
1. Instale as libs necessárias para o projeto
    ```
    pip install -r requirements.txt
    ```
1. Crie o arquivo `backend/db.ini` baseado no `backend/db.ini.modelo` e ajuste suas variaveis
1. Pronto, seu projeto pode ser executado

## Api

A api foi criada para uso interno do banco, com o intuito de escalabilidade e perfomance do app. Além de que o banco
possui microserviços que facilitam sua vida.

Para iniciar a api basta ir no terminal e digitar o seguinte comando:

```
make server-start
```