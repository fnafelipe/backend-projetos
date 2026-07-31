
from models.usuario import Usuario

class Gestor(Usuario):

    def __init__(self, nome, idade, sexo, cargo):
        super().__init__(nome, idade, sexo)
        self.cargo = cargo

    @property
    def cargo(self):
        return self.__cargo

    @cargo.setter
    def cargo(self, cargo):
        CARGOS = ('gerente', 'diretor', 'executivo')
        if not isinstance(cargo, str):
            raise TypeError('O cargo deve ser um str!')
        if cargo not in CARGOS:
            raise ValueError(f'O cargo deve ser válido! {CARGOS}')
        self.__cargo = cargo

    def adicionar_aluno(self):
        pass

    def remover_aluno(self):
        pass

    def adicionar_professor(self):
        pass

    def remover_professor(self):
        pass

    def adicionar_treino(self):
        pass

    def remover_treino(self):
        pass

    def info(self):
        super().info()
        print(f'Cargo: {self.cargo}')

    def para_dict(self):
        dicionario = super().para_dict()
        dicionario.update({'cargo' : self.cargo})
        return dicionario