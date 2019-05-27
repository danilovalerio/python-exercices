a = "João"
b = "Maria"
concatenar = a + " " + b

#print(concatenar)

#exibir nome a na vertical
# for i in a:
#     print(i)

#exibir intervalo de concatenar
#print(concatenar[2:9])

#como String em python também é um objeto podemos utilizar seus métodos

print(concatenar) #String concatenada normal
print(concatenar.lower()) #lower minúsculo
print(concatenar.upper()) #upper maiusculo

a = a + " "
print(a + b)
print(a.strip() + b) #strip remove o espaço no final da String

frase = "O rato roeu a roupa do rei de roma"
lista = frase.split(" ") #reparte (corta) aonde tem espaço e guarda no array lista
print(lista[1])

print(frase.find("rei")) #busca a posição do item na string

print(frase[23:]) #exibir conteúdo da busca em diante
print(frase[frase.find("rei"):]) #outra forma de fazer a mesma busca

print(frase.replace("o rei","a rainha"))
print(frase.replace("O rato","o gato"))


