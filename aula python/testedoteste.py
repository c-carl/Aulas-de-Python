print("\n")
print("="*70)
print("         Prezado usuário, seja bem-vindo à tela de cadastro ")
print("Para disponibilizarmos o seu acesso, é necessário fazer o cadastro")
print("                            Vamos lá!")
print("="*70+"\n")

print("="*70)
print("                  Digite as suas informações abaixo")
print("="*70+"\n")


print("="*70)
name=input("Digite o seu primeiro nome: ")
print("="*70)

sobrename=input("Digite o seu segundo nome: ")
print("="*70)

idade=int(input("Digite a sua idade: "))
print("="*70)

cpf=int(input("Digite o seu CPF: "))
print("="*70)

renda=float(input("Digite a sua renda: "))
print("="*70)

estado=input("Digite em que Estado você se localiza: ")
print("="*70)

cidade=input("Digite a Cidade em que você se localiza: ")
print("="*70)

bairro=input("Digite qual o bairro que você se localiza: ")
print("="*70)

course=input("Digite o curso que você está fazendo: ")
print("="*70)

faculdade=input("Digite onde é o polo que você realiza a sua faculdade: ")
print("="*70)

email=input("Digite o seu email: ")
print("="*70)

cell=input("Digite o seu celular com DDD: ")
print("="*70)

print("\n")

print("-"*70)
print("↓                      Relatório de Dados                            ↓") 
print("-"*70+"\n")


print("-"*70)
print("=                    Informações de Pessoais                         =")
print("-"*70)


print(f"|  Nome: {name}\n|  Sobrenome: {sobrename}\n|  Idade: {idade}\n|  CPF: {cpf}\n|  Renda: {renda}")


print("-"*70)
print("=                  Informações de Localização                        =")
print("-"*70)


print(f"|  Estado: {estado}\n|  Cidade: {cidade}\n|  Bairro: {bairro}")


print("-"*70)
print("=                    Informações de Contato                          =")
print("-"*70)


print(f"|  Celular: {cell}\n|  Email: {email}")


print("-"*70)
print("=                     Informações de Curso                           =")
print("-"*70)


print(f"|  Curso: {course}\n|  Polo da Curso: {faculdade}")
print("-"*70)
print(" "*1000)

