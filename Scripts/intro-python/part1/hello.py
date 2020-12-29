"""Run a Python script from the Terminal by passing it to the Interpreter."""

print("Hello Python!!  ...at least I didn't say World.")
#nome = input("Qual seu nome?... ")
#idade = input ("Qual sua idade? ...")
#print (f"Olá, meu nome é {nome.capitalize()} , e tenho {idade} anos")

funcao = input ("Qual função deseja pesquisar?!")
subitens = dir (funcao)
a = len(subitens)
#print (str(a))
print ("~"*50)
print (f"Abaixo a relação dos subitens da função {funcao}")
print ("~"*50)
for i in subitens:
    print(i)
print("="*50)
print (f"A função {funcao} tem {a} subitens")