from typing import List, Optional
from fastapi import FastAPI
from fastapi import HTTPException
from fastapi import status

from models import Curso

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
    try:
        curso = cursos[curso_id]
        return curso
    except KeyError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Curso não encontrado.')


@app.post('/cursos', status_code=status.HTTP_201_CREATED)
async def post_curso(curso: Curso):
    next_id: int = len(curso) + 1
    del curso.id
    curso[next_id] = curso
    return curso


if __name__ == '__main__':
    import uvicorn

    uvicorn.run('main:app', host='0.0.0.0', port=8000, debug=True, reload=True)

""" uvicorn main:app --port 8086, ou com python main.py e substituir 0000 por localhost #para executar a porta"""