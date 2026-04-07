from math import atan
pi = atan(1)*4
casas = int(input('Quantas casas decimais você deseja? '))
print(f'O número pi é: {pi:.{casas}f}')
