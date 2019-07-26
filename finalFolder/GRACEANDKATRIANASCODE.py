import turtle
import numpy as np

#START OF GAME
user = input("Welcome to Connect Four!  You need two players for this game.  Would you like to contine (yes or no)? ")
if (user== "yes"):
# User name
        player_1 = str(input("Welcome Player 1! Type in your name: "))
        player_2 = str(input("Welcome Player 2! Type in your name: "))
# Color of Playing Tiles
        choose_color1 = str(input(player_1 + ", what color do you want? \n"))
        if choose_color1 == "white":
            choose_color1 = str(input(player_1 + ", please choose a different color: \n"))
        choose_color2 = str(input(player_2 + ", what color do you want? \n"))
        if choose_color2 == "white":
            choose_color2 = str(input(player_2 + ", please choose a different color: \n"))

        
        board = turtle.Turtle()
        board.color('black')
        board.speed(0)

        board.penup()
        board.goto(-500,-350)
        board.pendown()

        board.forward(900)
        board.right(270)
        board.forward(850)
        board.right(270)
        board.forward(900)
        board.right(270)
        board.forward(850)

        board.penup()
        board.goto(-505, -355)
        board.pendown()
        board.right(270)
        board.forward(910)
        board.right(270)
        board.forward(860)
        board.right(270)
        board.forward(910)
        board.right(270)
        board.forward(860)
        board.hideturtle()
#Circle Slots
    #circle radius = 50
    #space between circles = 25
    #A1 = (-425, -250), B1 = (-300, -250)
        sir = turtle.Turtle()
        sir.color('black')
        sir.speed(0)

        sir.penup()
        sir.goto(-425, -250)
        sir.pendown()
        for x in range(6):
            for x in range(7):
                sir.circle(50)
                sir.penup()
                sir.forward(125)
                sir.pendown()
            sir.penup()
            sir.left(90)
            sir.forward(125)
            sir.left(90)
            sir.forward(875)
            sir.left(180)
            sir.pendown()
        sir.hideturtle()
        label = turtle.Turtle()
        label.speed(0)
        label.penup()
        label.goto(-525, -225)
        label.left(90)
        lis = [1, 2, 3, 4, 5, 6]
        for x in lis:
            label.pendown()
            style = ('Courier', 15)
            label.write(x, font=style, align='center')
            label.penup()
            label.forward(125)
        label.penup()
        label.goto(-425, -400)
        label.right(90)
        lis2 = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
        for x in lis2:
            label.pendown()
            style = ('Courier', 15)
            label.write(x, font=style, align='center')
            label.penup()
            label.forward(125)
        label.hideturtle()

#Board Text                           
        screen = turtle.Screen()

        turtle.penup()
        turtle.goto(-50,-300)
        turtle.pendown()
        screen.register_shape("comic.gif")
        image = "comic.gif"
        screen.addshape(image)
        turtle.shape(image)

#Credits
        wright = turtle.Turtle()
        wright.hideturtle()
        wright.penup()
        wright.goto(-50, -450)
        wright.pendown()
        style = ("Courier", 12)
        wright.write("Made by Epic Gamers: ", font=style, align='center')
        wright.penup()
        wright.goto(-50, -475)
        wright.pendown()
        style = ("Courier", 12)
        wright.write("Rucha B., Grace N., Alayna T., and Katriana T.", font=style, align='center')
        wright.penup()
        wright.goto(-50, -500)
        wright.pendown()
        style = ("Courier", 8)
        wright.write("~ Getting kicked out of rooms since 2019 ~", font=style, align='center')
        wright.penup()
#Assigning variables to each circle
    #Player 1 color = choose_color1
    #Player 2 color = choose_color2
    # Capital letter = turtle name
    # Lowercase letter = circle variable
        player1circles = turtle.Turtle()
        player1circles.color(choose_color1, choose_color1)
        player1circles.speed(0)
        player1circles.hideturtle()
        player2circles = turtle.Turtle()
        player2circles.color(choose_color2, choose_color2)
        player2circles.speed(0)
        player2circles.hideturtle()
        circles = {"a1": (-425, -250), "a2": (-425, -125), "a3": (-425, 0), "a4": (-425, 125), "a5": (-425, 250), "a6": (-425, 375),"b1": (-300, -250), "b2": (-300, -125), "b3": (-300, 0), "b4": (-300, 125), "b5": (-300, 250), "b6": (-300, 375),"c1": (-175, -250), "c2": (-175, -125), "c3": (-175, 0), "c4": (-175, 125), "c5": (-175, 250), "c6": (-175, 375),"d1": (-50, -250), "d2": (-50, -125), "d3": (-50, 0), "d4": (-50, 125), "d5": (-50, 250), "d6": (-50, 375),"e1": (75, -250), "e2": (75, -125), "e3": (75, 0), "e4": (75, 125), "e5": (75, 250), "e6": (75, 375),"f1": (200, -250), "f2": (200, -125), "f3": (200, 0), "f4": (200, 125), "f5": (200, 250), "f6": (200, 375),"g1": (325, -250), "g2": (325, -125), "g3": (325, 0), "g4": (325, 125), "g5": (325, 250), "g6": (325, 375)}

#Defines lists and coordinates
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

#Coloring selected circles
    #Player1
#def player1():
        o = "d1"              #variable for which circle to color in
        for selection in circles.values():
            player1circles.penup()
            player1circles.goto(circles[o])    #also has variable for which circle to color in
            player1circles.pendown()
            player1circles.begin_fill()
            player1circles.circle(50)
            player1circles.end_fill()
                
            #Player2
        #def player2():
        t = "a1"
        for selection in circles.values():
            player2circles.penup()
            player2circles.goto(circles[t])
            player2circles.pendown()
            player2circles.begin_fill()
            player2circles.circle(50)
            player2circles.end_fill()
else:
    print ("Ok, bye.  See you again soon! :) ")
              
