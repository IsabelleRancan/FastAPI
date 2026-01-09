***ANOTAÇÕES SOBRE FASTAPI***

**Section 2: Introdução ao FastAPI**

*Prática - Primeira API*
1 - Criando um ambiente virtual para a pasta nova
Instalando fast api e uvicorn (servidor para executar códigos assíncronos)
-> python -m venv venv
-> venv\Scripts\activate
-> pip install fastapi gunicorn uvicorn
-> pip freeze > requirements.txt
-> deactivate

*versão fastapi utilizada 0.75.2
(pra instalar essa versão pip install fastapi==0.75.2)
*versão uvicorn 0.17.6

2 - Criando o main.py
Importamos o fast api no arquivo novo e inicializamos a API

from fastapi import FastAPI

app = FastAPI() //instanciando o objeto FastAPI

@app.get('/') //decorator com todas as funções (get, post, del...). Esse app tem esse nome porque é o nome que demos pra instanciar a FastAPI
async def raiz(): // essa função vai ser chamada quando diretório raiz for chamado 
    return {"msg:" 'FastAPI'}

3 - Executando a API:
*no terminal: uvicorn main:app
*ctrl + c (para desativar)
Quando abrimos no navegador, vemos o retorno da API. Podemos clicar em 'inspecionar' na tela no navegador e ir na aba 'network' pra saber sobre as informações da API

A FastAPI gera documentação automática pra nós em: caminho_da_uri/docs ou /redc para um novo formato de documentação 

O ambiente de navegador não é o melhor para testar APIs então vamos usar uma extensão de cliente dentro do próprio VSCode, chama-se Thunder Client 

4 - Recompilando o código automáticamente
Quando fazemos uma mudança no código, teríamos que recarregar o código de novo, ou no terminal podemos executar ele da seguinte forma: uviconr main:app --reload

Outra forma mais fácil e recomendada de fazer isso é atravéz de uma entrada no código do arquivo 'main', colocamos da seguinte forma: 

if __name__ == '__main__': //independente do nome do seu arquivo, de forma interna ele sempre vai se chamar 'main' para o python 
    import uvicorn

    uvicorn.run("main:app", host="127.0.0.1", port=8000, log level="info", reload=True) //aqui estamos colocando onde o arquivo está salvo, a porta, e mandando ele recarregar de forma automática. Também podemos deixar o host em 0.0.0.0 para que qualquer pessoa com acesso a rede possa acessar minha API através do IP da minha máquina que está rodando a API, basta informar: http://IP_da_máquina:8000/


**Section 3: Entendendo os conceitos do FastAPI**

*Prática - Definindo o novo Projeto*
1 - Criamos uma nova pasta e geramos o ambiente virtual 
2 - Criamos o arquivo 'models.py' e importamos algumas classes
3 - Criamos o arquivo 'main.py' e criamos um dicionário de cursos 
4 - Criamos a entrada no código para ele recarregar de forma automática

- O arquivo models é responsável por definir os modelos de dados da aplicação.
Ele representa a estrutura das tabelas do banco de dados e é utilizado pelo ORM (Mapeamento Objeto-Relacional) para realizar consultas e manipulações de dados de forma mais prática.
Cada classe definida em models corresponde a uma tabela do banco de dados, e cada atributo da classe representa uma coluna dessa tabela.
- O arquivo main é o arquivo principal da aplicação, responsável por inicializar e configurar a API.
É nele que a aplicação é criada e onde são registradas rotas, configurações e dependências.
Quando a aplicação é executada diretamente por esse arquivo, o bloco
if __name__ == "__main__" é utilizado para iniciar o servidor.

-> Resolvendo o problema de importação que surgiu: as importações não estavam funcionando no código. 
A solução encontrada é porque o interpretador estava errado então fizemos o seguinte: 
ctrl + shift + P;
digitar 'python'
selecionar a opção de 'escolher interpretador'
selecionar o interpretador instalado no ambiente virtual

*Prática - O Método GET*

@app.get('/cursos')
async def get_cursos():
    return cursos

Quando vamos criar uma rota (endpoint), sempre usamos o decorador '@' para associar essa rota a uma função.
Neste exemplo estamos criando um endpoint para cursos com uma função assincrona chamada 'get_cursos' e essa função vai retornar o dicionário 'cursos' que foi criado no arquivo.

@app.get('/cursos/{curso_id}')
async def get_curso(curso_id : int):
    curso = cursos[curso_id]
    curso.update({"id" : curso_id})
    return curso

Neste outro trexo de código, estamos criando outra função get que recebe o id de um dos cursos e retorna as informações sobre ele. 
Quando usamos python, geralmente usamos 'int(variável)' para defnir uma variável do tipo inteiro, porém em FastAPI, temos uma forma mais fácil e rápida de fazer isso:
'async def get_curso(curso_id : int):'
Esta é a linha de definição da função, quando passamos os atributos dentro dela, já podemos tipa-los.

*Prática - Tratando Exceções*
Para tratar ecxeções, fazemos duas importações dentro do nosso código:

'from fastapi import HTTPException
 from fastapi import status'

OBS: ctrl+clicar em cima do status mostra as faixas de erro mais comuns utilizadas.

Agora no código, o lançamento e tratamento de exceções fica assim:

@app.get('cursos/{curso_id}')
async def get_curso(curso_id : int):
    try:
        curso = cursos[curso_id]
        return curso
    except KeyError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Curso não encontrado.')

Colocamos o 'try' como a primeira opção e caso ocorra um erro lançamos 'raise' escolhendo o código do erro (neste caso foi 404) e detalhamos o que foi o erro. Neste caso é quando um curso não foi encontrado (lançamos um ID que ainda não foi criado no dicionário).
