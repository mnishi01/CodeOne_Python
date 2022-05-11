# > LET´S CODE - CODE ONE
# > Laços de Repetição - While

# Exemplo 01
numero_sorteado = 15
numero_escolhido = int(input('Informe um número entre 1 e 20: '))

while (numero_escolhido != numero_sorteado):
    print('Você errou! Tente novamente: ')
    numero_escolhido = int(input('Informe um número entre 1 e 20: '))

print('Parabéns, você acertou!')

# Exemplo 02
contador = 0

while (contador < 5):
    print('Contador =', contador)
    contador = contador + 1
