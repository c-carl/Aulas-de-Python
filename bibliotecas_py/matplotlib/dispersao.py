import matplotlib.pyplot as plt

x = [1,2,3,4,5]
y1 = [2,5,9,3,8]
y2 = [1,2,1,1,2]


plt.scatter(x,y1, label="Relação entre o eixo X e Y1", 
            color='red', linestyle="--", marker="o", s=100) # Gera o gráfico
plt.scatter(x,y2, label="Relação entre o eixo X e Y2", color='green', linestyle="--", marker="x")
plt.fill_between(x, y1, y2, color="orange")


plt.title("Gráfico de linha")
plt.xlabel("Eixo X")
plt.ylabel("Eixo Y")
plt.legend()
plt.show() # Exibe o gráfico na tela