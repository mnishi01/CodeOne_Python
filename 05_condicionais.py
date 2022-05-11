# > LET´S CODE - CODE ONE
# > Estruturas Condicionais

# EXEMPLO 01
idade = 18

if (idade >= 18):
    print('Você é maior de idade.')
else:
    print('Você é menor de idade.')

# EXEMPLO 02
media = float(input('Informe a média do estudante: '))
if(media >= 7):
    print('Você foi aprovado(a).')
elif (media >= 5):
    print('Recuperação')
else:
    print('Você foi reprovado(a).')

# EXEMPLO 03
media = 10
presenca = 60

if ((media >= 7) and (presenca >= 70)):
    print('Aprovado(a)')
else:
    print('Reprovado(a)')
