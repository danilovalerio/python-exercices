#manipulação do objeto
list1 = [1,2,3,4,5,6]
list2 = ["abacaxi","melância","abacate","limão"]
list3 = [0,"ola","biscoito","bolacha","pudim",True]

# #precorrer a lista 2
# for item in list2:
#     print(item)

# #exbir pares da lista 1
# for item in list1:
#     if(item % 2 == 0):
#         print(item)

# #exbir ímpares da lista 1
# for item in list1:
#     if(item % 2 == 1):
#         print(item)

#tamanho da lista
print(len(list2))

#add item na lista
list2.append("maracujá")
print(len(list2))

#in para verificar se tem o item na lista
if 6 in list1:
    print("6 está na lista 1")

#apagar item na lista
del list2[2:] #remove a partir do item  na posição 2
print("Itens na lista:",list2)

#ordenação da lista
listDesordem = [8,7,1,2,3,4,5,6,10,12,11]
print(listDesordem)
listDesordem.sort()
print(listDesordem)
listDesordem.sort(reverse=True)
print(listDesordem)
listDesordem.reverse()
print(listDesordem)

#Retorno de uma lista ordenada
print("Retorno de lista:")
listDesordem = [8,7,1,2,3,4,5,6,10,12,11]
listOrdenada = sorted(listDesordem) 
print(listDesordem)
print(listOrdenada)

