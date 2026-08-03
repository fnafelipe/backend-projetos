from menus.admin.alunos.sub_alunos.buscar_aluno import buscar_aluno
from menus.admin.alunos.sub_alunos.editar_aluno import editar_aluno
from menus.admin.alunos.sub_alunos.excluir_aluno import excluir_aluno
from menus.admin.alunos.sub_alunos.novo_aluno import novo_aluno
from utils.auxiliares import escolher, limpar


def pagina_menu_alunos():
    '''Exibe a pagina do menu de alunos.'''

    limpar()
    print("====== MENU DE ALUNOS ======")
    print("[1] Novo aluno")
    print("[2] Buscar aluno")
    print("[3] Editar aluno")
    print("[4] Excluir aluno")
    print("[0] Voltar")
    print("============================")

def menu_alunos(sistema):
    '''Exibe o menu de alunos do sistema, permitindo ao usuário acessar diferentes funcionalidades relacionadas aos alunos.'''

    while True:
        pagina_menu_alunos()
        resp = escolher(4)
        match resp:
            case 1: novo_aluno(sistema)
            case 2: buscar_aluno(sistema)
            case 3: editar_aluno(sistema)
            case 4: excluir_aluno(sistema)
            case 0: return

