

from menus.admin.gestores.sub_gestores.buscar_gestor import buscar_gestor
from menus.admin.gestores.sub_gestores.editar_gestor import editar_gestor
from menus.admin.gestores.sub_gestores.excluir_gestor import excluir_gestor
from menus.admin.gestores.sub_gestores.novo_gestor import novo_gestor
from utils.auxiliares import escolher, limpar


def pagina_menu_gestores():
    '''Exibe a pagina do menu de gestores'''

    limpar()
    print("====== AREA DOS GESTORES ======")
    print("[1] Novo gestor")
    print("[2] Buscar gestor")
    print("[3] Editar gestor")
    print("[4] Remover gestor")
    print("[0] Voltar")
    print("==================================")

def menu_gestores(sistema):
    '''Exibe o menu de gestores do sistema, permitindo ao usuário acessar informações sobre gestores.'''
    
    while True:
        pagina_menu_gestores()
        resp = escolher(4)
        match resp:
            case 1: novo_gestor(sistema)
            case 2: buscar_gestor(sistema)
            case 3: editar_gestor(sistema)
            case 4: excluir_gestor(sistema)
            case 0: return
