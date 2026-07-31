from app.models.exercicio import Exercicio
from app.models.aluno import Usuario
from app.services.armazenamento import salvar_usuario

usuario = Usuario('Felipe', 19, 64.3, 1.85, 'Masculino')
usuario.info()

usuario.atualizar_altura(1.84)
usuario.atualizar_peso(64.7)
usuario.info()

usuario.atualizar_peso(65)
usuario.info()
