
from menus.usuario.login_aluno import login_aluno
from menus.usuario.login_professor import login_professor
from utils.auxiliares import escolher, limpar


def pagina_menu_usuario():
    '''Exibe o menu de login dos usuarios.'''

    limpar()
    print("====== MENU USUARIO ======")
    print("[1] Login Aluno")
    print("[2] Login Professor")
    print("[0] Sair")
    print("============================")  

def menu_usuario(sistema):
    '''Menu de usuario do sistema.'''

    while True:
        limpar()
        pagina_menu_usuario()
        resp = escolher(2)
        match resp:
            case 1: login_aluno(sistema)
            case 2: login_professor(sistema)
            case 0: return