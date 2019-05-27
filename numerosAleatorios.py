import random
#random.seed(2) #para fixar um número gerado (inútil)
numAleatorio = random.randint(0,10)
print(numAleatorio)

#escolher aleatoriamente com base numa lista com método choice 
sorteio = ["João","Maria","Enzo","Valentina"]
print(random.choice(sorteio))