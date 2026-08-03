
from utils.auxiliares import limpar


def pagina_buscar_professor():
    '''Exibe a pagina do menu de busca de professores'''

    limpar()
    print("====== BUSCAR PROFESSOR ======")
    print("Digite o cref:")
    print("==========================")

def buscar_professor(sistema):
    '''Exibe o menu de busca de professores, e consulta as informações'''

    while True:
        pagina_buscar_professor()

        try:
            cref = input("Cref: ")
            professor = sistema.buscar_professor(cref)

            if not professor:
                raise ValueError("Professor não encontrado!")

            print("Professor encontrado.")
            print()
            print("Dados:")
            print(f"Nome: {professor.nome}")
            print(f"Idade: {professor.idade} anos")
            print(f"Sexo: {(professor.sexo).capitalize()}")
            print(f"Especialidade: {(professor.especialidade).capitalize()}")

            input("Pressione enter para voltar...")
            return

        except Exception as e:  # noqa: BLE001
            print(f"Erro: {e}")
            input("Pressione enter para tentar novamente...")
            continue