def Leer_Numero_Natural():
    while True:
        try:
            numero = int(input("Ingrese un número natural: "))
            if numero <= 0:
                raise ValueError("El número debe ser natural (mayor que cero).")

            return numero
        except ValueError as e:
            print(f"Error: {e}. Intente de nuevo.")


def Calcular_Divisores(numero):

    divisores = [i for i in range(1, numero + 1) if numero % i == 0]
    return divisores


def main():
    numero = Leer_Numero_Natural()

    divisores = Calcular_Divisores(numero)

    print(f"Todos los divisores de {numero} son: {divisores}")

if __name__ == "__main__":
    main()
