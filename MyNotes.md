**Acabar de formatar esse arquivo com todas as minhas anotações**

# 📘 Anotações --- FastAPI

## Section 2 --- Introdução ao FastAPI

### Ambiente

``` bash
python -m venv venv
venv\Scripts\activate
pip install fastapi gunicorn uvicorn
pip freeze > requirements.txt
```

Versões: - fastapi 0.75.2 - uvicorn 0.17.6

### main.py

``` python
from fastapi import FastAPI
app = FastAPI()

@app.get("/")
async def raiz():
    return {"msg": "FastAPI"}
```

### Executando

``` bash
uvicorn main:app --reload
```

Docs: - /docs - /redoc

## Section 3 --- Conceitos

### GET

``` python
@app.get("/cursos")
async def get_cursos():
    return cursos
```

``` python
@app.get("/cursos/{curso_id}")
async def get_curso(curso_id:int):
    curso = cursos[curso_id]
    curso.update({"id":curso_id})
    return curso
```

### Exceções

``` python
from fastapi import HTTPException, status

@app.get("/cursos/{curso_id}")
async def get_curso(curso_id:int):
    try:
        return cursos[curso_id]
    except KeyError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Curso não encontrado")
```

### POST

``` python
from models import Curso

@app.post("/cursos", status_code=status.HTTP_201_CREATED)
async def post_curso(curso:Curso):
    next_id = len(cursos)+1
    cursos[next_id] = curso
    del curso.id
    return curso
```

JSON:

``` json
{"titulo":"Aula X","aulas":54,"horas":12}
```

### PUT

``` python
@app.put("/cursos/{curso_id}")
async def put_curso(curso_id:int, curso:Curso):
    if curso_id in cursos:
        cursos[curso_id] = curso
        del curso.id
        return curso
    else:
        raise HTTPException(status_code=404, detail="Não encontrado")
```

### DELETE

``` python
from fastapi import Response

@app.delete("/cursos/{curso_id}")
async def delete_curso(curso_id:int):
    if curso_id in cursos:
        del cursos[curso_id]
        return Response(status_code=204)
    else:
        raise HTTPException(status_code=404, detail="Não encontrado")
```
