from utils.auxiliares import confirmar, limpar


def pagina_excluir_professor():
    '''Exibe a pagina do menu de exclusão de professores.'''

    limpar()
    print("====== EXCLUIR PROFESSOR ======")
    print("Digite o cref:")
    print("==========================")

def excluir_professor(sistema):
    '''Exclui um professor do sistema.'''

    while True:
        pagina_excluir_professor()

        try:
            cref = input("Cref: ")
            professor = sistema.buscar_professor(cref)

            if not professor:
                raise ValueError("Professor não encontrado!")

            print("Professor encontrado.")
            print()
            print(f"Nome: {professor.nome}")

            if not confirmar("Deseja realmente excluir esse professor?"):
                raise Exception("Professor não excluído!")  # noqa: TRY002

            sistema.professores.remove(professor)
            print("Professor excluído.")
            input("Pressione enter para voltar...")
            return

        except Exception as e:  # noqa: BLE001
            print(f"Erro: {e}")
            input("Pressione enter para tentar novamente...")
            continue