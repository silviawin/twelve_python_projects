import random
import string
from Words import words

# the first step is that the computer has to figure out a word for us to guess
# let´s randomly select a word from the list, and exclude the one´s with a complicate format

def palavra_valida(words):
    palavra = random.choice(words)
    while '-' in palavra or ' ' in palavra:
        palavra = random.choice(words)
    return palavra.upper()

def hangman():
    palavra = palavra_valida(words)
    salva_letras = set(palavra)
    alfabeto = set(string.ascii_uppercase)
    letras_ja_escolhidas = set()

    vidas = 6

# a condição a ser satisfeita pra quando o user acertar todas as letras
# na palavra é quando o len da salva-letras for 0
    while len(salva_letras) > 0 and vidas > 0:
        # a cada interação falar pro user o que ja foi usado:
        print('You have ', vidas, 'left. Letras já usadas: ', ' '.join(letras_ja_escolhidas))
        # dizer pro user como a palavra esta ( W - R D)
        lista_de_palavras = [letra if letra in letras_ja_escolhidas else '-' for letra in palavra]
        print('Palavra atual: ', ' ' .join(lista_de_palavras) )

        escolhendo_letra = input("Escolha uma letra: ").upper()
        if escolhendo_letra in alfabeto - letras_ja_escolhidas:
            letras_ja_escolhidas.add(escolhendo_letra)
            if escolhendo_letra in salva_letras:
                salva_letras.remove(escolhendo_letra)

            else:
                vidas = vidas - 1
                print('Essa letra não está na palavra secreta')

        elif escolhendo_letra in letras_ja_escolhidas:
            print('Essa letra já foi. Escolhe outra')

        else:
            print('Caractere invalido')

    # gets here when len(salva-letras) == 0 OR quando vidas = 0
    if vidas == 0:
        print('Não era essa. A palavra é:', palavra)
    else:
        print('Palavra correta yeeee', palavra)

hangman()
#user_input = input("Escreve: ")
#print(user_input)






