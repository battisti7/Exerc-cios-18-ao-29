# 20. Verificar e calcular as raízes reais de A*x² + B*x + C = 0.
# Procedimentos sem parâmetros e variáveis globais.
a = b = c = delta = x1 = x2 = 0.0


def ler_dados():
    global a, b, c
    a = float(input("Coeficiente A: "))
    b = float(input("Coeficiente B: "))
    c = float(input("Coeficiente C: "))


def calcular_e_mostrar():
    global delta, x1, x2
    if a == 0:
        print("A deve ser diferente de zero para uma equação do 2º grau.")
    else:
        delta = b ** 2 - 4 * a * c
        if delta < 0:
            print("A equação não possui raízes reais.")
        elif delta == 0:
            x1 = -b / (2 * a)
            print("A equação possui duas raízes reais iguais:", x1)
        else:
            x1 = (-b + delta ** 0.5) / (2 * a)
            x2 = (-b - delta ** 0.5) / (2 * a)
            print("Raiz 1:", x1)
            print("Raiz 2:", x2)


def main():
    ler_dados()
    calcular_e_mostrar()


if __name__ == "__main__":
    main()
