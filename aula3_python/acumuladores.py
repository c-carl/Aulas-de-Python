total,cont,media_turma,soma = 2, 1, 0, 0
while True:
    nome = input("Nome: ")
    if nome == '-1':
        break
    n1 = float(input("Nota da primeira prova: "))
    n2 = float(input("Nota da seguunda prova: "))
    media =(n1+n2) / 2
    if media >= 7:
        print(f"O aluno {nome} foi aprovado com media {media}" )
    else:
        print(f"O aluno {nome} foi aprovado com media {media}" )