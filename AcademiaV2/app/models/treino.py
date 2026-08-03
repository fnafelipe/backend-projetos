from models.exercicio import Exercicio
from utils.auxiliares import confirmar


class Treino:

    def __init__(self, nome):
        self.nome = nome
        self.exercicios = []

    @property
    def nome(self):
        return self.__nome
    @property
    def exercicios(self):
        return self.__exercicios

    @nome.setter
    def nome(self, nome):
        if not (isinstance(nome, str)):
            raise TypeError('O nome do treino deve ser uma string!')
        if not (4 <= len(nome)):
            raise ValueError('O nome do treino deve possuir pelo menos 4 letras!')
        self.__nome = nome

    def adicionar_exercicio(self, exercicio_novo):
        if not isinstance(exercicio_novo, Exercicio):
            raise TypeError('O exercicio novo deve ser válido!')
        if confirmar(f'Deseja adicionar o exercicio {exercicio_novo.nome} com {exercicio_novo.series} de {exercicio_novo.repeticoes} aos treinos?'):
            self.__exercicios.append(exercicio_novo)
            print('Exercicio adicionado.')
        else:
            print('Exercicio não adicionado!')

    def remover_exercicio(self, exercicio_procurado):
        if not isinstance(exercicio_procurado, Exercicio):
            raise TypeError('O exercicio procurado deve ser válido!')
        if exercicio_procurado not in self.__exercicios:
            raise ValueError('Exercicio não encontrado!')
        if confirmar(f'Deseja remover o exercicio {exercicio_procurado.nome} dos treinos?'):
            self.__exercicios.remove(exercicio_procurado)
            print('Exercicio removido.')
        else:
            print('Exxercicio não removido!')

    def info(self):
        print(self.nome)
        for exercicio in self.exercicios:
            exercicio.info()

    def to_dict(self):
        treino = {
            'nome' : self.nome,
            'exercicios' : [exercicio.to_dict() for exercicio in self.exercicios]
        }
        return treino

    @classmethod
    def from_dict(cls, dicionario):
        return cls(
            nome = dicionario['nome'],
            exercicios = [Exercicio.from_dict(exercicio) for exercicio in dicionario['exercicios']]
        )
