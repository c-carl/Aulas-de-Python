nome=input("Digite o nome do aluno: ")
av1=float(input("Digite a nota da AV1 do aluno: "))
av2=float(input("Digite a nota da AV2 do aluno: "))
media=(av1+av2)/2
if(media>=6):
    print(f"O aluno {nome} está aprovado com média igual a {media:.2f}")
elif(media>=4.0):
    print(f"O aluno {nome} está aprovado com a média igual a {media:.2f}")
else:
    print(f"O aluno {nome} está aprovado com a média igual a {media:.2f}")