import turtle
import numpy as np
import wip

#START OF GAME
user = input("Welcome to Connect Four!  You need two players for this game.  Would you like to contine (yes or no)? ")
if (user== "yes"):
        #VARIABLES
        circles = {"a1": (-425, -250), "a2": (-425, -125), "a3": (-425, 0), "a4": (-425, 125), "a5": (-425, 250), "a6": (-425, 375),"b1": (-300, -250), "b2": (-300, -125), "b3": (-300, 0), "b4": (-300, 125), "b5": (-300, 250), "b6": (-300, 375),"c1": (-175, -250), "c2": (-175, -125), "c3": (-175, 0), "c4": (-175, 125), "c5": (-175, 250), "c6": (-175, 375),"d1": (-50, -250), "d2": (-50, -125), "d3": (-50, 0), "d4": (-50, 125), "d5": (-50, 250), "d6": (-50, 375),"e1": (75, -250), "e2": (75, -125), "e3": (75, 0), "e4": (75, 125), "e5": (75, 250), "e6": (75, 375),"f1": (200, -250), "f2": (200, -125), "f3": (200, 0), "f4": (200, 125), "f5": (200, 250), "f6": (200, 375),"g1": (325, -250), "g2": (325, -125), "g3": (325, 0), "g4": (325, 125), "g5": (325, 250), "g6": (325, 375)}
        count = 0
        game_over = False
        turn = 0
        selection = 'z'
        chosenColumn = 0

        openSpaceA = ['a1','a2','a3','a4','a5','a6']
        openSpaceB = ['b1','b2','b3','b4','b5','b6']
        openSpaceC = ['c1','c2','c3','c4','c5','c6']
        openSpaceD = ['d1','d2','d3','d4','d5','d6']
        openSpaceE = ['e1','e2','e3','e4','e5','e6']
        openSpaceF = ['f1','f2','f3','f4','f5','f6']
        openSpaceG = ['g1','g2','g3','g4','g5','g6']

        opena = [1,2,3,4,5,6]
        openb = [1,2,3,4,5,6]
        openc = [1,2,3,4,5,6]
        opend = [1,2,3,4,5,6]
        opene = [1,2,3,4,5,6]
        openf = [1,2,3,4,5,6]
        openg = [1,2,3,4,5,6]

        coordinates = {'1st column': (-490, -362.5), '2nd column' : (-362.5, -237.5), '3rd column': (-237.5, -112.5), '4th column': (-112.5, 12.5), '5th column': (12.5, 137.5), '6th column': (137.5, 262.5), '7th column': (262.5, 387.5)}

        a = coordinates['1st column']
        b = coordinates['2nd column']
        c = coordinates['3rd column']
        d = coordinates['4th column']
        e = coordinates['5th column']
        f = coordinates['6th column']
        g = coordinates['7th column']

        bess = turtle.Turtle()


        #SETUP
        player_1 = str(input("Welcome Player 1! Type in your name: "))
        player_2 = str(input("Welcome Player 2! Type in your name: "))

        choose_color1 = chooseColor(player_1)
        choose_color2 = chooseCOlor(player_2)

        mkBoard()
        mkCirc()
        mkTxt()

        player1circle = defPlayerCirc(choose_color1)
        player2circle = defPlayerCirc(choose_color2)    

        playerList = [player_1, player_2]

        player1coins = []
        player2coins = []

        win = False

    #TURNS LOOP
        while(True):
            #player 1 turn

            x = findPosition()
            col = tracker_goto(x)
            colNum = clickyColumn(col)
            returnFirstCircleName(colNum)
            circleCoordAAA = magic(colNum) #return name for grace's go
            player1coins.append([circleCoordAAA[0],int(circleCoordAAA[1])])#add to list of player 1 's coins as a list the column and row of the coin
            drawCirc(player1circle,circleCoordAAA) #draws circle
            checkAll(player1coins)
            win = checkAll
            if(win == True):
                print("Congratulations" + player_1 + "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!1")
                break

            #player 2 turm
                
            x = findPosition()
            col = tracker_goto()
            colNum = clickyColumn(col)
            returnFirstCircleName(colNum)
            circleCoordAAA = magic(colNum) #return name for grace's go
            player2coins.append([circleCoordAAA[0],int(circleCoordAAA[1])])#add to list of player 1 's coins as a list the column and row of the coin
            drawCirc(player2circle,circleCoordAAA) #draws circle
            checkAll(player2coins)
            win = checkAll
            if(win == True):
                print("Congratulations" + player_2 + "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!1")
                break
        print("Thank you for playing Connect Four !! :) Don't forget to smash that like button and hit subscribe! See you on the flip side epic gamers B)")
else:
    print ("Ok, bye.  See you again soon! :) ")
    
