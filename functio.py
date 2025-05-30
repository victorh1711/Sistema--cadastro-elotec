
def cadastrarmissao(lista):
    print("\n--- Cadastro de Missão ---")
    nave = input("Nome da nave: ")
    destino = input("Destino: ")
    tripulantes = int(input("Nº de tripulantes: "))
    combustivel = float(input("Combustível disponível (litros): "))
    duracao = int(input("Duração da missão (dias): "))
    
    missao = {
        "nave": nave,
        "destino": destino,
        "tripulantes": tripulantes,                                 
        "combustivel": combustivel,
        "duracao": duracao
    }
    lista.append(missao)
    print("Missão cadastrada com sucesso!")

def listarmissoes(lista):
    print("\n--- Missões Cadastradas ---")
    if len(lista) == 0:
        print("Nenhuma missão cadastrada.")
    else:

        for indice, missao in enumerate(lista):
            print(f"\nMissão {indice+1}")           
            print(f"Nave: {missao['nave']}")
            print(f"Destino: {missao['destino']}")
            print(f"Tripulantes: {missao['tripulantes']}")
            print(f"Combustível: {missao['combustivel']} L")
            print(f"Duração: {missao['duracao']} dias")

def simularlancamento(lista):
    print("\n--- Simulação de Lançamento ---")
    if len(lista) == 0:
        print("Nenhuma missão cadastrada.")
        return
    for indice, missao in enumerate(lista):
        print(f"{indice+1} - {missao['nave']} (Destino: {missao['destino']})")
    escolha = int(input("Escolha a missão: ")) -1
 
    if 0 <= escolha < len(lista):
        missao = lista[escolha]
        consumo = missao['tripulantes'] * 500

        print(f"\nSimulando a missão da nave {missao['nave']}")
        print(f"Combustível necessário: {consumo} L")
        print(f"Disponível: {missao['combustivel']} L")
        if missao['combustivel'] >= consumo:
            print("Missão aprovada! Lançamento autorizado.")
        else:
            print("Combustível insuficiente.")
    else:
        print("Missão invalida")
     
        