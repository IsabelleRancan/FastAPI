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
3 - Criamos o arquivo main e criamos um dicionário de cursos 
4 - Criamos a entrada no código para ele recarregar de forma automática

-> Resolvendo o problema de importação que surgiu: as importações não estavam funcionando no código. 
A solução encontrada é porque o interpretador estava errado então fizemos o seguinte: 
ctrl + shift + P;
digitar 'python'
selecionar a opção de 'escolher interpretador'
selecionar o interpretador instalado no ambiente virtual