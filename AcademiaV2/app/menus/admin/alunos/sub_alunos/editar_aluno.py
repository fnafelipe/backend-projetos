from utils.auxiliares import limpar


def pagina_editar_aluno():
    '''Exibe a pagina do menu de edição de alunos'''

    limpar()
    print("====== EDITAR ALUNO ======")
    print("Digite a matricula:")
    print("==========================")

def editar_aluno(sistema):
    '''Edita informações de um aluno já existente.'''

    while True:
        pagina_editar_aluno()

        try:
            matricula = int(input("Matricula: "))
            aluno = sistema.buscar_aluno(matricula)

            if not aluno:
                raise ValueError("Aluno não encontrado!")

            print("Aluno encontrado.")
            print()
            print("Digite o dado novo ou vazio pra manter igual.")
            aluno.nome = input(f"Nome ({aluno.nome}): ").strip() or aluno.nome
            idade = input(f"Idade ({aluno.idade}): ").strip()
            aluno.idade = int(idade) if idade else aluno.idade
            aluno.sexo = input(f"Sexo ({(aluno.sexo).capitalize()}): ").strip() or aluno.sexo
            peso = input(f"Peso: ({aluno.peso}): ").strip()
            aluno.peso = float(peso) if peso else aluno.peso
            altura = input(f"Altura: ({aluno.altura}): ").strip()
            aluno.altura = float(altura) if altura else aluno.altura

            print("Aluno editado.")
            input("Pressione enter para voltar...")
            return

        except Exception as e:  # noqa: BLE001
            print(f"Erro: {e}")
            input("Pressione enter para tentar novamente...")
            continue