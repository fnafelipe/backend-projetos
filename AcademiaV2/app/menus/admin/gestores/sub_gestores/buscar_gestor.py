
from utils.auxiliares import limpar


def pagina_buscar_gestor():
    '''Exibe a pagina do menu de busca de gestores'''

    limpar()
    print("====== BUSCAR GESTOR ======")
    print("Digite o codigo:")
    print("==========================")

def buscar_gestor(sistema):
    '''Exibe o menu de busca de gestores, e consulta as informações'''

    while True:
        pagina_buscar_gestor()

        try:
            codigo = int(input("Codigo: "))
            gestor = sistema.buscar_gestor(codigo)

            if not gestor:
                raise ValueError("Gestor não encontrado!")

            print("Gestor encontrado.")
            print()
            print("Dados:")
            print(f"Nome: {gestor.nome}")
            print(f"Idade: {gestor.idade} anos")
            print(f"Sexo: {(gestor.sexo).capitalize()}")
            print(f"Cargo: {(gestor.cargo).capitalize()}")

            input("Pressione enter para voltar...")
            return

        except Exception as e:  # noqa: BLE001
            print(f"Erro: {e}")
            input("Pressione enter para tentar novamente...")
            continue