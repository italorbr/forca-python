import random
import time
from palavras import *

palavra_secreta = random.choice(palavras).upper()
display = []
op = 0
tentativas = 0
letras = []

while op != 'S':
    print("\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
    print("***BEM VINDO AO JOGO DA FORCA!***")
    print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
    print("\nGostaria de jogar? S / N")
    op = input("Enquanto você não quiser eu vou continuar perguntando: ").upper()
    if op != 'S' and op != 'N':
        print("\nNão adianta tentar digitar qualquer outra coisa, suas opções são(S/N) aceitar jogar ou responder não pra sempre")
        time.sleep(1)
       

print("\nBeleza! Fico feliz que tenha concordado em participar!")
time.sleep(1)

print("\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
print("***CASO NAO SAIBA AS REGRAS SÃO***")
print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
print("\n1 - Você terá um número limitado de tentativas para as letras(7) mais o chute da palavra completa no final.")
print("2 - Você não poderá chutar a mesma letra mais de uma vez(seria burrice)")
print("3 - A palavra tem o número de letras exatamente igual ao número de underscores(_) que aparecerão na tela")
print("4 - Você só pode tentar adivinhar a palavra quando acabarem suas tentativas")
print("5 - As palavras não terão acentuação")
time.sleep(1)

print("\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
print("***ENTENDIDAS AS REGRAS VAMOS AO JOGO***")
print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")

print("===============")
print("||")
print("||")
print("||")
print("||")
print("||")
print("||")
print("||", end="   ")
for i in range(len(palavra_secreta)):
    display.append("_")
    print(display[i], end="  ")
    
while tentativas < 7:
    x = input("\n\nVamos lá diga uma letra: ").upper()
    if x in alfabeto:
        if x in letras:
            print("\nEssa você já tentou! A tentativa sera desconsiderada.\n")
        else:    
            letras.append(x)
        if x in palavra_secreta:
            print("\nÉ isso ai!! a letra", x, "está na nossa palavra secreta continue assim!\n")
            for i in range(len(palavra_secreta)):
                if x == palavra_secreta[i]:
                    display[i] = x
                print(display[i], end="  ")
        else:
            print("\nEssa letra não está na nossa palavra secreta, mas bola pra frente erros acontecem")
            
        tentativas +=1
    else:
        print("\nDigite apenas uma letra e sem acentos, simbolos etc")
        
print("\nAcabaram suas tentativas, vamos para o chute final!!")
final = input("\n\nQual vc pensa ser a palavra secreta? ").upper()

if final == palavra_secreta:
    print("\nAcertou")
else:
    print("\nErrou!! A palavra era: ", palavra_secreta)
