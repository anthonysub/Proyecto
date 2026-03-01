from app.services.usuario_service import UsuarioService

def run():
    service = UsuarioService()
    service.crear_usuario("Max Benito")
    print(service.obtener_usuarios())

if __name__ == "__main__":
    run()