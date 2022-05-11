# > LET´S CODE - CODE ONE
# > Funções

# Primeiro Exemplo
def saudacao():
    print('Seja bem-vindo(a)!')
    print('Olá, é um prazer ter você fazendo parte desse curso!')

saudacao()

# Segundo Exemplo
def saudacao(nome, curso):
    print(f'Seja bem-vindo(a), {nome}!')
    print(f'Olá, é um prazer ter você fazendo parte do curso de {curso}!')

saudacao('José', 'Python')
saudacao('Aline', 'Java Script')

# Terceiro Exemplo
def saudacao(nome, curso="Python"):
    print(f'Seja bem-vindo(a), {nome}!')
    print(f'Olá, é um prazer ter você fazendo parte do curso de {curso}!')

saudacao('José')
saudacao('Aline', 'Java Script')

# Quarto Exemplo
def soma(num1, num2):
    return num1 + num2

resultado = soma(10,2)
print('O resultado da soma é:', resultado)

# Quinto Exemplo
def calculadora(num1, num2, operacao='+'):
    if(operacao=='+'):
        return num1 + num2
    elif (operacao == '-'):
        return num1 - num2

resultado = calculadora(10, 20, '+') 
print('O resultado da soma é:', resultado)
resultado = calculadora(10, 20, '-') 
print('O resultado da diferença é:', resultado)
