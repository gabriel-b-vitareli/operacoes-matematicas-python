from fractions import Fraction

dividendo = int(input('Digite o valor do dividendo: '))
divisor = int(input('Digite o valor do divisor: '))

div_int = dividendo // divisor
rest_div = dividendo % divisor
fracao = Fraction(rest_div, divisor)

print(f'O valor é {div_int} {fracao}')
