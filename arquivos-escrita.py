#abre o arquivo para escrita e sobrescreve todo conteúdo com o texto
# w = open("arquivo-escrita.txt","w") 

#abre o arquivo para escrita e adiciona texto ao final do conteúdo
w = open("arquivo-escrita.txt","a") 
w.write("Mensagem escrita de teste\n") #escrita
w.close() #fecha escrita de arquivo

