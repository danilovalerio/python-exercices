#LEITURA DE ARQUIVO 
#----------------------

arquivo = open("arquivo.txt") #abertura do arquivo

#lê as linhas do arquivo
#--------------------------------
# linhas = arquivo.readlines() 
# print(linhas)
# for linha in linhas:
#     print(linha)

#lê todo o conteúdo do arquivo
#--------------------------------
texto_completo = arquivo.read() 
print("Teste",texto_completo)

