from collections import defaultdict

estudantes_por_sala = defaultdict(list)

estudantes_por_sala['B'].append('Carlos')
estudantes_por_sala['A'].append('Gabigol')
estudantes_por_sala['A'].append('Neymar')

print(dict(estudantes_por_sala))