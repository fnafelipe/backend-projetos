from models.aluno import Aluno
from models.professor import Professor
from models.gestor import Gestor
from models.exercicio import Exercicio
from models.treino import Treino
from services.armazenamento import salvar_usuario
from rich import inspect

aluno = Aluno('Felipe', 19, 'masculino', 64.3, 1.85)
professor = Professor('Raimundo', 55, 'masculino', '123456-P/PI', 'musculacao')
gestor = Gestor('Fernanda', 61, 'feminino', 'executivo')

exercicio1 = Exercicio('rosca direta', 'biceps', 3, 8)
exercicio2 = Exercicio('triceps frances', 'triceps', 2, 10)
exercicio3 = Exercicio('desenvolvimento', 'ombro', 4, 6)

exercicio4 = Exercicio('leg press', 'quadriceps', 4, 8)
exercicio5 = Exercicio('cadeira flexora', 'posterior', 3, 10)

treino1 = Treino('Treino de braços', [exercicio1, exercicio2, exercicio3])
treino2 = Treino('Treino de perna', [exercicio4, exercicio5])

''' #TESTE HISTORICO PESO E ALTURA
usuario.atualizar_altura(1.84)
usuario.atualizar_peso(64.7)
usuario.info()
usuario.atualizar_peso(65)
usuario.info()'''

'''#TESTE MANIPULANDO TREINOS EM USUARIO
usuario.adicionar_treino(treino1)
usuario.adicionar_treino(treino2)
usuario.info()
usuario.remover_treino(treino2)
usuario.info()'''

'''#TESTE ENCAPSULAMENTO
print(usuario.peso)
usuario.adicionar_treino(treino1)
usuario.adicionar_treino(treino2)
inspect(usuario, private=True)
usuario.nome = 'Carmem'
usuario.idade = 50
usuario.peso = 72
usuario.altura = 1.70
usuario.sexo = 'feminino'
inspect(usuario, private=True)
try:
    usuario.nome = 20
except Exception as e:
    print(f'Erro: {e}')
try:
    usuario.idade = 20.5
except Exception as e:
    print(f'Erro: {e}')
try:
    usuario.peso = 20
except Exception as e:
    print(f'Erro: {e}')
try:
    usuario.altura = 'Felipe'
except Exception as e:
    print(f'Erro: {e}')
try:
    usuario.sexo = ''
except Exception as e:
    print(f'Erro: {e}')'''

#TESTE HERANÇA
inspect(aluno)
inspect(professor)
inspect(gestor)
#setters
try:
    aluno.nome = 'Felipe Aguiar'
    professor.especialidade = 'crossfit'
    gestor.cargo = 'diretor'
    #gestor.cargo = 19
    #aluno.nome = 189
    #aluno.idade = 15
    #professor.sexo = 'M'
except Exception as e:
    print(f'Erro: {e}')
#getters
print(aluno.nome)
print(aluno.peso)
print(professor.sexo)
print(professor.cref)
print(gestor.idade)
print(gestor.cargo)
#infos
aluno.info()
professor.info()
aluno.adicionar_treino(treino1)
professor.adicionar_aluno(aluno)
aluno.info()
professor.info()
