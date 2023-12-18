# Classe Funcionario para calcular valor desconto INSS


class Funcionario(object):

    def __init__(self, nome, salario):

        self.nome = nome
        self.salario = salario

    def setnome(self, nome):
        self.nome = nome

    def getnome(self):
        return self.nome

    def setsalario(self, salario):
        self.salario = salario

    def getsalario(self):
        return self.salario

    def _str_(self):
        return (
            '\n Nome: ' + str(self.getnome()) +
            '\n Salario R$:  {:.2f}'.format(self.getsalario())