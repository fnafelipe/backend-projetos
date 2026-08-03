from utils.auxiliares import limpar


def pagina_editar_gestor():
    '''Exibe a pagina do menu de edição de gestores'''

    limpar()
    print("====== EDITAR GESTOR ======")
    print("Digite o codigo:")
    print("==========================")

def editar_gestor(sistema):
    '''Edita informações de um gestor já existente.'''

    while True:
        pagina_editar_gestor()

        try:
            codigo = int(input("Codigo: "))
            gestor = sistema.buscar_gestor(codigo)

            if not gestor:
                raise ValueError("Gestor não encontrado!")

            print("Gestor encontrado.")
            print()
            print("Digite o dado novo ou vazio pra manter igual.")
            gestor.nome = input(f"Nome ({gestor.nome}): ").strip() or gestor.nome
            idade = input(f"Idade ({gestor.idade}): ").strip()
            gestor.idade = int(idade) if idade else gestor.idade
            gestor.sexo = input(f"Sexo ({(gestor.sexo).capitalize()}): ").strip() or gestor.sexo
            gestor.cargo = input(f"Cargo: ({(gestor.cargo).capitalize()}): ").strip() or gestor.cargo

            print("Gestor editado.")
            input("Pressione enter para voltar...")
            return

        except Exception as e:  # noqa: BLE001
            print(f"Erro: {e}")
            input("Pressione enter para tentar novamente...")
            continue