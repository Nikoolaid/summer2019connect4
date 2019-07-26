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
openSpaces = [a1,a2,a3,a4,a5,a6,b1,b2,b3,b4,b5,b6,c1,c2,c3,c4,c5,c6,d1,d2,d3,d4,d5,d6,e1,e2,e3,e4,e5,e6,f1,f2,f3,f4,f5,f6,g1,g2,g3,g4,g5,g6]
opena = [1,2,3,4,5,6]
openb = [1,2,3,4,5,6]
openc = [1,2,3,4,5,6]
opend = [1,2,3,4,5,6]
opene = [1,2,3,4,5,6]
openf = [1,2,3,4,5,6]
openg = [1,2,3,4,5,6]

##################################################################
while not game_over:
    if (turn == 0):
        selection = (input("player 1 choose column(a-g)"))
        
        
    elif (turn == 1):
        selection = (input("player 2 choose column(a-g)"))
        
    turn += 1
    turn = turn%2
    
##################################################################
def magic():
    if (selection == 'a'):
        opena.pop(0)
    elif (selection == 'b'):
        openb.pop(0)
    elif (selection == 'c'):
        openc.pop(0)
    elif (selection == 'd'):
        opend.pop(0)
    elif (selection == 'e'):
        opene.pop(0)
    elif (selection == 'f'):
        openf.pop(0)
    elif (selection == 'g'):
        openg.pop(0)
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
'''def translateToLetters(selection):
    if (selection == 'a'):
        chosenColumn = '1'
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
    print ("Column " + chosenColumn + " chosen")'''
    




    
