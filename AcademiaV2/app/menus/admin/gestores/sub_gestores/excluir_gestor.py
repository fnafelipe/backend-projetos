from utils.auxiliares import confirmar, limpar


def pagina_excluir_gestor():
    '''Exibe a pagina do menu de exclusão de gestores.'''

    limpar()
    print("====== EXCLUIR GESTOR ======")
    print("Digite o codigo:")
    print("==========================")

def excluir_gestor(sistema):
    '''Exclui um gestor do sistema.'''

    while True:
        pagina_excluir_gestor()

        try:
            codigo = int(input("Codigo: "))
            gestor = sistema.buscar_gestor(codigo)

            if not gestor:
                raise ValueError("Gestor não encontrado!")

            print("Gestor encontrado.")
            print()
            print(f"Nome: {gestor.nome}")

            if not confirmar("Deseja realmente excluir esse gestor?"):
                raise Exception("Gestor não excluído!")  # noqa: TRY002

            sistema.gestores.remove(gestor)
            print("Gestor excluído.")
            input("Pressione enter para voltar...")
            return

        except Exception as e:  # noqa: BLE001
            print(f"Erro: {e}")
            input("Pressione enter para tentar novamente...")
            continue