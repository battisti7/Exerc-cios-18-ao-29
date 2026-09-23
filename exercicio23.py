# 23. Receber três valores em ordem crescente e inserir um quarto na ordem.
# Procedimentos sem parâmetros e variáveis globais.
valor1 = valor2 = valor3 = valor4 = 0.0


def ler_dados():
    global valor1, valor2, valor3, valor4
    valor1 = float(input("Primeiro valor: "))
    valor2 = float(input("Segundo valor (maior ou igual ao primeiro): "))
    while valor2 < valor1:
        valor2 = float(input("Digite um valor maior ou igual ao primeiro: "))
    valor3 = float(input("Terceiro valor (maior ou igual ao segundo): "))
    while valor3 < valor2:
        valor3 = float(input("Digite um valor maior ou igual ao segundo: "))
    valor4 = float(input("Quarto valor: "))


def mostrar_ordem():
    if valor4 <= valor1:
        print("Ordem crescente:", valor4, valor1, valor2, valor3)
    elif valor4 <= valor2:
        print("Ordem crescente:", valor1, valor4, valor2, valor3)
    elif valor4 <= valor3:
        print("Ordem crescente:", valor1, valor2, valor4, valor3)
    else:
        print("Ordem crescente:", valor1, valor2, valor3, valor4)


def main():
    ler_dados()
    mostrar_ordem()


if __name__ == "__main__":
    main()
