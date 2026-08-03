

def pagina_historicos_aluno(aluno):

    print("====== HISTORICOS DO ALUNO ======")
    print(f"Peso: {aluno.historico_peso}")
    print(f"Altura:{aluno.historico_altura}")
    print("==============================")

def historicos_aluno(aluno):

    pagina_historicos_aluno()
    input("Pressione enter para voltar...")