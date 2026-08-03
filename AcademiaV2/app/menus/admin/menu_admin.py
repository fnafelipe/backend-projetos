from menus.admin.alunos.menu_alunos import menu_alunos
from menus.admin.gestores.menu_gestores import menu_gestores
from menus.admin.professores.menu_professores import menu_professores
from menus.admin.sistema.menu_sistema import menu_sistema
from utils.auxiliares import escolher, limpar


def pagina_menu_admin():
    '''Exibe a página do menu de administração'''

    limpar()
    print("====== AREA ADMINISTRATIVA ======")
    print("[1] Alunos")
    print("[2] Professores")
    print("[3] Gestores")
    print("[4] Sistema")
    print("[0] Voltar")
    print("===================================")

def menu_admin(sistema):
    '''Exibe o menu de administração do sistema, permitindo ao usuário salvar e carregar dados, bem como visualizar estatísticas.'''

    while True:
        limpar()
        pagina_menu_admin()
        resp = escolher(4)
        match resp:
            case 1: menu_alunos(sistema)
            case 2: menu_professores(sistema)
            case 3: menu_gestores(sistema)
            case 4: menu_sistema(sistema)
            case 0: return