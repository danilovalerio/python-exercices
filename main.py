#modularização 
#---Arquivos importados (módulos) são os que compõem esse programa---#
import media as m
import aleatorio as a

lista = a.geraListaInteiros(10)
print(lista)

media = m.media(lista)
mediana = m.mediana(lista)
moda = m.moda(lista)

print("A média da minha lista é "+str(media))
print("A médiana da minha lista é "+str(mediana))
print("A moda da minha lista é "+str(moda))

