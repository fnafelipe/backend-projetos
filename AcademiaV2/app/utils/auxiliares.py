
def confirmar(pergunta):
    while True:
        resp = input(f'{pergunta} S/N ').upper()
        if resp == 'S': return True
        elif resp == 'N': return False
        else: print('Resposta inválida!')
    