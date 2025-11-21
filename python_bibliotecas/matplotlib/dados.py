import matplotlib.pyplot as plt

x = [1,2,3,4,5]
y = [2,5,9,3,8]

plt.plot(x,y, label="Relação entre X e Y") # Gera o gráfico
plt.title("Gráfico de linha")
plt.xlabel("Eixo X")
plt.ylabel("Eixo de Y") 
plt.legend()
plt.show() # Exibe o gráfico