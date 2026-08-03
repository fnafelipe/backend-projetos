
from models.aluno import Aluno
from utils.auxiliares import limpar


def pagina_novo_aluno():
    '''Exibe a página de cadastro de aluno.'''

    limpar()
    print("====== NOVO ALUNO ======")
    print("Digite os dados novos:")
    print("========================")

def novo_aluno(sistema):
    '''Exibe o menu de cadastro de alunos, e realiza um cadastro'''

    while True:
        pagina_novo_aluno()

        try:
            matricula = int(input("Matricula: "))
            aluno = sistema.buscar_aluno(matricula)

            if aluno:
                raise ValueError("Aluno já cadastrado!")

            nome = input("Nome: ")
            idade = int(input("Idade: "))
            sexo = input("Sexo: ")
            peso = float(input("Peso: "))
            altura = float(input("Altura: "))

            aluno = Aluno(matricula, nome, idade, sexo, peso, altura)
            sistema.alunos.append(aluno)
            print("Aluno cadastrado.")
            input("Pressione enter para voltar...")
            return

        except Exception as e:  # noqa: BLE001
            print(f"Erro: {e}")
            input("Pressione enter para tentar novamente...")
            continue