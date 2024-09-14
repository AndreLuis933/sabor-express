# 1
pessoa = {'nome':'Andre','idade':'18','cidade':'Pimenta Bueno'}


# # 2
# pessoa.update({'idade':20,'proficao':'trabalhador'})
# del pessoa['cidade']
# print(pessoa)

# # 3
# numeros = {1:1*1,2:2*2,3:3*3,4:4*4,5:5*5}
# print(numeros)

# 4 
# itens = {'caneta':'azul','tamanho':2.5,'altura':5}

# if 'caneta' in itens:
#     print('ceu')
# else:
#     print('cor de nada')
         

# numeros_quadrados = {x: x**2 for x in range(1, 6)}
# print(numeros_quadrados)

frase = "Python se tornou uma das linguagens de programação mais populares do mundo nos últimos anos."
contagem_palavras = {}
palavras = frase.split()
for palavra in palavras:
    contagem_palavras[palavra] = contagem_palavras.get(palavra, 0) + 1
print(contagem_palavras)



