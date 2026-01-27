from fastapi import APIRouter

router = APIRouter()

@router.get('/api/v2/usuarios')
async def get_usuarios():
    return {'info': 'Todos os usuarios'}