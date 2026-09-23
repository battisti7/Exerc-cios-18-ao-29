# 27. Calcular a velocidade média em km/h de um circuito.
# Procedimento com parâmetros, variáveis locais e sem retorno de valor.


def calcular_e_mostrar_velocidade(voltas, extensao, tempo):
    if voltas < 0 or extensao <= 0 or tempo <= 0:
        print("Use voltas não negativas, extensão e tempo positivos.")
    else:
        distancia_km = voltas * extensao / 1000
        tempo_horas = tempo / 60
        velocidade = distancia_km / tempo_horas
        print(f"Velocidade média: {velocidade:.2f} km/h")


def main():
    voltas = int(input("Número de voltas: "))
    extensao = float(input("Extensão do circuito em metros: "))
    tempo = float(input("Duração em minutos: "))
    calcular_e_mostrar_velocidade(voltas, extensao, tempo)


if __name__ == "__main__":
    main()
