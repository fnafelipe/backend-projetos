
from menus.usuario.aluno import menu_aluno
from utils.auxiliares import limpar


def pagina_login_aluno():
    '''Exibe a pagina do menu de login de alunos'''

    limpar()
    print("====== LOGIN ALUNO ======")
    print("Digite sua matricula:")
    print("==========================")

def login_aluno(sistema):
    '''Exibe o menu de login de alunos, e consulta as informações'''

    while True:
        pagina_login_aluno()

        try:
            matricula = int(input("Matricula: "))
            aluno = sistema.buscar_aluno(matricula)

            if not aluno:
                raise ValueError("Aluno não encontrado!")

            print("Aluno encontrado.")

            input("Pressione enter para entrar...")

            menu_aluno(aluno)

        except Exception as e:  # noqa: BLE001
            print(f"Erro: {e}")
            input("Pressione enter para tentar novamente...")
            continue