import json, time, os
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.text import Text
from rich.align import Align
from rich.columns import Columns
from rich.prompt import Prompt
from rich import box
from rich.theme import Theme
from rich.rule import Rule

tema = Theme({'sucesso' : 'bold green',
             'erro' : 'blink red',
             'alerta' : 'italic yellow',
             'menus' : 'bold blue',
             'destaque' : 'bold white'})

console = Console(width=50, theme=tema)

def voltar():
    input_meio('Pressione enter para voltar')

def mostrar_linha():
    console.print(Rule(style='menus'))

def print_meio(prompt='', padrao='white'):
    console.print(prompt, justify='center', style=padrao)

def input_meio(prompt=''):
    resp = input(" " * ((50 - len(prompt)) // 2) + prompt)
    return resp

def voltar_uma_linha():
    print("\033[1A\033[2K\r", end="")

def voltar_duas_linhas():
    print("\033[1A\033[2K\033[1A\033[2K\r", end="")

def carregar_tela():
    print_meio('Carregando. . .')
    time.sleep(2)
    os.system('cls')

def login(usuarios, biblioteca_exercicios):
    carregar_tela()
    mostrar_pagina('LOG IN')
    email = confirmar_email_login(usuarios)
    senha = confirmar_senha_login(email, usuarios)
    if senha:
        usuario = usuarios[email]
        menu_principal(usuario, usuarios, biblioteca_exercicios)
        return
    
def confirmar_senha_login(email, usuarios):
    print('')
    while True:
        mensagem_erro = ''
        senha = validar_senha()
        confirma = input_meio("Confirme a senha: ")
        if senha != confirma:
            mensagem_erro = 'Senha não confirmada!'
        elif usuarios[email]['senha'] != int(senha):
            mensagem_erro = 'SENHA INCORRETA!'
        if mensagem_erro:
            voltar_duas_linhas()
            voltar_uma_linha()
            print_meio(mensagem_erro, 'erro')
            continue
        voltar_duas_linhas()
        voltar_uma_linha()
        print_meio(f'Senha: {senha}', 'destaque')
        print_meio('Senha correta.', 'sucesso')
        return True

def confirmar_email_login(usuarios):
    print('')
    while True:
        mensagem_erro = ''
        email = validar_email()
        if email not in usuarios.keys():
            mensagem_erro = 'EMAIL NÃO ENCONTRADO!'
        if mensagem_erro:
            voltar_duas_linhas()
            print_meio(mensagem_erro, 'erro')
            continue
        voltar_duas_linhas()
        print_meio(f'Email: {email}', 'destaque')
        print_meio(f'Email encontrado.', 'sucesso')
        return email
    
def mostrar_pagina(pagina):
    console.print(Panel(Align.center('[bold white on blue]:weight_lifter:  ACADEMIA:running:[/]'), box=box.DOUBLE, style='menus'))
    console.print(pagina, style='destaque', end=' ', justify='center')
    mostrar_linha()

def signin(usuarios=None):
    carregar_tela()
    mostrar_pagina('SIGN IN')
    nome = validar_nome()
    idade = validar_idade()
    peso = validar_peso()
    altura = validar_altura()
    sexo = validar_sexo()
    email = confirmar_email_signin(usuarios)
    senha = confirmar_senha_signin()
    usuarios.update({email : {'email' : email,
                                'senha' : senha,
                                'nome' : nome,
                                'idade' : idade,
                                'peso' : [peso],
                                'altura' : [altura],
                                'sexo' : sexo,
                                'imc' : [],
                                'categoria' : None,
                                'treinos' : {}}})
    salvar_usuarios(usuarios)
    print_meio(f'Usuario {usuarios[email]['nome']} cadastrado.', 'sucesso')
    voltar()

def validar_nome():
    print('')
    while True:
        nome = input_meio('Digite o nome: ').strip().title()
        mensagem_erro = ""
        if nome == "":
            mensagem_erro = 'O nome não pode ser vazio!'
        elif not ((nome.replace(' ','')).isalpha()):
            mensagem_erro = 'O nome deve possuir apenas letras!'
        elif not esta_no_intervalo(len(nome), 4, 50):
            mensagem_erro = 'O nome deve possuir entre 4 e 50 letras!'
        if mensagem_erro:
            voltar_duas_linhas()
            print_meio(mensagem_erro, 'alerta')
            continue
        voltar_duas_linhas()
        print_meio(f'Nome: {nome}', 'destaque')
        return nome

def validar_idade():
    print('')
    while True:
        idade = input_meio('Digite a idade: ').strip()
        mensagem_erro = ""
        if not idade:
            mensagem_erro = 'A idade não pode ser vazia!'
        else:
            try:
                idade = int(idade)
                if not esta_no_intervalo(idade, 16, 120):
                    mensagem_erro = 'A idade deve estar entre 16 e 120 anos!'
            except ValueError:
                mensagem_erro = 'A idade é um número inteiro!'
        if mensagem_erro:
            voltar_duas_linhas()
            print_meio(mensagem_erro, 'alerta')
            continue
        voltar_duas_linhas()
        print_meio(f'Idade: {idade}', 'destaque')
        return idade

def validar_peso():
    print('')
    while True:
        peso = input_meio('Digite o peso: ').strip()
        mensagem_erro = ""
        if not peso:
            mensagem_erro = 'O peso não pode ser vazio!'
        else:
            try:
                peso = float(peso)
                if not esta_no_intervalo(peso, 30, 250):
                    mensagem_erro = 'O peso deve estar entre 30 e 250 kilos!'
            except ValueError:
                mensagem_erro = 'O peso é um número decimal com apenas 1 ponto!'
        if mensagem_erro:
            voltar_duas_linhas()
            print_meio(mensagem_erro, 'alerta')
            continue
        voltar_duas_linhas()
        print_meio(f'Peso: {peso} kg', 'destaque')
        return round(peso, 1)

def validar_altura():
    print('')
    while True:
        altura = input_meio('Digite a altura em cm: ').strip()
        mensagem_erro = ""
        if altura == '':
            mensagem_erro = 'A altura não pode ser vazia!'
        else:
            try:
                altura = int(altura)
                if not esta_no_intervalo(altura, 125, 225):
                    mensagem_erro = 'A altura deve estar entre 125 e 225 centimetros'
            except ValueError:
                mensagem_erro = 'A altura é um número em centímetros!'
        if mensagem_erro:
            voltar_duas_linhas()
            print_meio(mensagem_erro, 'alerta')
            continue
        voltar_duas_linhas()
        print_meio(f'Altura: {altura / 100} m', 'destaque')
        return altura / 100

def validar_sexo():
    SEXOS = ('masculino', 'feminino')
    print('')  
    while True:
        sexo = input_meio('Digite o sexo: ').strip().lower()
        mensagem_erro = ""
        if sexo not in SEXOS:
            mensagem_erro = 'O sexo deve ser Masculino ou Feminino!'
        if mensagem_erro:
            voltar_duas_linhas()
            print_meio(mensagem_erro, 'alerta')
            continue
        voltar_duas_linhas()
        print_meio(f'Sexo: {sexo.title()}', 'destaque')
        return sexo

def validar_email():
    dominios = ('@gmail.com', '@outlook.com', '@icloud.com', '@yahoo.com', '@proton.me', '@hotmail.com')
    while True:
        email = input_meio('Digite o email: ').strip().lower()
        mensagem_erro = ""
        if email == "":
            mensagem_erro = 'O email não pode ser vazio!'
        elif not esta_no_intervalo(len(email), 11, 60):
            mensagem_erro = 'O email deve possuir entre 11 e 60 caracteres!'
        elif not any(dominio in email for dominio in dominios):
            mensagem_erro = 'O email deve possuir uma formatação válida!'
        elif email[-4:] != '.com':
            mensagem_erro = 'O email deve terminar com ".com"'
        if mensagem_erro:
            voltar_duas_linhas()
            print_meio(mensagem_erro, 'alerta')
            continue
        return email

def validar_senha():
    while True:
        senha = input_meio('Digite a senha de 6 números: ').strip()
        mensagem_erro = ""
        if senha == '':
            mensagem_erro = 'A senha não pode ser vazia!'
        elif not (senha.isdigit()):
            mensagem_erro = 'A senha deve possuir somente números!'
        elif not (len(senha) == 6):
            mensagem_erro = 'A senha deve possuir exatamente 6 numeros!'
        if mensagem_erro:
            voltar_duas_linhas()
            print_meio(mensagem_erro, 'alerta')
            continue
        return senha

def confirmar_senha_signin():
    print('')
    while True:
        senha = validar_senha()
        confirma = input_meio('Confirme a senha: ').strip()
        mensagem_erro = ""
        if senha != confirma:
            mensagem_erro = 'Senha não confirmada!'
        if mensagem_erro:
            voltar_duas_linhas()
            voltar_uma_linha()
            print_meio(mensagem_erro, 'erro')
            continue
        voltar_duas_linhas()
        voltar_uma_linha()
        print_meio(f'Senha: {senha}', 'destaque')
        return int(senha)

def confirmar_email_signin(usuarios):
    print('')
    while True:
        email = validar_email()
        mensagem_erro = ""
        if email in usuarios.keys():
            mensagem_erro = 'O email ja foi registrado'
        if mensagem_erro:
            voltar_duas_linhas()
            print_meio(mensagem_erro, 'alerta')
            continue
        voltar_duas_linhas()
        print_meio(f'Email: {email}', 'destaque')
        return email
    
def esta_no_intervalo(num, ini, fim):
    return ini <= num <= fim

def encerrar():
    carregar_tela()
    mostrar_pagina('ENCERRAR')
    print_meio('Obrigado por usar.', 'sucesso')
    print_meio('Encerrando programa...')
    time.sleep(2)

def carregar_dados():
    carregar_tela()
    usuarios = carregar_usuarios()
    biblioteca_exercicios = carregar_exercicios()
    print(usuarios)
    print(biblioteca_exercicios)
    menu_entrada(usuarios, biblioteca_exercicios)

def menu_entrada(usuarios, biblioteca_exercicios):
    while True:
        pagina_menu_entrada()
        resp = validar_resposta(3)
        if resp == '1': login(usuarios, biblioteca_exercicios)
        elif resp == '2': signin(usuarios)
        elif resp == '3': break
    encerrar()

def validar_resposta(fim):
    while True:
        resp = input_meio('Qual ação deseja realizar?')
        opcoes = [str(opcao) for opcao in range(1, fim+1)]
        if resp not in opcoes:
            resposta_invalida()
            continue
        return resp

def resposta_invalida():
    voltar_duas_linhas()
    print_meio('RESPOSTA INVÁLIDA!', 'erro')
    
def pagina_menu_entrada():
    carregar_tela()
    mostrar_pagina('MENU DE ENTRADA')
    opcoes = [
        ("1", "Log in"),
        ("2", "Sign in"),
        ("3", "Encerrar")
    ]
    for chave, desc in opcoes:
        console.print(Align.center(f"[bold bright_magenta][{chave}][/] {desc:<10}"))
    console.print(Rule(style='menus'))
    print('')

def criar_arquivo(nome_arquivo):
    arquivo_novo = open(nome_arquivo, 'x', encoding='utf-8')
    arquivo_novo.close()
    print(f'Arquivo {nome_arquivo[6:]} criado com sucesso.')

def carregar_usuarios():
    try:
        with open('Semana02-Organização/Projeto/usuarios.json', 'r', encoding='utf-8') as arquivo:
            usuarios = json.load(arquivo)
            print('Usuários Carregados.')
            return usuarios
    except FileNotFoundError:
        print('Arquivo de usuarios não encontrado!')
        criar_arquivo('Projeto/usuarios.json')
        return {}
    except json.JSONDecodeError:
        print('Arquivo de usuarios vazio ou corrompido!')
        return {}

def carregar_exercicios():
    try:
        with open('Semana02-Organização/Projeto/exercicios.json', 'r', encoding='utf-8') as arquivo:
            biblioteca_exercicios = json.load(arquivo)
            print('Exercicios carregados.')
            return biblioteca_exercicios
    except FileNotFoundError:
        print('Arquivo de exercicios não encontrado')
        criar_arquivo('Projeto/exercicios.json')
        return {}
    except json.JSONDecodeError:
        print('Arquivo de exercicios vazio ou corrompido!')
        return {}

def salvar_usuarios(usuarios):
    with open('Projeto/usuarios.json', 'w', encoding='utf-8') as arquivo:
        json.dump(usuarios, arquivo, indent=4, ensure_ascii=False)
        return

def salvar_exercicios(exercicios):
    with open('Projeto/exercicios.json', 'w', encoding='utf-8') as arquivo:
        json.dump(exercicios, arquivo, indent=4, ensure_ascii=False)
        return

def pagina_perfil(usuario):
    carregar_tela()
    mostrar_pagina(f'PERFIL DE {usuario['nome'].upper()}')
    informações = [
        f'Email: {usuario['email']}',
        f'Senha: {usuario['senha']}',
        f'Idade: {usuario['idade']}',
        f'Peso: {usuario['peso'][0]}',
        f'Altura: {usuario['altura'][0]}',
        f'Sexo: {usuario['sexo']}'
    ]
    imc = usuario['imc'][0] if usuario['imc'] else 'Indefinido'
    categoria = usuario['categoria'] if usuario['categoria'] else 'Indefinido'
    opcoes = [
        ('1', 'Editar nome'),
        ('2', 'Editar peso'),
        ('3', 'Editar altura'),
        ('4', 'Voltar')
    ]
    for informacao in informações:
        console.print(Align.center(f"[destaque]{informacao:<23}[/]"))
    console.print(Align.center(f'[destaque]IMC: {imc:<18}[/]'))
    console.print(Align.center(f'[destaque]Categoria: {categoria:<13}[/]'))
    mostrar_linha()
    for chave, desc in opcoes:
        console.print(Align.center(f"[bold bright_magenta][{chave}][/] [destaque]{desc:<13}[/]"))
    
    console.print(Rule(style='menus'))
    print('')

def funcao_teste():
    print('Teste git')

def perfil(usuario, usuarios):
    while True:
        pagina_perfil(usuario)
        resp = validar_resposta(4)
        if resp == '1': editar_nome(usuario, usuarios)
        elif resp == '2': editar_peso(usuario, usuarios)
        elif resp == '3': editar_altura(usuario, usuarios)
        elif resp == '4': return

def editar_peso(usuario, usuarios):
    carregar_tela()
    mostrar_pagina('EDITAR PESO')
    print_meio(f'Peso atual: {usuario['peso'][0]}', 'destaque')
    peso_novo = confirmar_edicao_peso()
    atualiza_peso(peso_novo, usuario)
    print_meio('Peso atualizado.', 'sucesso')
    mostrar_linha()
    salvar_usuarios(usuarios)
    input_meio('Digite enter para voltar ')

def confirmar_edicao_peso():
    while True:
        peso_novo = validar_peso()
        voltar_uma_linha()
        print_meio(f'Peso novo: {peso_novo} kg', 'destaque')
        resp = input_meio('Deseja confirmar o peso novo? S/N').upper()
        if resp == 'S':
            voltar_uma_linha()
            return peso_novo
        voltar_duas_linhas()

def atualiza_peso(peso_novo, usuario):
    historico_peso = usuario['peso'].copy()
    historico_peso.insert(0, peso_novo)
    usuario.update({'peso' : historico_peso})

def editar_altura(usuario, usuarios):
    carregar_tela()
    mostrar_pagina('EDITAR ALTURA')
    print_meio(f'Altura atual: {usuario['altura'][0]}', 'destaque')
    altura_nova = confirmar_edicao_altura()
    atualiza_altura(altura_nova, usuario)
    salvar_usuarios(usuarios)
    print_meio('Altura atualizado.', 'sucesso')
    mostrar_linha()
    input_meio('Digite enter para voltar ')

def confirmar_edicao_altura():
    while True:
        altura_nova = validar_altura()
        voltar_uma_linha()
        print_meio(f'Altura nova: {altura_nova} m', 'destaque')
        resp = input_meio('Deseja confirmar a altura nova? S/N').upper()
        if resp == 'S':
            voltar_uma_linha()
            return altura_nova
        voltar_duas_linhas()

def atualiza_altura(altura_nova, usuario):
    historico_altura = usuario['altura'].copy()
    historico_altura.insert(0, altura_nova)
    usuario.update({'altura' : historico_altura})

def editar_nome(usuario, usuarios):
    carregar_tela()
    mostrar_pagina('EDITAR NOME')
    print_meio(f'Nome atual: {usuario['nome']}', 'destaque')
    nome_novo = confirmar_edicao_nome()
    usuario.update({'nome' : nome_novo})
    salvar_usuarios(usuarios)
    print_meio('Nome atualizado.', 'sucesso')
    mostrar_linha()
    input_meio('Digite enter para voltar ')

def confirmar_edicao_nome():
    while True:
        nome_novo = validar_nome()
        voltar_uma_linha()
        print_meio(f'Nome novo: {nome_novo}', 'destaque')
        resp = input_meio('Deseja confirmar o nome novo? S/N').upper()
        if resp == 'S':
            voltar_uma_linha()
            return nome_novo
        voltar_duas_linhas()

def imc(usuario):
    while True:
        pagina_imc(usuario)
        resp = validar_resposta(3)
        if resp == '1': calcular_imc(usuario)
        elif resp == '2': classificar_imc(usuario)
        elif resp == '3': return

def pagina_imc(usuario):
    carregar_tela()
    mostrar_pagina(f'IMC DE {usuario['nome'].upper()}')
    opcoes = [
        ('1', 'Calcular IMC'),
        ('2', 'Classificação'),
        ('3', 'Voltar')
    ]
    for chave, desc in opcoes:
        console.print(Align.center(f"[bold bright_magenta][{chave}][/] [destaque]{desc:<23}[/]"))
    console.print(Rule(style='menus'))
    print('')

def calcular_imc(usuario):
    carregar_tela()
    mostrar_pagina('CALCULAR IMC')
    imc = calcula_imc((usuario['peso'][0]), (usuario['altura'][0]))
    atualiza_imc(imc, usuario)
    print_meio(f'O IMC atual do usuário é {imc}.', 'sucesso')
    voltar()

def calcula_imc(peso, altura):
    return round((peso / altura ** 2), 2)

def atualiza_imc(imc, usuario):
    historico_imc = usuario['imc']
    historico_imc.insert(0, imc)
    usuario.update({'imc' : historico_imc})

def classificar_imc(usuario):
    carregar_tela()
    mostrar_pagina('CLASSIFICAR IMC')
    CATEGORIAS_IMC = ("Abaixo do peso", "Peso normal", "Sobrepeso", "Obesidade Grau I", "Obesidade Grau II", "Obesidade Grau III")
    imc = usuario['imc'][0] if usuario['imc'] else None
    if not imc:
        print_meio('O imc ainda não foi calculado!', 'alerta')
        voltar()
        return
    elif imc < 18.5:
        print_meio("O usuário está abaixo do peso.", 'destaque')
        categoria = CATEGORIAS_IMC[0]
    elif 18.5 <= imc < 25:
        print_meio("O usuário está com peso normal.", 'destaque')
        categoria = CATEGORIAS_IMC[1]
    elif 25 <= imc < 30:
        print_meio('O usuário está acima do peso.', 'destaque')
        categoria = CATEGORIAS_IMC[2]
    elif 30 <= imc < 35:
        print_meio('O usuário está com obesidade grau I.', 'destaque')
        categoria = CATEGORIAS_IMC[3]
    elif 35 <= imc < 40:
        print_meio('O usuário está com obesidade grau II.', 'destaque')
        categoria = CATEGORIAS_IMC[4]
    else:
        print_meio('O usuário está com obesidade grau III.', 'destaque')
        categoria = CATEGORIAS_IMC[5]
    usuario.update({'categoria' : categoria})
    print_meio('Categoria atualizada.', 'sucesso')
    voltar()

def treinos(usuario, biblioteca_exercicios):
    while True:
        pagina_treinos(usuario)
        resp = validar_resposta(5)
        if resp == '1': adicionar_treino(usuario, biblioteca_exercicios)
        elif resp == '2': remover_treino(usuario)
        elif resp == '3': editar_treino(usuario)
        elif resp == '4': listar_treinos(usuario)
        elif resp == '5': return

def pagina_treinos(usuario):
    carregar_tela()
    mostrar_pagina(f'TREINOS DE {usuario['nome'].upper()}')
    opcoes = [
        ('1', 'Adicionar treino'),
        ('2', 'Remover treino'),
        ('3', 'Editar treino'),
        ('4', 'Listar treinos'),
        ('5', 'Voltar')
    ]
    for chave, desc in opcoes:
        console.print(Align.center(f"[bold bright_magenta][{chave}][/] [destaque]{desc:<23}[/]"))
    console.print(Rule(style='menus'))
    print('')

def procurar_treino(nome_treino, usuario):
    if nome_treino in usuario['treinos'].keys():
        return True
    return False

def editar_treino(usuario):
    carregar_tela()
    mostrar_pagina('EDITAR TREINO')
    while True:
        treino_procurado = input_meio('Digite o nome do treino pra editar: ')
        if not procurar_treino(treino_procurado, usuario):
            voltar_uma_linha()
            print_meio('O treino não foi encontrado.', 'alerta')
            continue
        voltar_uma_linha()
        print_meio(f'Treino: {treino_procurado}', 'destaque')
        print_meio('Treino encontrado.', 'sucesso')
        confirmar_edicao_treino(treino_procurado, usuario)
        return

def confirmar_edicao_treino(treino_editado, usuario):
    for exercicio in usuario['treinos'][treino_editado]:
        print_meio(f'Exercicio: {exercicio}', 'destaque')
        series_novas = int(input_meio('Digite o novo número de series ou 999 pra manter igual: '))
        if series_novas == 999:
            continue
        repeticoes_novas = int(input_meio('Digite o novo número de repeticoes: '))
        exercicio.update({'series' : series_novas, 'repeticoes' : repeticoes_novas})
        print_meio(f'Exercicio: {exercicio}', 'sucesso')
    voltar()

def listar_treinos(usuario):
    carregar_tela()
    mostrar_pagina('LISTAR TREINOS')
    if not verificar_treinos(usuario):
        print_meio('Nenhum treino cadastrado.', 'alerta')
        voltar()
        return
    for i, treino in enumerate(usuario['treinos'], 1):
        print_meio(f'{i}. {treino}', 'destaque')
    voltar()

def adicionar_treino(usuario, biblioteca_exercicios):
    carregar_tela()
    mostrar_pagina('ADICIONAR TREINO')
    while True:
        nome_treino = input_meio('Digite o nome do novo treino: ')
        if procurar_treino(nome_treino, usuario):
            voltar_uma_linha()
            print_meio('Você já tem um treino com esse nome!', 'alerta')
            continue
        voltar_uma_linha()
        print_meio(f'Nome: {nome_treino}', 'destaque')
        confirmar_adicao_treino(nome_treino)
        break
    lista_exercicios = selecionar_exercicio(biblioteca_exercicios)
    if lista_exercicios is None:
        return
    else:
        usuario['treinos'].update({nome_treino : lista_exercicios})
        print_meio(f'{nome_treino} adicionado a lista de treinos.', 'sucesso')
        voltar()

def confirmar_adicao_treino(nome_treino):
    while True:
        resp = input_meio(f'Deseja salvar com o nome {nome_treino}? S/N ').strip().upper()
        if resp == 'S': break
        elif resp == 'N': continue
        else:
            voltar_uma_linha()
            print_meio('RESPOSTA INVÁLIDA!', 'erro')

def selecionar_exercicio(biblioteca_exercicios):
    lista_exercicios = []
    while True:
        carregar_tela()
        mostrar_pagina('SELECIONAR EXERCICIO')
        mostrar_exercicios(biblioteca_exercicios)
        exercicio = validar_exercicio(biblioteca_exercicios)
        series = int(input_meio('Digite o número de series: '))
        repeticoes = int(input_meio('Digite o número de repetições: '))
        lista_exercicios.append({'exercicio' : exercicio, 'series' : series, 'repeticoes' : repeticoes})
        print_meio(f'Exercicio {exercicio} adicionado com {series} series de {repeticoes} repetições.', 'sucesso')
        resp = input_meio('Deseja adicionar mais exercicios? S/N ').upper()
        if resp == 'N':
            for item in lista_exercicios:
                print_meio(f'{item["exercicio"]} - {item["series"]}x{item["repeticoes"]}', 'destaque')
            resp = input_meio('Deseja confirmar o treino novo? S/N ').upper()
            if resp == 'S': return lista_exercicios
            else: return None

def mostrar_exercicios(biblioteca_exercicios):
    print_meio('Exercicios disponíveis: ', 'destaque')
    for grupo in biblioteca_exercicios:
        print_meio(f'{grupo}: {biblioteca_exercicios[grupo]}', 'destaque')
    mostrar_linha()

def exercicio_existe(exercicio, biblioteca_exercicios):
    for exercicios in biblioteca_exercicios.values():
        if exercicio in exercicios:
            return True
    return False

def validar_exercicio(biblioteca_exercicios):
    while True:
        exercicio_procurado = input_meio('Digite o exercicio: ').lower()
        if not exercicio_existe(exercicio_procurado, biblioteca_exercicios):
            voltar_uma_linha()
            print_meio('Exercicio não encontrado!', 'alerta')
        else:
            voltar_uma_linha()
            print_meio(f'Exercicio: {exercicio_procurado}', 'destaque')
            print_meio('Exercicio encontrado.', 'sucesso')
            return exercicio_procurado

def remover_treino(usuario):
    carregar_tela()
    mostrar_pagina('REMOVER TREINO')
    while True:
        treino_procurado = input_meio('Digite o nome do treino a ser removido: ')
        if treino_procurado not in usuario['treinos'].keys():
            voltar_uma_linha()
            print_meio('Treino não encontrado!', 'alerta')
            continue
        voltar_uma_linha()
        print_meio(f'Treino: {treino_procurado}', 'destaque')
        resp = input_meio(f'Deseja remover o treino {treino_procurado}? S/N ').upper()
        if resp == 'N': continue
        elif resp == 'S':
            del usuario['treinos'][treino_procurado]
            print_meio('Treino removido.', 'sucesso')
            voltar()
            return

def exercicios(usuario, biblioteca_exercicios):
    while True:
        pagina_exercicios(usuario)
        resp = validar_resposta(4)
        if resp == '1': criar_exercicio(biblioteca_exercicios)
        elif resp == '2': pesquisar_nome(biblioteca_exercicios)
        elif resp == '3': pesquisar_grupo(biblioteca_exercicios)
        elif resp == '4': return

def pagina_exercicios(usuario):
    carregar_tela()
    mostrar_pagina(f'EXERCICIOS DE {usuario['nome'].upper()}')
    opcoes = [
        ('1', 'Criar exercicio'),
        ('2', 'Pesquisar por nome'),
        ('3', 'Pesquisar por grupo'),
        ('4', 'Voltar')
    ]
    for chave, desc in opcoes:
        console.print(Align.center(f"[bold bright_magenta][{chave}][/] [destaque]{desc:<23}[/]"))
    console.print(Rule(style='menus'))
    print('')

def criar_exercicio(biblioteca_exercicios):
    carregar_tela()
    mostrar_pagina('CRIAR EXERCICIO')
    mostrar_grupos(biblioteca_exercicios)
    grupo_escolhido = procurar_grupo(biblioteca_exercicios)
    exercicio_novo = confirmar_exercicio_novo(grupo_escolhido, biblioteca_exercicios)
    adicionar_exercicio(grupo_escolhido, exercicio_novo, biblioteca_exercicios)

def adicionar_exercicio(grupo_escolhido, exercicio_novo, biblioteca_exercicios):
    biblioteca_exercicios[grupo_escolhido].append(exercicio_novo)
    print_meio(f'{biblioteca_exercicios[grupo_escolhido]}', 'destaque')
    print_meio('Exercicio novo confirmado.', 'sucesso')
    voltar()

def mostrar_grupos(biblioteca_exercicios):
    print_meio('Grupos musculares:', 'destaque')
    for grupo in biblioteca_exercicios.keys():
        print_meio(grupo.capitalize(), 'destaque')
    mostrar_linha()

def confirmar_exercicio_novo(grupo_escolhido, biblioteca_exercicios):
    while True:
        exercicio_novo = validar_exercicio_novo(biblioteca_exercicios)
        resp = input_meio(f'Deseja salvar o exercicio {exercicio_novo} no grupo {grupo_escolhido}? S/N ').strip().upper()
        if resp == 'S': return exercicio_novo
        voltar_duas_linhas()

def procurar_grupo(biblioteca_exercicios):
    while True:
        grupo_procurado = input_meio('Digite o nome do grupo muscular: ').strip().lower()
        if grupo_procurado not in biblioteca_exercicios.keys():
            voltar_uma_linha()
            print_meio('Grupo não encontrado!', 'alerta')
            continue
        voltar_uma_linha()
        print_meio(f'Grupo: {grupo_procurado}', 'destaque')
        print_meio('Grupo encontrado.', 'sucesso')
        return grupo_procurado

def pesquisar_nome(biblioteca_exercicios):
    carregar_tela()
    mostrar_pagina('PESQUISAR POR NOME')
    nome_procurado = input_meio('Digite o nome a ser procurado: ').strip().lower()
    voltar_uma_linha()
    print_meio(f'Nome: {nome_procurado}', 'destaque')
    procurar_exercicio(nome_procurado, biblioteca_exercicios)
    voltar()

def procurar_exercicio(nome_procurado, biblioteca_exercicios):
    for grupo, exercicios in biblioteca_exercicios.items():
        if nome_procurado in exercicios:
            print_meio('Exercicio encontrado.', 'sucesso')
            print_meio(f'{nome_procurado} pertence ao grupo {grupo}.', 'destaque')
            return
    print_meio('Exercicio não encontrado!', 'alerta')

def pesquisar_grupo(biblioteca_exercicios):
    while True:
        carregar_tela()
        mostrar_pagina('PESQUISAR POR GRUPO')
        grupo_procurado = procurar_grupo(biblioteca_exercicios)
        print_meio(f'{grupo_procurado}: {biblioteca_exercicios[grupo_procurado]}', 'destaque')
        resp = input_meio('Deseja pesquisar outro grupo? S/N ').strip().upper()
        if resp != 'S': return

def validar_exercicio_novo(biblioteca_exercicios):
    print('')
    while True:
        exercicio_novo = input_meio('Digite o nome do novo exercicio: ').strip().lower()
        mensagem_erro = ""
        if exercicio_novo == "":
            mensagem_erro = 'O nome do exercicio não pode ser vazio!'
        elif exercicio_existe(exercicio_novo, biblioteca_exercicios):
            mensagem_erro = 'O nome do exercicio já foi registrado!'
        elif not (4 <= len(exercicio_novo)):
            mensagem_erro = 'O nome do exercicio deve possuir no mínimo 4 letras!'
        elif not (exercicio_novo.replace(' ','').isalpha()):
            mensagem_erro = 'O nome do exercicio deve possuir apenas letras!'
        if mensagem_erro:
            voltar_duas_linhas()
            print_meio(mensagem_erro, 'alerta')
            continue
        voltar_duas_linhas()
        print_meio(f'Exercicio: {exercicio_novo}', 'destaque')
        return exercicio_novo

def calcula_total_exercicios(usuario):
    total_exercicios = 0
    for treino in usuario['treinos'].values():
        total_exercicios += len(treino)
    return total_exercicios

def calcula_total_treinos(usuario):
    return len(usuario['treinos'].keys())

def verificar_treinos(usuario):
    return True if usuario['treinos'] else False

def estatisticas_individuais(usuario):
    carregar_tela()
    mostrar_pagina(f'ESTATISTICAS DE {usuario['nome'].upper()}')
    if not verificar_treinos(usuario):
        print_meio('Nenhum treino cadastrado.', 'alerta')
        voltar()
        return
    total_treinos = calcula_total_treinos(usuario)
    total_exercicios = calcula_total_exercicios(usuario)
    peso = usuario['peso'][0]
    imc = usuario['imc'][0] if usuario['imc'] else 'Indefinido'
    treino_maior, treino_menor, qtd_maior, qtd_menor = calcula_treino(usuario)
    print_meio(f'Quantidade de treinos: {total_treinos}', 'destaque')
    print_meio(f'Quantidade de exercicios: {total_exercicios}', 'destaque')
    print_meio(f'Peso: {peso}', 'destaque')
    print_meio(f'IMC: {imc}', 'destaque')
    print_meio(f'Maior treino: {treino_maior} ({qtd_maior} exercícios)', 'destaque')
    print_meio(f'Menor treino: {treino_menor} ({qtd_menor} exercícios)', 'destaque')
    mostrar_linha()
    voltar()
    return

def calcula_treino(usuario):
    treinos = usuario['treinos']
    treino_maior = max(treinos, key=lambda k: len(treinos[k]))
    treino_menor = min(treinos, key=lambda k: len(treinos[k]))
    return (
        treino_maior, 
        treino_menor, 
        len(treinos[treino_maior]), 
        len(treinos[treino_menor])
    )

def ranking(usuarios):
    carregar_tela()
    mostrar_pagina('RANKING GERAL')
    if not usuarios:
        print_meio('Nenhum usuário cadastrado.', 'alerta')
        voltar()
        return

    mais_pesado = max(usuarios.items(), key=lambda item: item[1]['peso'][0])
    mais_alto = max(usuarios.items(), key=lambda item: item[1]['altura'][0])
    mais_velho = max(usuarios.items(), key=lambda item: item[1]['idade'])
    mais_novo = min(usuarios.items(), key=lambda item: item[1]['idade'])
    mais_treinos = max(usuarios.items(), key=lambda item : len(item[1]['treinos']))
    menos_treinos = min(usuarios.items(), key=lambda item : len(item[1]['treinos']))

    usuarios_com_imc = [
        (email, dados) for email, dados in usuarios.items()
        if dados['imc'][0] is not None
    ]

    print_meio(f'Mais pesado: {mais_pesado[1]["nome"]} ({mais_pesado[0]}) - {mais_pesado[1]["peso"][0]} kg', 'destaque')
    print_meio(f'Mais alto: {mais_alto[1]["nome"]} ({mais_alto[0]}) - {mais_alto[1]["altura"][0]:.2f} m', 'destaque')
    print_meio(f'Mais velho: {mais_velho[1]["nome"]} ({mais_velho[0]}) - {mais_velho[1]["idade"]} anos', 'destaque')
    print_meio(f'Mais novo: {mais_novo[1]["nome"]} ({mais_novo[0]}) - {mais_novo[1]["idade"]} anos', 'destaque')
    print_meio(f'Mais treinos: {mais_treinos[1]["nome"]} ({mais_treinos[0]}) - {len(mais_treinos[1]['treinos'])} treinos', 'destaque')
    print_meio(f'Menos treinos: {menos_treinos[1]["nome"]} ({menos_treinos[0]}) - {len(menos_treinos[1]['treinos'])} treinos', 'destaque')

    if usuarios_com_imc:
        mais_imc = max(usuarios_com_imc, key=lambda item: item[1]['imc'][0])
        menos_imc = min(usuarios_com_imc, key=lambda item: item[1]['imc'][0])
        print_meio(f'Maior IMC: {mais_imc[1]["nome"]} ({mais_imc[0]}) - {mais_imc[1]["imc"][0]}', 'destaque')
        print_meio(f'Menor IMC: {menos_imc[1]["nome"]} ({menos_imc[0]}) - {menos_imc[1]["imc"][0]}', 'destaque')
    else:
        print_meio('Nenhum IMC calculado ainda.', 'alerta')
    mostrar_linha()
    voltar()

def calcula_estatisticas_gerais(usuarios):
    quant_usuarios = len(usuarios)
    quant_treinos = 0
    quant_exercicios = 0
    total_peso = 0
    total_altura = 0
    total_imc = 0
    quant_imc = len([dados for dados in usuarios.values() if dados['imc'][0] is not None])
    for usuario in usuarios.values():
        total_peso += usuario['peso'][0]
        total_altura += usuario['altura'][0]
        total_imc += usuario['imc'][0] if usuario['imc'][0] else 0
        for treino in usuario['treinos'].values():
            quant_exercicios += len(treino)
        quant_treinos += len(usuario['treinos'])
    return (quant_usuarios, 
            quant_treinos, 
            quant_exercicios, 
            total_peso/quant_usuarios, 
            total_altura/quant_usuarios, 
            total_imc/quant_imc, 
            quant_imc)

def estatisticas_gerais(usuarios):
    carregar_tela()
    mostrar_pagina('ESTATISTICAS GERAIS')
    (quant_usuarios,
     quant_treinos,
     quant_exercicios,
     media_pesos,
     media_alturas,
     media_imcs,
     quant_imc) = calcula_estatisticas_gerais(usuarios)
    print_meio(f'Quantidade de usuários: {quant_usuarios}', 'destaque')
    print_meio(f'Quantidade total de treinos: {quant_treinos}', 'destaque')
    print_meio(f'Quantidade total de exercicios: {quant_exercicios}', 'destaque')
    print_meio(f'Média dos pesos: {(media_pesos):.1f}', 'destaque')
    print_meio(f'Média das alturas: {(media_alturas):.2f}', 'destaque')
    print_meio(f'Média dos IMCs: {(media_imcs):.2f}' if quant_imc > 0 else 'Nenhum IMC registrado.', 'destaque' if quant_imc > 0 else 'alerta')
    mostrar_linha()
    voltar()
    return

def configuracoes(usuario):
    while True:
        pagina_configuracoes()
        resp = validar_resposta(2)
        if resp == '1': trocar_senha(usuario)
        elif resp == '2': return

def pagina_configuracoes():
    carregar_tela()
    mostrar_pagina('CONFIGURAÇÕES')
    opcoes = [
        ('1', 'Trocar senha'),
        ('2', 'Voltar')
    ]
    for chave, desc in opcoes:
        console.print(Align.center(f"[bold bright_magenta][{chave}][/] [destaque]{desc:<23}[/]"))
    console.print(Rule(style='menus'))
    print('')

def trocar_senha(usuario):
    carregar_tela()
    mostrar_pagina('TROCAR SENHA')
    print_meio(f'Senha atual: {usuario['senha']}', 'destaque')
    senha_nova = confirmar_trocar_senha(usuario)
    usuario.update({'senha' : senha_nova})
    print_meio('Senha atualizada.', 'sucesso')
    voltar()

def confirmar_trocar_senha(usuario):
    print('')
    while True:
        senha_nova = validar_senha()
        resp = input_meio(f'Deseja trocar {usuario['senha']} por {senha_nova}? S/N ').strip().upper()
        if resp == 'S': return senha_nova
        voltar_duas_linhas()

def excluir_conta(usuario, usuarios):
    carregar_tela()
    mostrar_pagina('EXCLUIR CONTA')
    print_meio('Confirme sua senha para poder realizar a exclusão.', 'alerta')
    while True:
        senha_exclusao = validar_senha()
        if senha_exclusao != usuario['senha']:
            voltar_uma_linha()
            print_meio('Senha incorreta!', 'erro')
            continue
        voltar_uma_linha()
        print_meio('Senha correta.', 'sucesso')
        break
    resp = input_meio('VOCÊ REALMENTE QUER EXCLUIR A CONTA? S/N ').strip().upper()
    if resp == 'S':
        del usuarios[usuario['email']]
        print_meio('Conta Excluída.', 'sucesso')
        voltar()
        return

def logout(usuario, usuarios):
    while True:
        pagina_logout()
        resp = validar_resposta(2)
        if resp == '1':
            deslogar(usuario)
            break
        if resp == '2':
            excluir_conta(usuario, usuarios)
            break
    return

def pagina_logout():
    carregar_tela()
    mostrar_pagina('LOGOUT')
    opcoes = [
        ('1', 'Sair da conta'),
        ('2', 'Excluir conta')
    ]
    for chave, desc in opcoes:
        console.print(Align.center(f"[bold bright_magenta][{chave}][/] [destaque]{desc:<23}[/]"))
    console.print(Rule(style='menus'))
    print('')

def deslogar(usuario):
    print_meio(f'Volte sempre {usuario['nome']}!', 'sucesso')
    print_meio('Deslogando...', 'alerta')
    return

def menu_principal(usuario, usuarios, biblioteca_exercicios):
    while True:
        pagina_menu_principal(usuario['nome'])
        resp = input_meio('Qual ação deseja realizar? ')
        if resp == '1': perfil(usuario, usuarios)
        elif resp == '2': imc(usuario)
        elif resp == '3': treinos(usuario, biblioteca_exercicios)
        elif resp == '4': exercicios(usuario, biblioteca_exercicios)
        elif resp == '5': estatisticas_individuais(usuario)
        elif resp == '6': estatisticas_gerais(usuarios)
        elif resp == '7': ranking(usuarios)
        elif resp == '8': configuracoes(usuario)
        elif resp == '9': break
        else: resposta_invalida()

def pagina_menu_principal(nome):
    carregar_tela()
    mostrar_pagina(f'BEM-VINDO {nome.upper()}')
    opcoes = [
        ('1', 'Perfil'),
        ('2', 'IMC'),
        ('3', 'Treinos'),
        ('4', 'Exercícios'),
        ('5', 'Estatísticas Individuais'),
        ('6', 'Estatísticas Gerais'),
        ('7', 'Ranking'),
        ('8', 'Configurações'),
        ('9', 'Logout')
    ]
    for chave, desc in opcoes:
        console.print(Align.center(f"[bold bright_magenta][{chave}][/] [destaque]{desc:<23}[/]"))
    console.print(Rule(style='menus'))
    print('')

def iniciar():
    console.print(Panel(Align.center('[bold white on blue]:weight_lifter:  ACADEMIA:running:[/]'), box=box.DOUBLE, style='menus'))
    console.print('Pressione enter para iniciar', style='white', end=' ', justify='center')
    input_meio()
    carregar_dados()
    encerrar()


if __name__ == "__main__":

    iniciar()