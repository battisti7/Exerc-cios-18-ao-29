# 18. Mostrar a diferença do maior inteiro pelo menor.
# Procedimentos sem parâmetros e variáveis globais.
numero1 = numero2 = diferenca = 0


def ler_dados():
    global numero1, numero2
    numero1 = int(input("Primeiro inteiro: "))
    numero2 = int(input("Segundo inteiro: "))


def calcular_e_mostrar():
    global diferenca
    if numero1 >= numero2:
        diferenca = numero1 - numero2
    else:
        diferenca = numero2 - numero1
    print("Diferença:", diferenca)


def main():
    ler_dados()
    calcular_e_mostrar()


if __name__ == "__main__":
    main()
