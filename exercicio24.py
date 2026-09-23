# 24. Verificar se um inteiro é divisível por 2 e por 3 simultaneamente.
# Procedimentos sem parâmetros e variáveis globais.
numero = 0


def ler_dados():
    global numero
    numero = int(input("Digite um inteiro: "))


def verificar_divisibilidade():
    if numero % 2 == 0 and numero % 3 == 0:
        print("É divisível por 2 e por 3.")
    else:
        print("Não é divisível por 2 e por 3 simultaneamente.")


def main():
    ler_dados()
    verificar_divisibilidade()


if __name__ == "__main__":
    main()
