# 21. Calcular a média de quatro notas e mostrar a situação do aluno.
# Procedimentos sem parâmetros e variáveis globais.
nota1 = nota2 = nota3 = nota4 = media = 0.0


def ler_dados():
    global nota1, nota2, nota3, nota4
    nota1 = float(input("Primeira nota: "))
    nota2 = float(input("Segunda nota: "))
    nota3 = float(input("Terceira nota: "))
    nota4 = float(input("Quarta nota: "))


def calcular_e_mostrar():
    global media
    media = (nota1 + nota2 + nota3 + nota4) / 4
    print(f"Média: {media:.2f}")
    if media >= 6:
        print("APROVADO")
    elif media >= 3:
        print("EXAME")
    else:
        print("RETIDO")


def main():
    ler_dados()
    calcular_e_mostrar()


if __name__ == "__main__":
    main()
