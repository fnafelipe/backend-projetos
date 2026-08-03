from menus.admin.sistema.sub_sistema.carregar_sistema import carregar_sistema
from menus.admin.sistema.sub_sistema.estatisticas import estatisticas
from menus.admin.sistema.sub_sistema.salvar_sistema import salvar_sistema
from utils.auxiliares import escolher, limpar


def pagina_menu_sistema():
    '''Exibe a pagina do menu de sistema'''

    limpar()
    print("====== SISTEMA ======")
    print("[1] Salvar sistema")
    print("[2] Carregar sistema")
    print("[3] Estatisticas")
    print("[0] Voltar")
    print("==================================")

def menu_sistema(sistema):

    while True:
        pagina_menu_sistema()
        resp = escolher(3)

        match resp:
            case 1: salvar_sistema(sistema)
            case 2: carregar_sistema(sistema)
            case 3: estatisticas(sistema)
            case 0: return