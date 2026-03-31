from collections import namedtuple

Ponto = namedtuple('Ponto', ['X', 'Y'])

meu_ponto = Ponto(10,20)
print(meu_ponto.X)
print(meu_ponto[1])