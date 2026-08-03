
from utils.auxiliares import limpar


def pagina_buscar_aluno():
    '''Exibe a pagina do menu de busca de alunos'''

    limpar()
    print("====== BUSCAR ALUNO ======")
    print("Digite a matricula:")
    print("==========================")

def buscar_aluno(sistema):
    '''Exibe o menu de busca de alunos, e consulta as informações'''

    while True:
        pagina_buscar_aluno()

        try:
            matricula = int(input("Matricula: "))
            aluno = sistema.buscar_aluno(matricula)

            if not aluno:
                raise ValueError("Aluno não encontrado!")

            print("Aluno encontrado.")
            print()
            print("Dados:")
            print(f"Nome: {aluno.nome}")
            print(f"Idade: {aluno.idade} anos")
            print(f"Sexo: {(aluno.sexo).capitalize()}")
            print(f"Peso: {aluno.peso} kg")
            print(f"Altura: {aluno.altura} m")

            input("Pressione enter para voltar...")
            return

        except Exception as e:  # noqa: BLE001
            print(f"Erro: {e}")
            input("Pressione enter para tentar novamente...")
            continue