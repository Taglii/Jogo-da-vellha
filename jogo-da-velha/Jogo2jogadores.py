import os
from colorama import Fore, Back, Style


jogarnovamente = "s"
jogadas = 0
quemjoga = 1 #1=jogador1 - 2=jogador2
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

def jogador1_joga():
    global jogadas
    global quemjoga
    global maxjogadas

    if quemjoga == 1 and jogadas < maxjogadas:
        try:
            print("Jogador 1")
            linha = int(input('Jogar na Linha: '))
            coluna = int(input('Jogar na Coluna:' ))
            while velha[linha][coluna] != "  ":
                linha = int(input('Jogar na Linha: '))
                coluna = int(input('Jogar na Coluna:' ))
            velha[linha][coluna] = " X"
            quemjoga = 2
            jogadas += 1
        except:
            print("Jogada invalida") 
            os.system("pause")    

def jogador2_joga():
    global jogadas
    global quemjoga
    global maxjogadas
    
    
    if quemjoga == 2 and jogadas < maxjogadas:
        try:
            print("Jogador 2")
            linha = int(input('Jogar na Linha: '))
            coluna = int(input('Jogar na Coluna:' ))
            while velha[linha][coluna] != "  ":
                linha = int(input('Jogar na Linha: '))
                coluna = int(input('Jogar na Coluna:' ))
            velha[linha][coluna] = " O"
            quemjoga = 1
            jogadas += 1
        except:
            print("Jogada invalida") 
            os.system("pause")  

def verificar_vitoria():
    global velha
    simbolos = [" X", " O"]
    
    # Verifica todas as possibilidades de vitória para cada símbolo
    for s in simbolos:
        # Vitória nas linhas
        for il in range(3):
            if velha[il][0] == s and velha[il][1] == s and velha[il][2] == s:
                return s
        
        # Vitória nas colunas
        for ic in range(3):
            if velha[0][ic] == s and velha[1][ic] == s and velha[2][ic] == s:
                return s
        
        # Vitória na diagonal principal
        if velha[0][0] == s and velha[1][1] == s and velha[2][2] == s:
            return s
        
        # Vitória na diagonal secundária
        if velha[0][2] == s and velha[1][1] == s and velha[2][0] == s:
            return s
    
    # Se não houve vitória
    return "n"

def redefinir():
    global velha
    global jogadas
    global quemjoga #1=jogador1 - 2=jogador2
    global maxjogadas 
    global vit 
    velha = [  
        ["  ","  ","  "],
        ["  ","  ","  "],
        ["  ","  ","  "]
    ]
    jogadas = 0

while(jogarnovamente == "s"):
    while True:
        tela()
        jogador1_joga()
        vit = verificar_vitoria()
        if vit != "n" or jogadas >= maxjogadas:
            break

        tela()
        jogador2_joga()
        vit = verificar_vitoria()
        if vit != "n" or jogadas >= maxjogadas:
            break

    tela()
    print(Fore.RED + "FIM DO JOGO" + Fore.RESET)
    if vit == " X" or vit == " O":
        print("Resultado: Jogador" + (" 1" if vit == " X" else " 2") + " venceu!")
    else:
        print("Resultado: Empate!")
    
    jogarnovamente = input(Fore.BLUE + "Jogar Novamente? [s/n]: " + Fore.RESET)
    redefinir()