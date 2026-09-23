# 26. Verificar se o maior inteiro é múltiplo do menor.
# Procedimentos sem parâmetros e variáveis globais.
numero1 = numero2 = maior = menor = 0


def ler_dados():
    global numero1, numero2
    numero1 = int(input("Primeiro inteiro: "))
    numero2 = int(input("Segundo inteiro: "))


def verificar_multiplos():
    global maior, menor
    if numero1 >= numero2:
        maior = numero1
        menor = numero2
    else:
        maior = numero2
        menor = numero1
    # Um múltiplo tem a forma menor * k, com k inteiro.
    # O único múltiplo de zero é o próprio zero.
    if menor == 0:
        if maior == 0:
            print("Zero é múltiplo de zero: 0 = 0 * 1.")
        else:
            print("O maior não é múltiplo do menor (zero).")
    elif maior % menor == 0:
        print("O maior é múltiplo do menor.")
    else:
        print("O maior não é múltiplo do menor.")


def main():
    ler_dados()
    verificar_multiplos()


if __name__ == "__main__":
    main()
