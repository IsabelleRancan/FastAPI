from fastapi import FastAPI
from fastapi import HTTPException
from fastapi import status
from fastapi import Response
from models import Curso

app = FastAPI()

cursos = {
    1: {
        "titulo" : "aula 1",
        "aulas" : 10,
        "horas" : 58
    },
    2: {
        "titulo" : "aula 2",
        "aulas" : 12,
        "horas" : 40
    }
}

@app.get('/cursos')
async def get_cursos():
    return cursos

@app.get('/cursos/{curso_id}')
async def get_curso(curso_id : int = Path(default=None, title='ID do curso', description='Deve ser entre 1 e 2', gt=0, lt=3)):
    try: 
        curso = cursos[curso_id]
        return curso
    except KeyError: 
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Curso não encontrado.')
    
@app.post('/cursos', status_code=status.HTTP_201_CREATED)
async def post_curso(curso: Curso):
    next_id: int = len(next_id) + 1
    cursos[next_id] = curso
    del curso.id
    return curso

@app.put('/cursos/{curso_id}')
async def put_curso(curso_id: int, curso: Curso):
    if curso_id in cursos:
        cursos[curso_id] = curso
        del curso.id 
        return cursos
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Não existe um curso com o id {curso_id}')
    
@app.delete('/cursos/{curso_id}')
async def delete_curso(curso_id: int):
    if curso_id in cursos:
        del cursos[curso_id]
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Não existe um curso com o id {curso_id}')

if __name__ == '__main__':
    import uvicorn

    uvicorn.run("main.app", host="0.0.0.0", port=8000, debug=True, reload=True)