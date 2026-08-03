from menus.admin.professores.sub_professores.buscar_professor import buscar_professor
from menus.admin.professores.sub_professores.editar_professor import editar_professor
from menus.admin.professores.sub_professores.excluir_professor import excluir_professor
from menus.admin.professores.sub_professores.novo_professor import novo_professor
from utils.auxiliares import escolher, limpar


def pagina_menu_professores():
    '''Exibe a pagina do menu de professores.'''

    limpar()
    print("====== MENU DE PROFESSORES ======")
    print("[1] Novo professor")
    print("[2] Buscar professor")
    print("[3] Editar professor")
    print("[4] Excluir professor")
    print("[0] Voltar")
    print("=================================")

def menu_professores(sistema):
    '''Exibe o menu de professores do sistema, permitindo ao usuário acessar diferentes funcionalidades relacionadas aos professores.'''

    while True:
        pagina_menu_professores()
        resp = escolher(4)
        match resp:
            case 1: novo_professor(sistema)
            case 2: buscar_professor(sistema)
            case 3: editar_professor(sistema)
            case 4: excluir_professor(sistema)
            case 0: return

