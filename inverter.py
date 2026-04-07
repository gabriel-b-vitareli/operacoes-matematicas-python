palavra = input('Digite qual palavra inverter: ')
palavraInvertida = palavra[::-1]

print(f'A palavra {palavra} invertida é: {palavraInvertida}')

if palavra.lower() == palavraInvertida.lower():
  print('Essa palavra é um palíndromo.')
