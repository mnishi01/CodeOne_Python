# > LET´S CODE - CODE ONE
# > Estrutura de Listas 

# > Listas
notas = [7.9, 9.7, 8.2]

# Criando listas
lista = []
lista = list()

lista = [26, 'Marcelo', 3.14159, True]
lista_de_listas = [10, [1, 2, 3] ]

# Indexação e Slices (fatiamento)
lista = [26, 'Marcelo', 3.14159, True]
print(lista[0])
print(lista[1])
print(lista[2])
print(lista[3])

print(lista[-1])
print(lista[-2])
print(lista[-3])
print(lista[-4])

# Slices
lista = [10, 50, 30, 40, 25, 60, 5]
print(lista[0:3])
print(lista[3:6])
print(lista[2:])
print(lista[2:6:2])

# Iterações com FOR 01
for elemento in lista:
    print (elemento)

# Iterações com FOR 02
print('Comprimento da lista:', len(lista))
for i in range(len(lista)):
    print(i, " - ", lista[i])

# Métodos e Funções de Listas
lista = [1, 3, 12, 8, 2]
print('Lista Original:', lista)

# append: sempre no final
lista.append(3)
print('Depois do append:', lista)

# insert: você indica onde (índice, valor)
lista.insert(2, 10)
print('Depois do insert:', lista)

# extend: junta duas listas, no final
lista2 = [1, 2, 3]
lista.extend(lista2)
print('Depois do extend:', lista)

# pop: remove o último quando não tem parâmetro
lista.pop()
print('Depois do pop:', lista)

# pop: remove o elemento do índice passado como parâmetro
lista.pop(0)
print('Depois do pop:', lista)

# remove: remove o primeiro elemento encontrado passado como parâmetro
lista.remove(3)
print('Depois do remove:', lista)

# count: conta quantos vezes o elemento passado como parâmetro
print('Quantos 2 existem na lista:', lista.count(2))

# index: informa o índice do elemento passado como parâmetro
print('Índice do elemento 12:', lista.index(12))

# sort: ordena a lista
lista.sort()
print('Lista ordenada:', lista)

lista.sort(reverse=True)
print('Lista ordenada decrescente:', lista)

# Funções de listas

# len
print('Tamanho da lista:', len(lista))

# sum
print('Soma dos elementos da lista:', sum(lista))

# max
print('Maior elemento da lista:', max(lista))

# min
print('Menor elemento da lista:', min(lista))
