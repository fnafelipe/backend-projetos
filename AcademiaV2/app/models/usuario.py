

class Usuario:

    def __init__(self, nome, idade, sexo):
        self.nome = nome
        self.idade = idade
        self.sexo = sexo

    @property
    def nome(self):
        return self.__nome
    @property
    def idade(self):
        return self.__idade
    @property
    def sexo(self):
        return self.__sexo

    @nome.setter
    def nome(self, nome):
        if not isinstance(nome, str):
            raise TypeError('O nome da usuário deve ser um str!')
        if not (4 <= len(nome)):
            raise ValueError('O nome deve possuir ao menos 4 letras!')
        self.__nome = nome

    @idade.setter
    def idade(self, idade):
        IDADE_MINIMA, IDADE_MAXIMA = 18, 120
        if not isinstance(idade, int):
            raise TypeError('A idade deve ser um int!')
        if not (IDADE_MINIMA <= idade <= IDADE_MAXIMA):
            raise ValueError('A idade deve estar entre 18 e 120 anos!')
        self.__idade = idade

    @sexo.setter
    def sexo(self, sexo):
        SEXOS = ('masculino', 'feminino')
        if sexo.lower() not in SEXOS:
            raise ValueError('Sexo deve ser Masculino ou Feminino!')
        self.__sexo = sexo.lower()

    def info(self):
        print(f'Nome: {self.nome}')
        print(f'Idade: {self.idade} anos')
        print(f'Sexo: {self.sexo}')

    def para_dict(self):
        dicionario = {
            'nome' : self.nome,
            'idade' : self.idade,
            'sexo' : self.sexo
        }
        return dicionario