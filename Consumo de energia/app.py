#Programa de cálculo de consumo de energia eletrica

# Entrada de dados:
nome_aparelho=input ("Digite o nome do aparelho")
potencia=float (input("Digite a potência do aparelho em Watts(W):"))
horas_dias=float (input("Digite o tempo médio de uso diario em horas:"))

# Processamento
#Formula: (POtencia em W * horas de uso diário * 30 dias)/1000
consumo_mensal = (potencia * horas_dias * 30) / 1000

# Cálculo opcional do custo estimado (ex: R$ 0,75 por kWh)
tarifa_kwh = 0.75
custo_estimado = consumo_mensal * tarifa_kwh

# Saída de dados
print("\n" + "="*30)
print(f"Aparelho: {nome_aparelho}")
print(f"Consumo estimado: {consumo_mensal:.2f} kWh/mês")
print(f"Custo estimado (R$ {tarifa_kwh:.2f}/kWh): R$ {custo_estimado:.2f}/mês")
print("="*30)

