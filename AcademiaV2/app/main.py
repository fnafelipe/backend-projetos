from models.exercicio import Exercicio
from models.usuario import Usuario
from services.armazenamento import salvar_usuario

usuario = Usuario('Felipe', 19, 64.3, 1.85, 'Masculino')
usuario.info()
'''usuario.atualizar_peso(64.7)
usuario.info()
usuario.atualizar_altura(1.84)
usuario.info()'''
exercicio = Exercicio('Rosca direta', 'Biceps', 3, 8)
exercicio.info()
usuario.adicionar_exercicio(exercicio)
usuario.info()
usuario_dict = usuario.usuario_para_dict()
print(usuario_dict)
salvar_usuario(usuario_dict)
'''usuario.info()
usuario.remover_exercicio(exercicio)
usuario.info()'''

