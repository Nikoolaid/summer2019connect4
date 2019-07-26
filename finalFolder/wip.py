

# Color of Playing Tiles
def chooseColor(player):
        choose_color1 = str(input( player + ", what color do you want? \n"))
        if choose_color1 == "white":
            choose_color1 = str(input( player + ", please choose a different color: \n"))
        return choose_color1
        
def mkBoard():
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

def mkCirc():
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


        coordinates = {'1st column': (-490, -362.5), '2nd column' : (-362.5, -237.5), '3rd column': (-237.5, -112.5), '4th column': (-112.5, 12.5), '5th column': (12.5, 137.5), '6th column': (137.5, 262.5), '7th column': (262.5, 387.5)}
        a = coordinates['1st column']
        b = coordinates['2nd column']
        c = coordinates['3rd column']
        d = coordinates['4th column']
        e = coordinates['5th column']
        f = coordinates['6th column']
        g = coordinates['7th column']

        if (n > a[0] and n < a[1]):
                return 1
        elif (n > b[0] and n < b[1]):
                return 2
        elif (n > c[0] and n < c[1]):
                return 3
        elif (n > d[0] and n < d[1]):
                return 4
        elif (n > e[0] and n < e[1]):
                return 5
        elif (n > f[0] and n < f[1]):
                return 6
        elif (n > g[0] and n < g[1]):
                return 7

def mkTxt():
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

def defPlayerCirc(chooseColor):
    #Assigning variables to each circle
    #Player 1 color = choose_color1
    #Player 2 color = choose_color2
    # Capital letter = turtle name
    # Lowercase letter = circle variable
        playerAcircles = turtle.Turtle()
        playerAcircles.color(chooseColor, chooseColor)
        playerAcircles.speed(0)
        playerAcircles.hideturtle()

        return playerAcircles

        circles = {"a1": (-425, -250), "a2": (-425, -125), "a3": (-425, 0), "a4": (-425, 125), "a5": (-425, 250), "a6": (-425, 375),"b1": (-300, -250), "b2": (-300, -125), "b3": (-300, 0), "b4": (-300, 125), "b5": (-300, 250), "b6": (-300, 375),"c1": (-175, -250), "c2": (-175, -125), "c3": (-175, 0), "c4": (-175, 125), "c5": (-175, 250), "c6": (-175, 375),"d1": (-50, -250), "d2": (-50, -125), "d3": (-50, 0), "d4": (-50, 125), "d5": (-50, 250), "d6": (-50, 375),"e1": (75, -250), "e2": (75, -125), "e3": (75, 0), "e4": (75, 125), "e5": (75, 250), "e6": (75, 375),"f1": (200, -250), "f2": (200, -125), "f3": (200, 0), "f4": (200, 125), "f5": (200, 250), "f6": (200, 375),"g1": (325, -250), "g2": (325, -125), "g3": (325, 0), "g4": (325, 125), "g5": (325, 250), "g6": (325, 375)}

def defCoords():
    #Defines lists and coordinates
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

        '''
        lista = [0:6]
        listb = [6:12]
        listc = [12:18]
        listd = [18:24]
        listee = [24:30]
        listf = [30:36]
        listg = [36:42]
        '''

def drawCirc(playerCirc, goToCirc):
        for selection in circles.values():
                playerCirc.penup()
                playerCirc.goto(circles[goToCirc])    #also has variable for which circle to color in
                playerCirc.pendown()
                playerCirc.begin_fill()
                playerCirc.circle(50)
                playerCirc.end_fill()

def returnFirstCircName(selection): # returns first open spot in vertical column. returns a1, a2, etc
        if (selection == 1):
                first = (opena[0] - 1)
                return openSpaceA[first]
        elif (selection == 2):
                first = (openb[0] - 1)
                return openSpaceB[first]
        elif (selection == 3):
                first = (openc[0] - 1)
                return openSpaceC[first]
        elif (selection == 4):
                first = (opend[0] - 1)
                return openSpaceD[first]
        elif (selection == 5):
                first = (opene[0] - 1)
                return openSpaceE[first]
        elif (selection == 6):
                first = (openf[0] - 1)
                return openSpaceF[first]
        elif (selection == 7):
                first = (openg[0] - 1)
                return openSpaceG[first]

#return to me coord of new circle
def magic(selection):
        if (selection == 1):
                opena.pop(0)

        elif (selection == 2):
                openb.pop(0)

        elif (selection == 3):
                openc.pop(0)

        elif (selection ==4):
                opend.pop(0)

        elif (selection == 5):
                opene.pop(0)

        elif (selection == 6):
                openf.pop(0)

        elif (selection == 7):
                openg.pop(0)

#get mouse pos as list and return column its in
def clickyColumn(n):
        if ((n > a[0]) and (n < a[1])):
                return 1
        elif ((n > b[0]) and (n < b[1])):
                return 2
        elif ((n > c[0]) and (n < c[1])):
                return 3
        elif ((n > d[0]) and (n < d[1])):
                return 4
        elif ((n > e[0]) and (n < e[1])):
                return 5
        elif ((n > f[0]) and (n < f[1])):
                return 6
        elif ((n > g[0]) and (n < g[1])):
                return 7

def tracker_goto(x):
        why = bess.ycor()
        bess.goto(x,why)   
        bess.hideturtle()
        bess.penup()

# Find position of mouse click
def findPosition():
        wn = turtle.Screen()
        wn.listen()
        wn.onclick(tracker_goto)
        x = bess.pos()
        return(x)

def checkAll(listy):
        horiz = checkHorizontal(listy)
        vert = checkVertical(listy)
        dia = checkDiagonal(listy)
        if((horiz == True) or (vert == True) or (dia == True)):
                return True
        else:
                return False


def letterConvert(listy, indexx): #replaces all column letters with number
        letters = ['a','b','c','d','e','f','g']
        for k in range(len(listy)):    
                for x in range(len(letters)): # for all in list
                        if letters[x] == listy[k][indexx]:
                                listy[k][indexx] = x + 1
        return listy


def checkHorizontal(listy): #listy is all player checkers
        listy = letterConvert(listy, 0) #coverting listy to numbers
        for x in listy:
                coolList = []
                for y in listy:
                        if (x[1] == y[1]): # if they share the same x coord (if they're in same row)
                                coolList.append(y[0])# add t
        print(coolList)
        return checkColumn(coolList)

def checkVertical(listy): #listy is all player checkers
        listy = letterConvert(listy, 0) #coverting listy to numbers
        for x in listy:
                coolList = []
                for y in listy:
                        if (x[0] == y[0]): # if they share the same y coord (if they're in same row)
                                coolList.append(y[1])# add t
        print(coolList)
        return checkColumn(coolList)

def checkDiagonal(listy): #listy is all player checkers
        listy = letterConvert(listy, 0) #coverting listy to numbers
        counter = 1
        coolList = []
        for x in listy:
                for y in listy:
                        xo = x[0]
                        yo = y[0]
                        xi = x[1]
                        yi = y[1] #if coords x and y are x+1 and y+1
                        if (((xo == yo + counter) and (xi == yi + counter)) or ((xo == yo - counter) and (xi == yi - counter))):
                                counter += 1 #add to counter
        if(counter >= 4):
                return True
        else:
                return False
    
def checkColumn(column):
        counter = 1
        Ncounter = 1
        for c in column:
                for d in column:
                        if(c == d + counter):
                                counter += 1
                        if(c == d - Ncounter):
                                Ncounter += 1
                print(str(Ncounter) + str(counter))
                if((counter >= 4) or (Ncounter >= 4) or (counter + Ncounter >= 4)):
                        return True
                else:
                        return False
