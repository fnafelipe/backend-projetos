
from menus.menu_principal import menu_principal


def iniciar(sistema):
    '''Inicia o programa, exibindo a tela de boas-vindas e chamando o menu principal.'''
    print("====== INICIANDO O PROGRAMA ======")
    menu_principal(sistema)
    encerrar(sistema)

def encerrar(sistema):
    '''Encerra o programa, exibindo a tela de encerramento e salvando os dados do sistema.'''
    print("====== ENCERRANDO O PROGRAMA ======")