import matplotlib.pyplot as plt

categorias = ['A','B','C','D']
valores = [10, 20, 15, 5]

plt.pie(valores, labels=categorias)
plt.show()