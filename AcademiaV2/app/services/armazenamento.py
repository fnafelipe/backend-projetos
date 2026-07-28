
import json

def carregar_usuarios():
    usuarios = []
    try:
        with open('data/usuarios.json', 'r', encoding='utf-8') as arquivo:
            usuarios = json.load(arquivo)
            return usuarios
    except FileNotFoundError:
        print('Arquivo não encontrado!')

def salvar_usuario(usuario):
    usuarios = carregar_usuarios()
    usuarios.append(usuario)
    try:
        with open('data/usuarios.json', 'w', encoding='utf-8') as arquivo:
            json.dump(usuarios, arquivo, indent=3, ensure_ascii=False)
    except Exception as e:
        print(f'Não salvou  {e}')