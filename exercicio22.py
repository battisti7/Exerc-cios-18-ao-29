# 22. Mostrar dois inteiros diferentes em ordem crescente.
# Procedimentos sem parâmetros e variáveis globais.
numero1 = numero2 = 0


def ler_dados():
    global numero1, numero2
    numero1 = int(input("Primeiro inteiro: "))
    numero2 = int(input("Segundo inteiro, diferente do primeiro: "))
    while numero2 == numero1:
        numero2 = int(input("Os valores devem ser diferentes. Digite novamente: "))


def mostrar_ordem():
    if numero1 < numero2:
        print("Ordem crescente:", numero1, numero2)
    else:
        print("Ordem crescente:", numero2, numero1)


def main():
    ler_dados()
    mostrar_ordem()


if __name__ == "__main__":
    main()
