def divisao(dividendo: float, divisor: float) -> float:
    if divisor == 0:
        raise ValueError("Divisor must be greater than zero.")
    return dividendo / divisor

first_number = int(input('First number: '))
second_number = int(input('Second number: '))

print(divisao(first_number, second_number))