from fastapi import APIRouter

router = APIRouter()

@router.get('/api/v2/cursos')
async def get_cursos():
    return {'info': 'Todos os cursos'}