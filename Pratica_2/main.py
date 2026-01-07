from fastapi import FastAPI

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

if __name__ == '__main__':
    import uvicorn

    uvicorn.run("main.app", host="0.0.0.0", port=8000, debug=True)