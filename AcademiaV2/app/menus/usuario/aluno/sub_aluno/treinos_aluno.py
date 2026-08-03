

def pagina_treinos_aluno(aluno):

    print("====== TREINOS DO ALUNO ======")
    print("Digite o nome de um treino:")
    print(f"[{i}] {treino}" for i, treino in enumerate(aluno.treinos))
    print("==============================")

def treinos_aluno(aluno):

    pagina_treinos_aluno()
    input("Pressione enter para voltar...")