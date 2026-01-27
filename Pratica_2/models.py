from typing import Optional

from pydantic import BaseModel, field_validator 

class Curso(BaseModel):
    id: Optional[int] = None
    titulo: str
    aulas: int
    horas: int

cursos = [
    Curso(id=1, titulo='Aula 1', aulas=42, horas=56),
    Curso(id=2, titulo='Aula 2', aulas=52, horas=66),
]

@field_validator('titulo')
def validar_titulo(cls, value: str):
    palavras = value.split(' ')
    if len(palavras) < 3:
        raise ValueError('O título deve ter pelo menos 3 palavras.')
    
    if value.islower():
        raise ValueError('O título deve ser em maiúsculo.')
    
    return value