# 28. Calcular o novo preço conforme a venda média mensal e o preço atual.
# As duas condições de cada faixa devem ser atendidas simultaneamente.
# Procedimento com parâmetros, variáveis locais e sem retorno de valor.


def calcular_e_mostrar_preco(preco_atual, venda_mensal):
    if venda_mensal < 500 and preco_atual < 30:
        novo_preco = preco_atual * 1.10
    elif 500 <= venda_mensal < 1000 and 30 <= preco_atual < 80:
        novo_preco = preco_atual * 1.15
    elif venda_mensal >= 1000 and preco_atual >= 80:
        novo_preco = preco_atual * 0.95
    else:
        novo_preco = preco_atual
    print(f"Novo preço: R$ {novo_preco:.2f}")


def main():
    preco_atual = float(input("Preço atual: R$ "))
    venda_mensal = float(input("Média de unidades vendidas por mês: "))
    calcular_e_mostrar_preco(preco_atual, venda_mensal)


if __name__ == "__main__":
    main()
