# 29. Mostrar o investimento corrigido em 30 dias.
# Taxas do enunciado: poupança 3%; renda fixa 5%.
# Procedimento com parâmetros, variáveis locais e sem retorno de valor.


def calcular_e_mostrar_investimento(tipo, valor):
    if tipo == 1:
        valor_corrigido = valor * 1.03
        print(f"Valor corrigido: R$ {valor_corrigido:.2f}")
    elif tipo == 2:
        valor_corrigido = valor * 1.05
        print(f"Valor corrigido: R$ {valor_corrigido:.2f}")
    else:
        print("Tipo de investimento não considerado.")


def main():
    tipo = int(input("Tipo de investimento (1 = poupança, 2 = renda fixa): "))
    valor = float(input("Valor do investimento: R$ "))
    calcular_e_mostrar_investimento(tipo, valor)


if __name__ == "__main__":
    main()
