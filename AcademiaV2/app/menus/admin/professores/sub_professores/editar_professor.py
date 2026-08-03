from utils.auxiliares import limpar


def pagina_editar_professor():
    '''Exibe a pagina do menu de edição de professores'''

    limpar()
    print("====== EDITAR PROFESSOR ======")
    print("Digite o cref:")
    print("==========================")

def editar_professor(sistema):
    '''Edita informações de um professor já existente.'''

    while True:
        pagina_editar_professor()

        try:
            cref = input("cref: ")
            professor = sistema.buscar_professor(cref)

            if not professor:
                raise ValueError("Professor não encontrado!")

            print("Professor encontrado.")
            print()
            print("Digite o dado novo ou vazio pra manter igual.")
            professor.nome = input(f"Nome ({professor.nome}): ").strip() or professor.nome
            idade = input(f"Idade ({professor.idade}): ").strip()
            professor.idade = int(idade) if idade else professor.idade
            professor.sexo = input(f"Sexo ({(professor.sexo).capitalize()}): ").strip() or professor.sexo
            professor.especialidade = input(f"Especialidade: ({(professor.especialidade).capitalize()}): ").strip() or professor.especialidade

            print("Professor editado.")
            input("Pressione enter para voltar...")
            return

        except Exception as e:  # noqa: BLE001
            print(f"Erro: {e}")
            input("Pressione enter para tentar novamente...")
            continue