from utils.auxiliares import confirmar

class Usuario:
    def __init__(self, nome, idade, peso, altura, sexo):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura
        self.sexo = sexo
        self.treino = []

    def info(self):
        print(self.nome)
        print(self.idade)
        print(self.peso)
        print(self.altura)
        print(self.sexo)
        print([exercicio.nome for exercicio in self.treino])

    def atualizar_peso(self, peso_novo):
        print(f'Peso atual: {self.peso}')
        print(f'Peso novo: {peso_novo}')

        if confirmar(f'Deseja atualizar o peso de {self.nome}?'):
            self.peso = peso_novo
            print(f'Peso de {self.nome} atualizado.')

        else:
            print(f'Peso não atualizado!')

    def atualizar_altura(self, altura_nova):
        print(f'Altura atual: {self.altura}')
        print(f'Altura nova: {altura_nova}')

        if confirmar(f'Deseja atualizar a altura de {self.nome}?'):
            self.altura = altura_nova
            print(f'Altura de {self.nome} atualizada.')

        else:
            print(f'Altura não atualizada!')

    def adicionar_exercicio(self, exercicio_novo):
        if confirmar(f'Deseja adicionar o exercicio {exercicio_novo.nome} ao treino de {self.nome}?'):
            self.treino.append(exercicio_novo)
            print('Exercicio adicionado')
        else:
            print('Exercicio não adicionado!')

    def remover_exercicio(self, exercicio_procurado):
        if exercicio_procurado not in self.treino:
            print('Exercicio não encontrado')
        else:
            if confirmar(f'Deseja remover o exercicio {exercicio_procurado.nome} do treino de {self.nome}?'):
                self.treino.remove(exercicio_procurado)
                print('Exercicio removido.')
            else:
                print('Exercicio não removido!')

    def usuario_para_dict(self):
        dicionario = {
            'nome' : self.nome,
            'idade' : self.idade,
            'peso' : self.peso,
            'altura' : self.altura,
            'sexo' : self.sexo,
        }
        return dicionario
