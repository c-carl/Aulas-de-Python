def script_calcula_nota(nome: str, nota1: float, nota2: float) -> None:
    media = (nota1+nota2)/2
    if media < 0:
        print("Média negativa, média inválida {}.".format(media))
    elif media >= 7 and media <= 10.0:
        print("O aluno %s foi aprovado coma media %.1f" % (nome, media))
    elif media < 7.0:
        print(f"O aluno {nome} foi reprovado com a media `{media:1.f}")
    else:
        print("Media inválida")

if __name__ =="__main__":
    nome = str(input("Digite seu nome: "))
    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))
    script_calcula_nota(nome, nota1, nota2)
        