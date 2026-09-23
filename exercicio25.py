# 25. Calcular a duração de um jogo, sempre inferior a 24 horas.
# Horários iguais representam duração zero, pois 24 horas não são permitidas.
# Procedimentos sem parâmetros e variáveis globais.
hora_inicio = minuto_inicio = hora_final = minuto_final = 0
inicio = fim = duracao = horas = minutos = 0


def ler_dados():
    global hora_inicio, minuto_inicio, hora_final, minuto_final
    hora_inicio = int(input("Hora inicial (0 a 23): "))
    minuto_inicio = int(input("Minuto inicial (0 a 59): "))
    hora_final = int(input("Hora final (0 a 23): "))
    minuto_final = int(input("Minuto final (0 a 59): "))


def calcular_e_mostrar():
    global inicio, fim, duracao, horas, minutos
    if (0 <= hora_inicio <= 23 and 0 <= hora_final <= 23
            and 0 <= minuto_inicio <= 59 and 0 <= minuto_final <= 59):
        inicio = hora_inicio * 60 + minuto_inicio
        fim = hora_final * 60 + minuto_final
        if fim < inicio:
            fim = fim + 24 * 60
        duracao = fim - inicio
        horas = duracao // 60
        minutos = duracao % 60
        print(f"Duração: {horas} hora(s) e {minutos} minuto(s).")
    else:
        print("Horário inválido.")


def main():
    ler_dados()
    calcular_e_mostrar()


if __name__ == "__main__":
    main()
