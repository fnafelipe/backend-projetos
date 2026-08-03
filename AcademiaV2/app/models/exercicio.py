from utils.auxiliares import confirmar


class Exercicio:
    def __init__(self, nome, grupo, series, repeticoes):
        self.nome = nome
        self.grupo = grupo
        self.series = series
        self.repeticoes = repeticoes

    @property
    def nome(self):
        return self.__nome
    @property
    def grupo(self):
        return self.__grupo
    @property
    def series(self):
        return self.__series
    @property
    def repeticoes(self):
        return self.__repeticoes

    @nome.setter
    def nome(self, nome):
        if not isinstance(nome, str):
            raise TypeError('O nome do exercicio deve ser uma string!')
        if not (4 <= len(nome)):
            raise ValueError('O nome do exercicio deve ter pelo menos 4 letras!')
        self.__nome = nome

    @grupo.setter
    def grupo(self, grupo):
        GRUPOS_MUSCULARES = ('peito', 'costas', 'biceps', 'triceps', 'ombros', 'quadriceps', 'posterior', 'panturrilha')
        if grupo.lower() not in GRUPOS_MUSCULARES:
            grupos = ', '.join(GRUPOS_MUSCULARES)
            raise ValueError(f'O grupo deve ser válido! {grupos}')
        self.__grupo = grupo

    @series.setter
    def series(self, series):
        if not isinstance(series, int):
            raise TypeError('As series devem ser numeros inteiros!')
        if series <= 0:
            raise ValueError('As series não podem ser negativas ou nulas!')
        self.__series = series

    @repeticoes.setter
    def repeticoes(self, repeticoes):
        if not isinstance(repeticoes, int):
            raise TypeError('As repetições devem ser numeros inteiros!')
        if repeticoes <= 0:
            raise ValueError('As repetições não podem ser negativas ou nulas!')
        self.__repeticoes = repeticoes

    def info(self):
        print(self.nome)
        print(self.grupo)
        print(self.series)
        print(self.repeticoes)

    def editar_series(self):
        print(f'Series atuais: {self.series}')
        series_novas = input('Series novas: ')
        if confirmar(f'Deseja atualizar as series do exercicio {self.nome}?'):
            self.series = series_novas
            print('Series atualizadas.')
        else:
            print('Series não atualizadas!')

    def editar_repeticoes(self):
        print(f'Repetições atuais: {self.repeticoes}')
        repeticoes_novas = input('Repetições novas: ')
        if confirmar(f'Deseja atualizar as repetições do exercicio {self.nome}?'):
            self.repeticoes = repeticoes_novas
            print('Repetições atualizadas.')
        else:
            print('Repetições não atualizadas!')

    def to_dict(self):
        exercicio = {
            'nome' : self.nome,
            'grupo' : self.grupo,
            'series' : self.series,
            'repeticoes' : self.repeticoes
        }
        return exercicio

    @classmethod
    def from_dict(cls, dicionario):
        return cls(
            nome = dicionario['nome'],
            grupo = dicionario['grupo'],
            series = dicionario['series'],
            repeticoes = dicionario['repeticoes']
        )