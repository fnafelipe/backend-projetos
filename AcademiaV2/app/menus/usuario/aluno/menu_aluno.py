
from menus.usuario.aluno.sub_aluno.historicos_aluno import historicos_aluno
from menus.usuario.aluno.sub_aluno.perfil_aluno import perfil_aluno
from menus.usuario.aluno.sub_aluno.treinos_aluno import treinos_aluno
from utils.auxiliares import escolher, limpar


def pagina_menu_aluno(nome):

    limpar()
    print(f"====== BEM VINDO {nome.upper()}! ======")
    print("[1] Meu perfil")
    print("[2] Meus treinos")
    print("[3] Históricos")
    print("[0] Sair")
    print("============================")  

def menu_aluno(aluno):

    while True:
        limpar()
        pagina_menu_aluno(aluno.nome)
        resp = escolher(3)
        match resp:
            case 1: perfil_aluno(aluno)
            case 2: treinos_aluno(aluno)
            case 3: historicos_aluno(aluno)
            case 0: return