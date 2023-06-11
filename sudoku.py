import math
import random

#checa se o mesmo numero na linha
def checar_horizontal(x,num):
    possui= False
    for y in range(linhas*3):
        if(sudoko[x][y]==num):
            possui=True
            return possui
            break
    return possui



#checa se o mesmo numero nas colunas
def checar_vertical(y,num):
    possui = False
    for x in range(colunas*3):
        if (sudoko[x][y] == num):
            possui = True
            return possui
    return possui
#verifica se a o numero na regiao 3 por 3
def checar_tpt(x,y,num):
    posx = math.floor(x/3)*3
    posy = math.floor(y/3)*3
    possui= False
    for x in range(3):
        for y in range(3):
            if(sudoko[posx+x][posy+y]==num):
                possui=True
                return possui
    return possui


def checar_tudo(x,y,num):
    if(imutaveis[x][y]!=1):
      return (checar_vertical(y,num) or checar_horizontal(x,num) or checar_tpt(x,y,num) )
    else:
      return false
 #Matriz do suko
 sudoku=[]
 #matriz com numero pre-preenchidos
 imutaveis=[[]]
 #Preenche uma matriz com 0
 #Os espacos livres sao definidos pelo 0
def criar_sudoku(lin,col):
    for x in range(lin*3):
        coluna=[]
        for y in range(col*3):
            coluna.append(0)
        sudoko.append(coluna)

#Preenche o sudoku com numeros aleatorios
def preencher_aleatorio(num):
    while(num>0):
        x_ale=  random.randint(1,colunas*3)-1
        y_ale= random.randint(1,linhas*3)-1
        if(sudoko[x_ale][y_ale]==0):
            num_al=random.randint(1,9)
            if(checar_tudo(x_ale,y_ale,num_al)==False):
                num -= 1
                sudoko[x_ale][y_ale]= num_al
                imutaveis[x_ale][y_ale]=1

#O usuario passara a posicao x,y e tambem o numero que deseja colocar no sudoku
#Esses serao colocar nesse modelo (x,y,num)
#O usuario pode passar varios desses inputs simultaneamente para preencher varios espacos 
#Seguindo este modelo (x,y,num) (x2,y2,num2) (x3,y3,num3)
def  parse_input(input_usuario):
    conjutoValores = []
    conjutos=0
    # parenteses esquerdo e direito
    PosPE=[]
    PosPD=[]
    count=0
    #Define o primeiro conjunto de parenteses
    for x in input_usuario:
        if (x == "("):
            conjutos+=1
            PosPE.append(count)
        if( x ==")"):
            PosPD.append(count)
        count+=1

    countconj=1
    
    
    while(countconj<=conjutos):
            if(count!=conjutos):
                conjutoAtual= input_usuario[PosPE[countconj-1]:PosPD[countconj-1]+1]
            else:
                conjutoAtual=input_usuario[PosPE[countconj-1]:]


            posvirgulas=[]
            posparenteses=[]
            count=0

            for x in conjutoAtual:
                if(x=="(" or x==")"):
                    posparenteses.append(int(count))
                if(x==","):
                    posvirgulas.append(int(count))
                count+=1
            lin=int (conjutoAtual[posparenteses[0]+1:posvirgulas[0]])
            col=int (conjutoAtual[posvirgulas[0]+1:posvirgulas[1]])
            num=int (conjutoAtual[posvirgulas[1]+1: posparenteses[1]])
            valores=[lin,col,num]
            conjutoValores.append(valores)
            countconj+=1
    return  conjutoValores
  
  
#O usuario passara a posicao x,y e a funcao ira colocar o numero 0
#Esses serao colocar nesse modelo (x,y)
#O usuario pode passar varios desses inputs simultaneamente para preencher varios espacos 
#Seguindo este modelo (x,y,num) (x2,y2,num2) (x3,y3)
def  parse_input_del(input_usuario):
    conjutoValores = []
    conjutos=0
    # parenteses esquerdo e direito
    PosPE=[]
    PosPD=[]
    count=0
    #Define o primeiro conjunto
    for x in input_usuario:
        if (x == "("):
            conjutos+=1
            PosPE.append(count)
        if( x ==")"):
            PosPD.append(count)
        count+=1

    countconj=1
    #Verifica se a multiplos conjuntos
    while(countconj<=conjutos):
            if(count!=conjutos):
                conjutoAtual= input_usuario[PosPE[countconj-1]:PosPD[countconj-1]+1]
            else:
                conjutoAtual=input_usuario[PosPE[countconj-1]:]


            posvirgulas=[]
            posparenteses=[]
            count=0
            #verifica se ha mais parenteses e virgulas
            for x in conjutoAtual:
                if(x=="(" or x==")"):
                    posparenteses.append(int(count))
                if(x==","):
                    posvirgulas.append(int(count))
                count+=1
            #pega as linhas e define o valor
            lin=int (conjutoAtual[posparenteses[0]+1:posvirgulas[0]])
            col=int (conjutoAtual[posvirgulas[0]+1:])
            if(imutaveis[lin,col]!=1):
              valores=[lin,col,0]
            else:
               valores=[lin,col,sudoku[lin,col]]
            conjutoValores.append(valores)
            countconj+=1
    return  conjutoValores

def printarsudoko():
    for x in range(linhas * 3):
        for y in range(colunas * 3):
            print(sudoko[x][y], end='')
        print()

jogar=True
while(jogar==True):
    
    # definir o numero de linhas e colunascada conjunto 3x3
    linhas,colunas = 4,4

    print("Digite um valor para começar o jogo")
    print("1- Jogo aleatorio")
    print("2- Jogo predefinido")
    tipo_de_jogo= int(input())
    print("Digite a dimensão do sudoko")
    colunas=int(input())
    linhas= colunas
    criar_sudoku(linhas,colunas)
    if(tipo_de_jogo==1):
        print("digite quantidade de numeros ja preenchida")
        num =int(input())
        preencher_aleatorio(num)
    else:
        valores=[1,1,1]
        while valores!=[0, 0, 0]:
            print("digite quantidade de numeros ja preenchida")
            print("digite no formato (lin,col,num")
            print("digite (0,0,0) para terminar")
            input_usu=input()
            Conjuntovalores= parse_input(input_usu)
            for valores in Conjuntovalores:
                if(checar_tudo(valores[0]-1,valores[1]-1,valores[2])==False):
                    sudoko[valores[0]-1][ valores[1]-1]= valores[2]
                elif(input_usu!="(0,0,0"):
                    print("não é possivel colocar o valor")
    ganhou = False
    while(ganhou==False):
        printarsudoko()
        print("1- para colocar valor")
        print("2- para remover")
        print("3- para verificar")
        esco= int(input())
        if(esco==1):
            print("digite os valores a serem colocados")
            input_usu = input()
            Conjuntovalores = parse_input(input_usu)
            for valores in Conjuntovalores:
                if (checar_tudo(valores[0] - 1, valores[1] - 1, valores[2]) == False):
                    sudoko[valores[0] - 1][valores[1] - 1] = valores[2]
                else:
                    print("não é possivel colocar o valor")
        if(esco==2):
            print("digite os valores a serem colocados")
            input_usu = input()
            Conjuntovalores = parse_input_del(input())
            for valores in Conjuntovalores:
                        sudoko[valores[0]-1][valores[1]-1] = valores[2]

        if(esco==3):
          #Verifica se ha algum valor nao preenchido no sudoku
          #caso nao tenha o jogo esta ganho
            ganhou=True
            for x in range(linhas*3):
                    for y in range(colunas*3):
                        if(sudoko[x][y]==0):
                            ganhou=False


    print("PARABENS")


    print("Digite 1 para jogar novamente")
    if(input()!="1"):
        jogar=False
