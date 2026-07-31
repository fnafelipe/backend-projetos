from models.aluno import Aluno
from models.usuario import Usuario

class Professor(Usuario):

    def __init__(self, nome, idade, sexo, cref, especialidade):
        super().__init__(nome, idade, sexo)
        self.cref = cref
        self.especialidade = especialidade
        self.__alunos = []

    @property
    def cref(self):
        return self.__cref
    @property
    def especialidade(self):
        return self.__especialidade
    @property
    def alunos(self):
        return self.__alunos

    @cref.setter
    def cref(self, cref):
        ESTADOS = {
            'AC', 'AL', 'AP', 'AM', 'BA', 'CE', 'DF', 'ES', 'GO', 
            'MA', 'MT', 'MS', 'MG', 'PA', 'PB', 'PR', 'PE', 'PI', 
            'RJ', 'RN', 'RS', 'RO', 'RR', 'SC', 'SP', 'SE', 'TO'
        }
        if not isinstance(cref, str):
            raise TypeError('O cref deve ser um str!')
        if not (len(cref) == 11 and cref[0:6].isdigit() and cref[6] == '-' and cref[7] in ('G', 'P') and cref[8] == '/' and cref[9:11] in ESTADOS):
            raise ValueError('O cref deve ser válido! exp: 123456-G/PI')
        self.__cref = cref

    @especialidade.setter
    def especialidade(self, especialidade):
        ESPECIALIDADES = ('musculacao', 'crossfit', 'funcional', 'pilates')
        if not isinstance(especialidade, str):
            raise TypeError('A especialidade deve ser um str!')
        if especialidade.lower() not in ESPECIALIDADES:
            raise ValueError(f'A especialidade deve ser válida {ESPECIALIDADES}')
        self.__especialidade = especialidade.lower()

    def adicionar_aluno(self, aluno):
        if not isinstance(aluno, Aluno):
            raise TypeError('O aluno deve ser válido!')
        if aluno in self.alunos:
            raise ValueError('O aluno ja foi adicionado')
        self.alunos.append(aluno)

    def remover_aluno(self, aluno):
        if not isinstance(aluno, Aluno):
            raise TypeError('O aluno deve ser válido!')
        if aluno not in self.alunos:
            raise ValueError('O aluno não foi encontrado!')
        self.alunos.remove(aluno)

    def info(self):
        super().info()
        print(f'Cref: {self.cref}')
        print(f'Especialidade: {self.especialidade}')
        print(f'Alunos:')
        for aluno in self.alunos:
            aluno.info()

    def para_dict(self):
        dicionario = super().para_dict()
        dicionario.update({'cref' : self.cref,
                           'especialidade' : self.especialidade,
                           'alunos' : [aluno.para_dict() for aluno in self.alunos]})
        return dicionario