
from utils.auxiliares import escolher, limpar


def pagina_perfil_aluno(aluno):

    limpar()
    print("====== PERFIL DO ALUNO ======")
    print(f"Nome: {aluno.nome.title()}")
    print(f"Idade: {aluno.idade} anos")
    print(f"Sexo: {aluno.sexo.title()}")
    print(f"Peso: {aluno.peso} kg")
    print(f"Altura: {aluno.altura} m")
    print("=============================")
    print("[1] Atualizar peso")
    print("[2] Atualizar altura")
    print("[0] Voltar")
    print("=============================")

def perfil_aluno(aluno):

    while True:
        pagina_perfil_aluno()
        resp = escolher(2)
        match resp:
            case 1: atualizar_peso(aluno)
            case 2: atualizar_altura(aluno)
            case 0: return

def atualizar_peso(aluno):
    pass

def atualizar_altura(aluno):
    pass