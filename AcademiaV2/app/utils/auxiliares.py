import os


def confirmar(pergunta):
    print()
    while True:
        resp = input(f'{pergunta} S/N ').upper()
        if resp == 'S': return True
        elif resp == 'N': return False
        else: informar('Resposta inválida!')

def escolher(num):
    print()
    while True:
        try:
            escolha = int(input('Qual ação deseja realizar? '))
            if 0 <= escolha <= num:
                return escolha
            else:
                raise ValueError
        except ValueError:
            informar("Resposta inválida!")

def limpar():
    os.system('cls' if os.name == 'nt' else 'clear')

def voltar_uma():
    print("\033[A\033[K", end="")

def voltar_duas():
    print("\033[A\033[K\033[A", end="")

def informar(mensagem_erro):
    '''Exibe uma mensagem de erro em cima da resposta do usuário'''

    voltar_duas()
    print(mensagem_erro)
