# Teste Jason
#file = open("intro-python/parsing-json/pep20.txt", mode="r")
'''file = open("pep20.txt", mode="r")
file_contents = file.read()
print (file_contents)
file.close()'''
print ("-"*50)
with open ("pep20.txt", mode="r") as file:
    file_contents = file.read()
    print(file_contents)

with open ("teste.txt", mode="a") as file2:
   file2.write("Iniciando texto\n")

with open("teste.txt", mode="r") as file3:
    file_c3 = file3.read()
    print(file_c3)


