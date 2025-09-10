def aluno():
    name=(input("Digite o seu nome: "))
    idade=(input("Digite a sua idade: "))
    av1=float(input("Digite a nota da av1: "))
    av2=float(input("Digite a nota da av2: "))

    media=(av1+av2)/2

    if(media>=6):
        print("Você está aprovado com a média ")
    elif(media<=5):
        print("Você está de recuperação ")
    else:
        print("Você está de recuperação ")
aluno()
