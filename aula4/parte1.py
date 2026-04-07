import pickle

dados = {"nome": "Carlos", "Idade": 19, "Profissão": "Técnico de Suporte N1 e N2"}

try:
    with open("dados.bin", "wb") as salva_binarios:
        pickle.dump(dados, salva_binarios)
    print("Dados salvos com sucesso!")
except Exception as e:
    print(f"Ocorreu um erro ao salvar os dados: {e}")

try:
    with open("dados.bin", "rb") as carrega_binario:
        dados_carregados = pickle.load(carrega_binario)
    print("Dados carregados com sucesso:"), dados_carregados
except Exception as e:
    print(f"Ocorreu um erro ao carregar os dados: {e}")