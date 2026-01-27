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

Formas de inicializar a API:
-> python (nome_do_arquivo).py
-> ctrl + c
-> uvicorn main:app --reload

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

*Prática - O Método POST*
A primeira coisa que fazemos no arquivo 'main.py' é importar a classe que criamos no arquivo 'models'.

from models import Curso

Depois disso criamos o próximo endpoint:

@app.post('/cursos', status_code=status.HTTP_201_CREATED)
async def post_curso(curso: Curso):
    next_id: int = len(cursos) + 1
    cursos[next_id] = curso
    del curso.id
    return curso 

Neste exemplo acessamos o método POST, e definimos o código de status no próprio end point, ele vai retornar o código caso dê certo!
Em baixo estamos definindo umna função assíncrona chamada 'post_curso' que recebe um objeto 'curso' do tipo 'Curso' -> (curso: Curso)
Depois criamos a variável 'next_id' que é do tipo inteiro e será o nosso 'contador' para definir o número do próximo id.
Acessamos o próximo lugar do dicionário 'cursos', já criado no nosso arquivo 'main', com a variável 'next_id' e adicionamos as informações enviadas via método POST.
Apagamos o id de curso apenas por causa da vizualização do servidor na hora de imputar os dados.
Ele retorna o dicionário 'curso', agora com as novas informações imputadas.

Para utilizarmos o método POST, temos que enviar os dados usando JSON da seguinte forma:

{
    "titulo": 'Aula X',
    "aulas": 54,
    "horas": 12
}

*Prática - O Método PUT*
O PUT é utilizado para atualizar algo já existente

@app.put('/cursos/{curso_id}')
async def put_curso(curso_id: int, curso: Curso):
    if curso_id in cursos:
        cursos[curso_id] = curso
        del curso.id

        return curso
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Não existe um curso com o id {curso_id}')

A aplicação do método post assemelha-se muito ao método GET. Primeiro passamos a URI com o espaço para receber o ID.
Na definição da função, já definimos que vamos receber um ID e as informações de um novo curso, que será um objetoda classe 'Curso'. Como já definimos quais são os padrões do nosso dicionário 
no arquivo models, não precisamos nos preocupar com os atributos obrigatórios ou em definir a estrutura do que vai ser informado.
No início da função fazemos uma verificação se o id informado existe no nosso dicionário, se existir ele vai substituir as informações existentes pelas informadas agora.
O 'del curso.id'é apenas um tratamente para aexibição do novo dicionário. 
Caso o id informado não seja econtrado, lança-se uma excessão.

*Prática - O Método DELETE*

@app.delete('/cursos/{curso_id}')
async def delete_curso(curso_id: int):
    if curso_id in cursos:
        del cursos[curso_id]
        return Response(status_code=status.HTTP_204_NO_CONTENT)
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Não existe um curso com o id {curso_id}')

Uma função sempre retorna alguma coisa, por isso vamos fazer a seguinte importação:

from fastapi import Response

Essa importação permite que retornemos a resposta quando o método 'delete' dá certo.

*Prática - Path Parameters*

O que é o Path? O path é o parametro que passamos na URI após o endpoint.
O Path é uma espécie de validação a mais que implementamos dentro da nossa URI para limitar algumas coisas.

from fastapi import Path

Vamos aplicar o Path Parameters dentro do nosso método GET:

@app.get('cursos/{curso_id}')
async def get_curso(curso_id : int = Path(default=None, title='ID do curso', description='Deve ser entre 1 e 2', gt=0, lt=3))
    try:
        curso = cursos[curso_id]
        return curso
    except KeyError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Curso não encontrado.')

A única coisa obrigatória nos Path Parameters é o uso do default, todo o resto é opcional, no caso do exemplo, estamos definindo um título e uma descfrição para que isso apareça na documentação, depois utilizamos o 'Greather Then' e 'Lower Then' para definirmos o intervalo dos números que serão aceitos.

*Prática - Query Parameters*

Os Query Parameters geralmente não são tão utilizados nas APIs. Na maioria das vezes utilizamos os Path parêmeters para definir os tipos e limitações de dados para a nossa URI. 
Já os Query parêmeters são uma espécie de 'filtro' que aplicamos para exibirmos os dados. 

Path Parameters: Integrados ao caminho da URL, geralmente entre barras (/) e podem ser definidos com marcadores como {id} no backend.
Query Parameters: Após um ponto de interrogação (?), com múltiplos parâmetros separados por &.

Como aplicamos no backend?
Vamos criar uma função aleatória, apenas para testarmos o uso.

from fatsapi import Query

@app.get('/calculadora')
async def calcular(a: int = Query(default+None, gt=5), b: int = Query(default=None, gt=10), c: Optional [int] = None)
    soma: int = a + b
    if c:
        soma = soma + c

    return {"resultado": soma}

Note que criamos uma função get, a função get serve para retornar e não para salvar informações, como então vamos passar os valores para essa soma? Através dos Query Parameters na URL

...../calculadora?a=6&b=2&c=5

Estamos passando os vaores de A, B e C.
Lembrando que este é apenas um exemplo prático de como funciona e não a forma ideal ou a mais utilizada no cootidiano já que o uso de Query geralmente é feito para filtragem, busca e ordenação de resultados. 

*Prática - Header Parameters*
Ao contrário dos Query Parameters ou Path Parameters, o Header não aparece na nossa URL/URI, na verdade ele contém informações adicionais que são enviadas 'escondidas' no cabeçalho das requisiões. Esse tipo de parametro é ideal para informações de controle e segurança como tokens de acesso, controle da cachê etc.

primeiro fazemos a importação de Header:

from fastapi import Header

Agora adicionamos Header na nossa função de calculadora, definindo sempre o 'default' que é obrigatório: 

@app.get('/calculadora')
async def calcular(a: int = Query(default+None, gt=5), b: int = Query(default=None, gt=10), x_geek: str = Header(default=None), c: Optional [int] = None)
    soma: int = a + b
    if c:
        soma = soma + c

    print(f'X-GEEK: {x_geek})

    return {"resultado": soma}

Lembrando que este trexo de código é apenas um exemplo de aplicação e utilização. 

*Prática - Injeção de Dependências*

As Dependências são arquivos ou trexos do código, do qual a nossa API depende para funcionar corretamente. Para injetarmos essas dependencias no código, utilizamos a injeção de dependências.

Nesta aula, a primeira coisa que fazemos são as importações e a criação de uma função para simular a conexão com um Banco de Dados.

from fastapi import Depends
from time import sleep

O trexo de código abaixo foi feito logo abaixo das importações do código, e antes da inicialização de 'app com FastAPI'.

def fake_db():
    try:
        print('Abrindo conexão com banco de dados...')
        sleep(1)
    finally:
        print('Fechando conexão com banco de dados...')
        sleep(1)

Agora colocamos essa dependência em todas as funções com métodos em nosso código. Ex:

from typing import Any

@app.get('/cursos')
async def get_cursos(db: Any = Depends(fake_db)):
    return cursos

*colocamos o trecho 'db: Any = Depends(fake_db)'.

Isso faz com que nosso código teste a conexão com as dependências antes de executar a função.

*Prática - Revisando os Docs*
Nesta aula aprendemos a customizar a nossa documentação gerada automáticamente pela FastAPI. 

Criamos descrições e explicações melhores na instancia de FastAPI e no método GET. 

app = FastAPI(
    title='API de Curso para aprendizado!',
    version='0.0.1',
    description='Uma API para estudo do FastAPI'
    )

@app.get('/cursos', 
    description='Retorna todos os cursos ou uma lista vazia.', 
    summary='Retorna todos os cursos.', 
    response_model=List[Curso],
    response_description='Cursos encontrados com sucesso!')
async def get_cursos(db: Any = Depends(fake_db)):
    return cursos

Agora no método POST:

@app.post('/cursos', status_code=status.HTTP_201_CREATED, response_model=Curso)
async def post_curso(curso: Curso, db: Any = Depends(fake_db)):
    next_id: int = len(next_id) + 1
    cursos[next_id] = curso
    del curso.id
    return curso

Além disso, removemos a nossa variável 'cursos' do arquivo main e salvamos no arquivo 'models' como uma lista

Agora importamos a nossa lista mokada em models:

from models import cursos

Podemos personalizar e alterar as descrições de todo o código.

*Prática - Definindo Rotas*
Vamos aprender a organizar a nossa API. Pra isso, criamos outra pasta, dentro dela criamos:
Pratica_02_v2>routes>
                curso_router.py/usuario_router.py
    main.py/requirements.txt

Não precisamos criar um novo ambiente virtual, podemos continuar usando o mesmo do outro projeto.

No arquivo curso_router.py:

from fastapi import APIRouter

router = APIRouter()

@router.get('/api/v2/cursos')
async def get_cursos():
    return {'info': 'Todos os cursos'}

usuaruio_router.py:

from fastapi import APIRouter

router = APIRouter()

@router.get('/api/v2/usuarios')
async def get_usuarios():
    return {'info': 'Todos os usuarios'}

main.py:

from fastapi import FastAPI

from routes import curso_router
from routes import usuario_router

app = FastAPI
app.include_router(curso_router.router, tags=['cursos']) //essa tag serve para identificarmos a rota de cada um na documentação ao invés de ficar escrito 'default'
app.include_router(usuario_router.router, tags=['usuarios'])

if __name__ == '__main__':
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)

*Prática - Validação Customizada Pydantic*
*Voltando na Prática_2_pt1

Modificando o POST:

@app.post('/cursos', status_code=status.HTTP_201_CREATED)
-> async def post_curso(curso: Curso):
    next_id: int = len(next_id) + 1
    -> curso.id = next_id
    -> cursos.append(curso)
    return curso

E agora? Como fazer uma validação no nosso POST?

No arquivo 'models.py':

from pydantic import BaseModel, validator

agora, dentro da classe Curso adicionamos em baixo de tudo:

#pra cada atributo criamos uma função e dentro dessa função fazemos todas as validações necessárias com os 'if'.

@validator('titulo')
def validar_titulo(cls, value: str):
    palavras = value.split(' ')
    if len(palavras) < 3:
        raise ValueError('O título deve ter pelo menos 3 palavras.')

    if value.islower():
        raise ValueError('O título deve ser em maiúsculo')

        return value

**Fazer a validação com aulas e horas: aulas mais de 12 e horas mais de 10**