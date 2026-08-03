
from models.professor import Professor
from utils.auxiliares import limpar


def pagina_novo_professor():
    '''Exibe a página de cadastro de professor.'''

    limpar()
    print("====== NOVO PROFESSOR ======")
    print("Digite os dados novos:")
    print("============================")

def novo_professor(sistema):
    '''Exibe o menu de cadastro de professores, e realiza um cadastro'''

    while True:
        pagina_novo_professor()

        try:
            cref = input("Cref: ")
            professor = sistema.buscar_professor(cref)

            if professor:
                raise ValueError("Professor já cadastrado!")

            nome = input("Nome: ")
            idade = int(input("Idade: "))
            sexo = input("Sexo: ")
            especialidade = input("Especialidade: ")

            professor = Professor(cref, nome, idade, sexo, especialidade)
            sistema.professores.append(professor)
            print("Professor cadastrado.")
            input("Pressione enter para voltar...")
            return

        except Exception as e:  # noqa: BLE001
            print(f"Erro: {e}")
            input("Pressione enter para tentar novamente...")
            continue