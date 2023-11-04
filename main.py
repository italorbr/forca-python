import random
import time
from palavras import palavras

palavra_secreta = random.choice(palavras)
display = []
op = 0
tentativas = 0
letras = []

while op != 'S':
    print("\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
    print("welcome to jogo da forca modafocka")
    print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
    print("\nGostaria de jogar? S / N")
    op = input("Enquanto vc nao quiser eu vou continuar perguntando ^^ entao aceita logo: ").upper()
    if op != 'S' and op != 'N':
        print("\nNao adianta tentar digitar qualquer outra coisa suas opcoes sao(S/N) aceitar jogar ou responder nao pra sempre :p")
        time.sleep(1)
       

print("\nBeleza! Fico feliz que tenha concordado espontaneamene em participar!")
time.sleep(1)

print("\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
print("***CASO NAO SAIBA TOMA AS REGRAS***")
print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
print("\n1 - Voce tera um numero limitado de tentativas para as letras(5) mais o chute da palavra completa ao final")
print("2 - Voce nao podera chutar a mesma letra mais de uma vez(seria burrice)")
print("3 - A palavra tem o numero de letras exatamente igual ao numero de underscores(_) que aparecerao na tela")
print("4 - Voce so pode tentar adivinhar a palavra quando acavarem suas tentativas")
print("5 - As palavras nao terao acentuacao")
time.sleep(2)

print("\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
print("***ENTENDIDAS AS REGRAS VAMOS AO JOGO***")
print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")

for i in palavra_secreta:
    display.append("_")

print(palavra_secreta)
for i in range(len(display)):
    print(display[i], end="  ")
    i +=1
    
while tentativas < 5:
    x = input("\nVamos la diga uma letra: ")
    if x in letras:
        print("\nEssa voce ja tentou! A tentativa sera desconsiderada.\n")
    else:    
        letras.append(x)
    
    for i in range(len(palavra_secreta)):
        if x == palavra_secreta[i]:
            display[i] = x
    
    for i in range(len(display)):
        print(display[i], end="  ")
        
    tentativas +=1
    
print("Acabaram suas tentativas, vamos para o chute final!!")
final = input("Qual vc pensa ser a palavra secreta? ")

if final == palavra_secreta:
    print("acertou")
else:
    print("errou")