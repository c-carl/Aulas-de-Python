from datetime import date

class Pessoa:
    def __init__(self, cpf: str, nome: str, nascimento: date, oculos: bool) -> None:
        self.cpf = cpf
        self.nome = nome
        self.nascimento = nascimento
        self.oculos = oculos

    def __str__(self):
        pass

class Marca:
    def __init__(self, id: int, nome: str, sigla: str) -> None:
        self.id = id
        self.nome = nome
        self.sigla = sigla

    def __str__(self):
        pass

class Veiculo:
    def __init__(self, placa: str, cor: str, proprietario_cpf: str, marca_id: int) -> None:
        self.placa = placa
        self.cor = cor
        self.proprietario_cpf = proprietario_cpf
        self.marca_id = marca_id

    def __str__(self):
        pass
