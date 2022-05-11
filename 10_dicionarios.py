# > LET´S CODE - CODE ONE
# # > Dicionários

# Criando dicionários
dicionario = {}
dicionario = dict()

dicionario = { 'nome': 'Marcelo', 'idade': 26, 'altura': 1.77}
print(dicionario)
print('Idade:', dicionario['idade'])


# Adicionando elementos no dicionário

dicionario['programador'] = True
print(dicionario)

dicionario['altura'] = 2
print(dicionario)


# Percorrer dicionário
for chave in dicionario:
    print(chave, dicionario[chave])


# Testar a existência de uma chave no dicionário
print('peso' in dicionario)
print('altura' in dicionario)
