"""Intro to Python - Part 1 - Hands-On Exercise."""

import math
import random

def inicia (titulo, proposta):
    print(f'{"=" * 40}\n{titulo:^40}\n{"=" * 40}')
    print(f'{"-" * 80}\nObjetivo: {proposta}\n\n Resultado: \n')

# ====================== Exercicio 1  ============================================================

# TODO: Write a print statement that displays both the type and value of `pi`

inicia("Exercicio 1", "Escreva uma declaração de impressão que exiba o tipo e o valor de `pi`")

# Executa o exercicio
pi = math.pi
tipo = str(type(pi))
tipok = tipo.split()
print(f"O valor do pi é {pi}, e o seu formato é {tipok[1]}")

print(f'{"-"*80}\n')


# ====================== Exercicio 2  ============================================================

# TODO: Write a conditional to print out if `i` is less than or greater than 50
inicia("Exercicio 2","Escreva uma condição para imprimir se `i` for menor ou maior que 50")
i = random.randint(0, 100)
if i < 50:
    print(f"O valor sorteado foi {i}, menor que 50.")
else:
    print(f"O valor sorteado foi {i}, portanto, maior que 50.")

print(f'{"-"*80}\n')

# ====================== Exercicio 3  ============================================================
inicia ("Exercicio 3","Escreva uma condicional que imprima a cor da fruta colhida")

# TODO: Write a conditional that prints the color of the picked fruit
frutas = ['orange', 'strawberry', 'banana']
cores = ['laranja','vermelha','amarela']
picked_fruit = random.choice(frutas)

for i , v in enumerate(frutas):
     if frutas[i] == picked_fruit:
       print(f'A fruta escolhida foi {picked_fruit} e sua cor é {cores[i]}')

print(f'{"-"*80}\n')

# ====================== Exercicio 4  ============================================================
inicia("Exercicio 4","Escreva uma função que multiplique dois números e retorne o resultado")
# TODO: Write a function that multiplies two numbers and returns the result
# Define the function here.
def mult (n, m):
  p = int(n)*int(m)
  return p

a = input ("Digite um número ---> ")
b = input ("Digite seu multiplicador ---> ")

print (f'\n {a} x {b} = {mult(a,b)}\n')

print(f'{"-"*80}\n')

# ====================== Exercicio 5  ============================================================
# TODO: Now call the function a few times to calculate the following answers
inicia ('Exercicio 5', 'Agora chame a função algumas vezes para calcular as seguintes respostas')
print ('Testando a função com os números abaixo')

print("12 x 96 =",mult(12,96) )

print("48 x 17 =", mult(48,17) )

print("196523 x 87323 =", mult (196523,87323))

print(f'{"-"*80}\n')