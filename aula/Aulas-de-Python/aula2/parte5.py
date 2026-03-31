import time

def get_coxinhas(*pedidos):
    print("--- [Return] Preparando TODA a formada de coxinhas de uma vez...")
    time.sleep(1) # Simula um processamento demorado
    return [f" {pedido} coxinhas " for pedido in pedidos]

def get_joelho(*pedidos):
    for pedido in pedidos:
        print(f"--- [Yield] Saindo um pedido de {pedido} joelho(s) agor!")
        time.sleep(1) # Simula o tempo de fritar um por um
        yield f" {pedido} joelho(s)"

if __name__ == "__main__":
    print("SOLICITANDO COXINHAS {return}: ")
    salgados_return = get_coxinhas(4, 6, 8)
    print("Recebi a lista completa: ", salgados_return)

    print("\n" + "="*30 + "\n")

    print("SOLICITANDO JOELHOS {Yield}: ")
    pedidos_joelho = get_joelho(4, 6, 8)
    for salgado in pedidos_joelho:
        print(f"Cliente recebeu: {salgado}")