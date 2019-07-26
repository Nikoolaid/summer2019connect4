import numpy as np
import turtle

#board is 800x900 px
#board is 6 rows by 7 columns

###################################################################

count = 0
game_over = False
turn = 0
selection = 'z'
chosenColumn = 0

openSpaceA = [a1,a2,a3,a4,a5,a6]
openSpaceB = [b1,b2,b3,b4,b5,b6]
openSpaceC = [c1,c2,c3,c4,c5,c6]
openSpaceD = [d1,d2,d3,d4,d5,d6]
openSpaceE = [e1,e2,e3,e4,e5,e6]
openSpaceF = [f1,f2,f3,f4,f5,f6]
openSpaceG = [g1,g2,g3,g4,g5,g6]

opena = [1,2,3,4,5,6]
openb = [1,2,3,4,5,6]
openc = [1,2,3,4,5,6]
opend = [1,2,3,4,5,6]
opene = [1,2,3,4,5,6]
openf = [1,2,3,4,5,6]
openg = [1,2,3,4,5,6]

'''
lista = [0:6]
listb = [6:12]
listc = [12:18]
listd = [18:24]
listee = [24:30]
listf = [30:36]
listg = [36:42]
'''
##################################################################
def get
    while not game_over:
        if (turn == 0):
            #selection = (input("player 1 choose column(a-g)"))
            selection = KATRIUANASFUNCTION
            magic()
            
        elif (turn == 1):
            #selection = (input("player 2 choose column(a-g)"))
            magic()
            
        turn += 1
        turn = turn%2
    
##################################################################
#delete the item in list after it's filled
#returns variable a1, a2, d1 etc

def magic(selection):
    if (selection == 'a'):
        returnFirstCircName()
        opena.pop(0)
        
    elif (selection == 'b'):
        returnFirstCircName()
        openb.pop(0)
        
    elif (selection == 'c'):
        returnFirstCircName()
        openc.pop(0)
        
    elif (selection == 'd'):
        returnFirstCircName()
        opend.pop(0)
        
    elif (selection == 'e'):
        returnFirstCircName()
        opene.pop(0)
        
    elif (selection == 'f'):
        returnFirstCircName()
        openf.pop(0)
        
    elif (selection == 'g'):
        returnFirstCircName()
        openg.pop(0)

##################################################################
def returnFirstCircName(selection): 
    if (selection == 'a'):
        first = (opena[0] - 1)
        return openSpaceA[first]
    elif (selection == 'b'):
        first = (openb[0] - 1)
        return openSpaceB[first]
    elif (selection == 'c'):
        first = (openc[0] - 1)
        return openSpaceC[first]
    elif (selection == 'd'):
        first = (opend[0] - 1)
        return openSpaceD[first]
    elif (selection == 'e'):
        first = (opene[0] - 1)
        return openSpaceE[first]
    elif (selection == 'f'):
        first = (openf[0] - 1)
        return openSpaceF[first]
    elif (selection == 'g'):
        first = (openg[0] - 1)
        return openSpaceG[first]
    
        
###################################################################
#get circle name of first open circle in chosen column
#take selection and check if row is filled
#if not filled, get first available space in selection column

'''def getCircle():
    if columnIsOpen():
       return (firstOpenSpace(('open' + selection)))
    else:
        play()
    
def firstOpenSpace(liste):
    return (liste[0])
        

def columnIsOpen(liste):
    count = liste.count(selection + '6')
    if (count == 0):
        return False
    else:
        return True'''
        

###################################################################
#translate the column letters to numbers for alayna
def translateToLetters(selection):
    if (selection == 'a'):
        return 1
    elif(selection == 'b'):
        chosenColumn = '2'
    elif(selection == 'c'):
        chosenColumn = '3'
    elif(selection == 'd'):
        chosenColumn = '4'
    elif(selection == 'e'):
        chosenColumn = '5'
    elif(selection == 'f'):
        chosenColumn = '6'
    elif(selection == 'g'):
        chosenColumn = '7'
    else:
        print ("error")
    print ("Column " + chosenColumn + " chosen")
    



    
