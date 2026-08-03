
from models.pessoa import Pessoa


class Gestor(Pessoa):

    def __init__(self, codigo, nome, idade, sexo, cargo):
        super().__init__(nome, idade, sexo)
        self.codigo = codigo
        self.cargo = cargo

    @property
    def codigo(self):
        return self.__codigo

    @property
    def cargo(self):
        return self.__cargo

    @codigo.setter
    def codigo(self, codigo):
        if not isinstance(codigo, int):
            raise TypeError('O codigo deve ser um int!')
        if codigo <= 0:
            raise ValueError('O codigo deve ser um número positivo!')
        self.__codigo = codigo

    @cargo.setter
    def cargo(self, cargo):
        CARGOS = ('gerente', 'diretor', 'executivo')
        if not isinstance(cargo, str):
            raise TypeError('O cargo deve ser um str!')
        if cargo.lower() not in CARGOS:
            raise ValueError(f'O cargo deve ser válido! {CARGOS}')
        self.__cargo = cargo.lower()

    def identificacao(self):
        return self.codigo

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

    def to_dict(self):
        dicionario = super().to_dict()
        dicionario.update({'cargo' : self.cargo})
        return dicionario

    @classmethod
    def from_dict(cls, dicionario):
        return cls(
            nome = dicionario['nome'],
            idade = dicionario['idade'],
            sexo = dicionario['sexo'],
            codigo = dicionario['codigo'],
            cargo = dicionario['cargo']
        )