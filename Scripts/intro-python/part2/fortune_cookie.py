#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Script flow and debugging. Print your own fortune cookie!"""

import random

FORTUNES = [
    "Ha uma boa chance de seu código funcionar, eventualmente.",
    "Vixi seu codigo vai dar problema.",
    "O tempo vai ser quente hoje.",
    "Prepare-se para o frio!!",
    "Vejo um desenvolvedor de rede em seu futuro.",
    "Acho melhor aprender a cozinhar !! kkkk.",
]


def generate_fortune() -> str:
    """Use forças místicas (uma seleção aleatória) para obter a sorte de um usuário.."""
    return random.choice(FORTUNES)


def generate_lucky_numbers(how_many: int) -> list:
    """Retorna uma lista de numeros da 'sorte' (aleatórios)."""

    lucky_numbers = []

    for item in range(how_many):
        lucky_numbers.append(random.randint(0, 99))

    return lucky_numbers


def create_fortune_cookie_message(how_many_lucky_numbers: int) -> str:
    """Crie e retorne uma mensagem de biscoito da sorte.
    A mensagem deve incluir a sorte e os números da sorte do usuário.
    """
    # TODO: Create a fortune cookie message by calling generate_fortune() and
    # generate_lucky_numbers() e então compondo e devolvendo a sorte escolhida
    # messagem do biscoito da sorte.

    Numeros_sorte = generate_lucky_numbers(how_many_lucky_numbers)
    Menssagem_sorte = generate_fortune()
    Msg_Final = (f'{Menssagem_sorte}\nSeus numeros de sorte sao: {Numeros_sorte}')
    return Msg_Final

   # raise NotImplementedError()





def main():
    """Create and print a fortune cookie."""
    print("Pegue seu biscoito da sorte")

    # Prompt the user for how many lucky numbers they would like
    qty_lucky_numbers = input("Quantos numeros da sorte voce quer?  ")
    qty_lucky_numbers = int(qty_lucky_numbers.strip())

    # Crie e exiba sua sorte
    fortune_cookie_message = create_fortune_cookie_message(qty_lucky_numbers)
    print("\nAqui esta a sua sorte:\n")
    print(fortune_cookie_message)


if __name__ == '__main__':
    main()

#  ---- Meu Debug ----
#   escolhido = random.choice(FORTUNES)
#    print(escolhido)
#    a = input("Estou aguardando ....")
#    random.choice(FORTUNES)
# print(type(how_many_lucky_numbers),type(how_many_lucky_numbers))
#    print(type(how_many),type(how_many))
#    a = input(how_many_lucky_numbers)
