from menus.usuario.menu_usuario import menu_usuario
from menus.admin.menu_admin import menu_admin
from utils.auxiliares import escolher, limpar


def pagina_menu_principal():
    limpar()
    print("====== MENU PRINCIPAL ======")
    print("[1] Area do usuário")
    print("[2] Area da administração")
    print("[0] Sair")
    print("============================")  

def menu_principal(sistema):
    '''Menu principal do sistema, permitindo ao usuário acessar diferentes áreas do sistema, como recepção, treinos, equipe e administração.'''

    while True:
        limpar()
        pagina_menu_principal()
        resp = escolher(2)
        match resp:
            case 1: menu_usuario(sistema)
            case 2: menu_admin(sistema)
            case 0: return