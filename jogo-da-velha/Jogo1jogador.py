import os
import random
from colorama import Fore, Back, Style

jogarnovamente = "s"
jogadas = 0
quemjoga = 2 #1=cpu - 2=jogador
maxjogadas = 9
vit = "false"
velha = [  
    ["  ","  ","  "],
    ["  ","  ","  "],
    ["  ","  ","  "]
]

def tela():
    global velha 
    os.system('cls')
    print("     0     1    2")
    print("0:  " + velha[0][0] + "  | " + velha [0][1] + "  | " + velha [0][2])
    print("    ---------------")
    print("1:  " + velha[1][0] + "  | " + velha [1][1] + "  | " + velha [1][2])
    print("    ---------------")
    print("2:  " + velha[2][0] + "  | " + velha [2][1] + "  | " + velha [2][2])
    print("jogadas: " + Fore.GREEN + str(jogadas) + Fore.RESET)

def jogadorjoga():
    global jogadas
    global quemjoga
    global maxjogadas

    if quemjoga == 2 and jogadas < maxjogadas:
        try:
            linha = int(input('Linha..= '))
            coluna = int(input('Coluna..= '))
            while velha[linha][coluna] != "  ":
                linha = int(input('Linha..= '))
                coluna = int(input('Coluna..= '))
            velha[linha][coluna]=" X"
            quemjoga = 1
            jogadas += 1
        except:
            print("Jogada invalida") 
            os.system("pause")


def cpujoga():
    global jogadas
    global quemjoga
    global vit
    global maxjogadas

    if quemjoga == 1 and jogadas < maxjogadas:
        linha = random.randrange(0,3)
        coluna = random.randrange(0,3)
        while velha[linha][coluna] != "  ":
            linha = random.randrange(0,3)
            coluna = random.randrange(0,3)
        velha[linha][coluna] = " O"
        jogadas +=1
        quemjoga = 2

def verificarvitoria():
    global velha
    vitoria = "n"
    simbolos = [" X"," O"]
    for s in simbolos:
        vitoria = "n"
        
        
        #vitoria em linha
        il=ic=0
        while il < 3:
            soma = 0
            ic = 0
            while ic < 3:
                if(velha[il][ic]==s):
                    soma +=1
                ic+=1
            if(soma==3):
                vitoria=s
                break
            il +=1
        if(vitoria!="n"):
            break
        
        
        #vitoria em coluna
        il=ic=0
        while ic < 3:
            soma = 0
            il = 0
            while il < 3:
                if(velha[il][ic]==s):
                    soma +=1
                il+=1
            if(soma==3):
                vitoria=s
                break
            ic+=1
        if(vitoria!="n"):
            break
        
        
        #vitoria diagonal1
        soma = 0
        idiag = 0
        while idiag < 3:
            if(velha[idiag][idiag]==s):
                soma +=1
            idiag+=1
        if (soma==3):
            vitoria=s
            break
        
        
        #vitoria diagonal2
        soma = 0
        idiagl = 0
        idiagc = 2
        while idiag < 3:
            if(velha[idiagl][idiagc]==s):
                soma +=1
        idiagl += 1
        idiagc -= 1
        if (soma==3):
            vitoria=s
            break
    return vitoria

def redefinir():
    global velha
    global jogadas
    global quemjoga #1=cpu - 2=jogador
    global maxjogadas 
    global vit 
    velha = [  
        ["  ","  ","  "],
        ["  ","  ","  "],
        ["  ","  ","  "]
    ]
while(jogarnovamente=="s"):
    while True:
        tela()
        jogadorjoga()
        cpujoga()
        tela()
        vit = verificarvitoria()
        if(vit!="n")or(jogadas>maxjogadas):
            break

    print(Fore.RED + "FIM DO JOGO" + Fore.YELLOW)
    if (vit == " X" or vit==" O"):
        print("Resultado: Jogador" + vit + " Venceu")
    else:
        print("Resultado: Empate")    
    jogarnovamente = input(Fore.BLUE + "Jogar Novamente? [s/n]: " + Fore.RESET)
    redefinir()

    

