from datetime import date

class Pessoa():
    def __init__(self, cpf: str, nome: str, nascimento: date, oculos: bool) -> None:
        self.cpf = cpf
        self.nome = nome
        self.nascimento = nascimento
        self.oculos = oculos

    def __str__(self):
        return f"CPF: {self.cpf}\nNOME: {self.nome}\nDATA: {self.nascimento}\nOCULOS: {self.oculos}"

nome = Pessoa("207.680.03-92", "Carlos", 10/8/2006, True)
print(nome)