

class Sistema:

    def __init__(self):
        self.alunos = []
        self.professores = []
        self.gestores = []

    def _buscar_pessoa(self, identificador, lista):
        '''Busca um usuário em uma lista específica (alunos, professores ou gestores) com base no identificador fornecido.'''

        for pessoa in lista:
            if pessoa.identificacao() == identificador:
                return pessoa

    def buscar_aluno(self, matricula):
        '''Busca um aluno no sistema com base na matrícula fornecida.'''

        return self._buscar_pessoa(matricula, self.alunos)

    def buscar_professor(self, cref):
        '''Busca um professor no sistema com base na matrícula fornecida.'''

        return self._buscar_pessoa(cref, self.professores)

    def buscar_gestor(self, codigo):
        '''Busca um gestor no sistema com base na matrícula fornecida.'''

        return self._buscar_pessoa(codigo, self.gestores)