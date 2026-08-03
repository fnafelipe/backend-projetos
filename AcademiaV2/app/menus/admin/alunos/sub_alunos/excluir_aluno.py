from utils.auxiliares import confirmar, limpar


def pagina_excluir_aluno():
    '''Exibe a pagina do menu de exclusão de alunos.'''

    limpar()
    print("====== EXCLUIR ALUNO ======")
    print("Digite a matricula:")
    print("==========================")

def excluir_aluno(sistema):
    '''Exclui um aluno do sistema.'''

    while True:
        pagina_excluir_aluno()

        try:
            matricula = int(input("Matricula: "))
            aluno = sistema.buscar_aluno(matricula)

            if not aluno:
                raise ValueError("Aluno não encontrado!")

            print("Aluno encontrado.")
            print()
            print(f"Nome: {aluno.nome}")

            if not confirmar("Deseja realmente excluir esse aluno?"):
                raise Exception("Aluno não excluído!")  # noqa: TRY002

            sistema.alunos.remove(aluno)
            print("Aluno excluído.")
            input("Pressione enter para voltar...")
            return

        except Exception as e:  # noqa: BLE001
            print(f"Erro: {e}")
            input("Pressione enter para tentar novamente...")
            continue