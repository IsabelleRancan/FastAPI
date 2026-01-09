from fastapi import FastAPI
from fastapi import HTTPException
from fastapi import status

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
async def get_curso(curso_id : int):
    try: 
        curso = cursos[curso_id]
        return curso
    except KeyError: 
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Curso não encontrado.')

if __name__ == '__main__':
    import uvicorn

    uvicorn.run("main.app", host="0.0.0.0", port=8000, debug=True, reload=True)