from palavras import *
import random

palavra = random.choice(palavras).lower()
letrasU = []
chances = 7
acertos = 0

print (f'A palavra tem {len(palavra)} Letras. ')
print ('-='*30)

while chances > 0:

    for letra in palavra:
        if letra.lower() in letrasU:
            print(letra, end=' ')
        else:
            print (' _ ', end='')

    print('')
    print ('-='*30)

    #tentativas do usuario
    tentativa = (input("Escolha uma letra: "))
    letrasU.append(tentativa.lower())
    if tentativa.lower() not in palavra.lower():
        chances -= 1
      

    #ganhar ou perder
    
    
    
for letra in palavra:
    if letra.lower() in letrasU:
        acertos += 1
if acertos == (len(palavra)):
    print("ganhou" , palavra)
else:
    print("perdeu a palavra era", palavra)