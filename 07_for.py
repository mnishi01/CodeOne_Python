# > LET´S CODE - CODE ONE
# > Laços de Repetição - For

# 1 parâmetro
for variavel in range(10):
    print('1 parâmetro - ', variavel)

# 2 parâmetros
for variavel in range(1,11):
    print('2 parâmetros - ', variavel)

# 3 parâmetros
for variavel in range(1,12,3):
    print('3 parâmetros - ', variavel)

# Exemplo
soma = 0
for i in range(1, 4):
    nota = float(input(f'Informe sua nota {i}: '))
    soma = soma + nota
print('A média é: ', soma/3)
