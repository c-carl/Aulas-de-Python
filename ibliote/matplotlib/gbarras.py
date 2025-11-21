import matplotlib.pyplot as plt

categoria = ['A','B','C','D']
valores = [10, 20, 15, 5]

plt.bar(categoria, valores, color="red") # Deixa o gráfico na vertical

# Deve ser usado o modelo de cima ou o modelo abaixo, caso utilize os dois o código roda mas fica feio

plt.barh(categoria, valores, color="blue") # Deixa o gráfico na horizontal
plt.show()