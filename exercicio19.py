# 19. Receber dois valores reais e mostrar o maior.
# Procedimentos sem parâmetros e variáveis globais.
numero1 = numero2 = 0.0


def ler_dados():
    global numero1, numero2
    numero1 = float(input("Primeiro valor: "))
    numero2 = float(input("Segundo valor: "))


def mostrar_maior():
    if numero1 > numero2:
        print("Maior valor:", numero1)
    elif numero2 > numero1:
        print("Maior valor:", numero2)
    else:
        print("Os valores são iguais:", numero1)


def main():
    ler_dados()
    mostrar_maior()


if __name__ == "__main__":
    main()
