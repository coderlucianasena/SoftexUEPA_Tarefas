print("=== Planejador de Custo de Viagem ===")

distancia = float(input("Distância da viagem (km): "))
consumo = float(input("Consumo do carro (km/l): "))
preco = float(input("Preço do combustível (R$/l): "))

litros = distancia / consumo
custo = litros * preco

print(f"Custo total da viagem: R$ {custo:.2f}")
