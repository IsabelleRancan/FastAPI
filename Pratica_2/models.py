from typing import Optional

from pydantic import BaseModel 

class Curso(BaseModel):
    id: Optional[int] = None
    titulo: str
    aulas: int
    horas: int

cursos = [
    Curso(id=1, titulo='Aula 1', aulas=42, horas=56),
    Curso(id=2, titulo='Aula 2', aulas=52, horas=66),
]