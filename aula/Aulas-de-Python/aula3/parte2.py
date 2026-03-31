from collections import Counter

palavras = "maçã banana maça laranja banana maçã".split()
contagem = Counter(palavras)

print(contagem)

print(contagem.most_common(4))