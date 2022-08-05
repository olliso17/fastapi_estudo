
from imp import reload
from fastapi import FastAPI

app = FastAPI()


cursos = {
    1: {
        "titulo": "Programação para leigos",
        "aulas": 112,
        "horas": 58
    },
    2: {
        "titulo": "Algoritmo e lógica de Programação",
        "aulas": 58,
        "horas": 67
    }
}


@app.get('/cursos')
async def get_cursos():
    return cursos


@app.get('/curso/{curso_id}')
async def get_curso(curso_id: int):
    curso = cursos[curso_id]
    curso.update({'id': curso_id})

    return curso


if __name__ == '__main__':
    import uvicorn

    uvicorn.run('main:app', host='0.0.0.0', port=8000, debug=True, reload=True)

""" uvicorn main:app --port 8086  #para executar a porta"""