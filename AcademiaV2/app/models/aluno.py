
from models.treino import Treino
from models.usuario import Usuario

class Aluno(Usuario):
    def __init__(self, nome, idade, sexo, peso, altura):
        super().__init__(nome, idade, sexo)
        self.__historico_peso = []
        self.__historico_altura = []
        self.peso = peso
        self.altura = altura
        self.__treinos = []

    @property
    def peso(self):
        return self.__peso
    @property
    def historico_peso(self):
        return self.__historico_peso
    @property
    def altura(self):
        return self.__altura
    @property
    def historico_altura(self):
        return self.__historico_altura
    @property
    def treinos(self):
        return self.__treinos

    @peso.setter
    def peso(self, peso):
        PESO_MIN, PESO_MAX = 30, 250
        if not isinstance(peso, (int, float)):
            raise TypeError('O peso deve ser um número!')
        if not (PESO_MIN <= peso <= PESO_MAX):
            raise ValueError('O peso deve estar entre 30 e 250 kilos!')
        self.__peso = peso
        self.__historico_peso.insert(0, self.peso)

    @altura.setter
    def altura(self, altura):
        ALTURA_MIN, ALTURA_MAX = 1.25, 2.25
        if not isinstance(altura, (int, float)):
            raise TypeError('A altura deve ser um número!')
        if not (ALTURA_MIN <= altura <= ALTURA_MAX):
            raise ValueError('A altura deve estar entre 1.25 e 2.25 Metros!')
        self.__altura = altura
        self.__historico_altura.insert(0, self.altura)

    def atualizar_peso(self, peso):
        self.peso = peso

    def atualizar_altura(self, altura):
        self.altura = altura

    def adicionar_treino(self, treino):
        if not isinstance(treino, Treino):
            raise TypeError('O treino deve ser válido!')
        self.treinos.append(treino)
        
    def remover_treino(self, treino):
        if not isinstance(treino, Treino):
            raise TypeError('O treino deve ser válido!')
        if treino not in self.treinos:
            raise ValueError('Treino não encontrado!')
        self.treinos.remove(treino)
                
    def info(self):
        super().info()
        print(f'Peso atual: {self.peso} kg')
        print(f'Histórico Peso: {self.historico_peso}')
        print(f'Altura atual: {self.altura} m')
        print(f'Histórico Altura: {self.historico_altura}')
        print('Treinos:')
        for treino in self.treinos:
            treino.info()

    def para_dict(self):
        dicionario = super().para_dict()
        dicionario.update({'peso' : self.peso,
                           'historico_peso' : self.historico_peso,
                           'altura' : self.altura,
                           'historico_altura' : self.historico_altura,
                           'treinos' : [treino.para_dict() for treino in self.treinos]})
        return dicionario
