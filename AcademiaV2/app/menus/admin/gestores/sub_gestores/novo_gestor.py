
from models.gestor import Gestor
from utils.auxiliares import limpar


def pagina_novo_gestor():
    '''Exibe a página de cadastro de gestor.'''

    limpar()
    print("====== NOVO GESTOR ======")
    print("Digite os dados novos:")
    print("============================")

def novo_gestor(sistema):
    '''Exibe o menu de cadastro de gestores, e realiza um cadastro'''

    while True:
        pagina_novo_gestor()

        try:
            codigo = int(input("Codigo: "))
            gestor = sistema.buscar_gestor(codigo)

            if gestor:
                raise ValueError("Gestor já cadastrado!")

            nome = input("Nome: ")
            idade = int(input("Idade: "))
            sexo = input("Sexo: ")
            cargo = input("Cargo: ")

            gestor = Gestor(codigo, nome, idade, sexo, cargo)
            sistema.gestores.append(gestor)
            print("Gestor cadastrado.")
            input("Pressione enter para voltar...")
            return

        except Exception as e:  # noqa: BLE001
            print(f"Erro: {e}")
            input("Pressione enter para tentar novamente...")
            continue