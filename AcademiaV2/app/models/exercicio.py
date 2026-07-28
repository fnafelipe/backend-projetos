from utils.auxiliares import confirmar

class Exercicio:
    def __init__(self, nome, grupo, series, repeticoes):
        self.nome = nome
        self.grupo = grupo
        self.series = series
        self.repeticoes = repeticoes

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

    def exercicio_para_dict(self):
        exercicio = {
            'nome' : self.nome,
            'grupo' : self.grupo,
            'series' : self.series,
            'repeticoes' : self.repeticoes
        }
        return exercicio