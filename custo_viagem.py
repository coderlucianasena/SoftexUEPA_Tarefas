print("=== Planejador de Custo de Viagem ===")

# Entrada de dados
distancia = float(input("Distância da viagem (km): "))
consumo = float(input("Consumo do carro (km/l): "))
preco = float(input("Preço do combustível (R$/l): "))

# Validação simples com operadores lógicos
if distancia <= 0 or consumo <= 0 or preco <= 0:
    print("❌ Erro: Todos os valores devem ser maiores que zero!")
else:
    # Cálculos
    litros = distancia / consumo
    custo = litros * preco
    
    # Exibição dos resultados
    print(f"\n📊 RESULTADOS:")
    print(f"📍 Distância: {distancia:.1f} km")
    print(f"⛽ Consumo: {consumo:.1f} km/l")
    print(f"💰 Preço: R$ {preco:.2f}/l")
    print(f"🛢️  Litros necessários: {litros:.2f} l")
    print(f"💵 Custo total: R$ {custo:.2f}")
    
    # Análise simples com operadores lógicos
    print(f"\n🧠 ANÁLISE:")
    
    # Verifica se é uma viagem econômica
    if consumo >= 10 and preco <= 5.0:
        print("✅ Viagem econômica!")
    elif consumo >= 10:
        print("✅ Veículo eficiente")
    elif preco <= 5.0:
        print("✅ Combustível com bom preço")
    else:
        print("⚠️  Considere otimizar")
    
    # Verifica o tipo de viagem
    if distancia > 100:
        print("🚗 Viagem longa")
    elif distancia > 50:
        print("🚙 Viagem média")
    else:
        print("🚶 Viagem curta")
