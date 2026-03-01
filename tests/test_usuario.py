import pytest
from app.services.usuario_service import UsuarioService
 
 
def test_crear_usuario_valido():
    service = UsuarioService()
    service.crear_usuario("Max")
 
    usuarios = service.obtener_usuarios()
    assert len(usuarios) == 1
    assert usuarios[0].nombre == "Max"
 
 
def test_crear_usuario_invalido():
    service = UsuarioService()
 
    with pytest.raises(ValueError):
        service.crear_usuario("")