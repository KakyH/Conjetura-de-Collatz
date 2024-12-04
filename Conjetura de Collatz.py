def collatz_sequence(n):
    """
    Genera la secuencia de Collatz para un número dado.
    :param n: Número inicial de la secuencia.
    :return: Lista con la secuencia de Collatz.
    """
    if n <= 0:
        raise ValueError("El número debe ser mayor que cero.")
    
    sequence = [n]
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        sequence.append(n)
    return sequence

def main():
    try:
        num = int(input("Introduce un número entero positivo: "))
        sequence = collatz_sequence(num)
        print(f"Secuencia de Collatz: {sequence}")
        print(f"Número de pasos: {len(sequence) - 1}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
