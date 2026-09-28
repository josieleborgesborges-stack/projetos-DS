"""
Sistema de Desconto Progressivo para Loja Online
Este programa calcula o valor do desconto e o valor total a ser pago
com base no valor total da compra inserido pelo usuário.
"""

def calcular_desconto(valor_compra):
    """
    Função que determina o percentual de desconto com base nas regras da loja:
    - Menor que R$ 200,00: 5% de desconto
    - De R$ 200,00 até R$ 299,99: 10% de desconto
    - Maior ou igual a R$ 300,00: 15% de desconto
    """
    if valor_compra < 200.00:
        return 0.05
    elif valor_compra < 300.00:
        return 0.10
    else:
        return 0.15

def main():
    print("=== SISTEMA DE DESCONTO PROGRESSIVO ===")
    
    # Bloco 1: Entrada de dados com tratamento básico de erros
    try:
        valor_total_compra = float(input("Insira o valor total da compra (R$): "))
        
        if valor_total_compra < 0:
            print("Erro: O valor da compra não pode ser negativo.")
            return
            
    except ValueError:
        print("Erro: Por favor, insira um valor numérico válido.")
        return

    # Bloco 2: Processamento - Cálculo do percentual e do valor do desconto
    percentual_desconto = calcular_desconto(valor_total_compra)
    valor_desconto = valor_total_compra * percentual_desconto
    
    # Bloco 3: Processamento - Cálculo do valor final a ser pago
    valor_final = valor_total_compra - valor_desconto

    # Bloco 4: Exibição dos resultados formatados para o usuário
    print("\n--- RESUMO DA COMPRA ---")
    print(f"Valor original da compra: R$ {valor_total_compra:.2f}")
    print(f"Desconto aplicado: {int(percentual_desconto * 100)}% (R$ {valor_desconto:.2f})")
    print(f"Valor total a ser pago: R$ {valor_final:.2f}")

# Ponto de entrada principal do programa
if __name__ == "__main__":
    main()