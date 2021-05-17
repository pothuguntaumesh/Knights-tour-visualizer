import turtle
import time
from playsound import playsound
import multiprocessing


class ChessBoard:
    def __init__(self):
        # setting up the screen
        self.wn = turtle.Screen()
        self.wn.setup(width=1000, height=820)
        self.wn.bgcolor('black')
        self.wn.title('Knights Tour')
        self.wn.addshape('knight.gif')
        self.clicked = True
        self.time = 1
        self.timer = True
        # writer used for writing number on the board
        self.writer = turtle.Turtle()
        self.writer.width(10)
        self.writer.color('black')
        self.writer.pencolor('black')
        self.writer.pensize(10)
        self.writer.penup()
        self.writer.hideturtle()
        # creating a pen
        pn = turtle.Turtle()
        pn.penup()
        pn.goto(x=-400, y=400)
        pn.speed(100)
        # Position to start drawing
        curY = 400
        # intializes the board
        self.initBoard(pn, curY)
        self.wn.onscreenclick(self.placeKnight)
        # Now make a function to exactly place things at the center of each grid
        self.wn.mainloop()

    def sound(self):
        playsound('sound.mp3')

    def placeKnight2(self, x, y):
        self.knight.goto(self.boardMapper[x][y][0], self.boardMapper[x][y][1])
        self.sound()
        self.knight.showturtle()

    def placeKnight(self, x, y):
        if self.clicked and x <= 400 and x >= -400 and y <= 400 and y >= -400:
            newX, newY = self.placeCenter(int(x), int(y))
            self.startX = newX
            self.startY = newY
            self.knight = turtle.Turtle()
            self.knight.penup()
            self.knight.shape('knight.gif')
            self.knight.goto(newX, newY)
            self.sound()
            self.clicked = False
            self.knight_tour(8)
        # if not self.clicked and self.timer:
        #     print('hello')
        #     self.time = 9999
        #     self.timer = False
        # elif not self.clicked and not self.timer:
        #     self.time = 1

    def removeKnight(self):
        self.knight.hideturtle()

    def placeNumber(self, number, x, y):
        if y <= 0:
            y -= 40
        else:
            y -= 40
        self.writer.goto(x, y)
        self.writer.write(number, align='center', font=('Arial', 50, 'normal'))

    def placeNumber2(self, number, x, y, marker):
        if y <= 0:
            y -= 40
        else:
            y -= 40
        marker.hideturtle()
        marker.goto(x, y)
        marker.hideturtle()
        marker.write(number, align='center', font=('Arial', 50, 'normal'))

    def placeCenter(self, x, y):
        xCoor = str(x)
        yCoor = str(y)
        if len(xCoor) == 2:
            xCoor = '0'+xCoor
        if len(yCoor) == 2:
            yCoor = '0'+yCoor
        if len(xCoor) == 1:
            xCoor = '00'+xCoor
        if len(yCoor) == 1:
            yCoor = '00'+yCoor
        # get the last two of xcoor and ycoor
        xLastTwo = 100-int(xCoor[-1:-3:-1][-1::-1])
        yLastTwo = 100-int(yCoor[-1:-3:-1][-1::-1])
        if x < 0:
            newX = x-xLastTwo
        else:
            newX = x+xLastTwo
        if y < 0:
            newY = y-yLastTwo
        else:
            newY = y+yLastTwo
        if newX < 0:
            newX += 50
        if newY < 0:
            newY += 50
        if newX > 0:
            newX -= 50
        if newY > 0:
            newY -= 50
        return (newX, newY)

    def initBoard(self, pn, curY):
        for i in range(8):
            pn.goto(x=-400, y=curY)
            curY -= 100
            pn.pendown()

            for j in range(8):
                if (i+j) % 2 == 0:
                    color = 'white'
                else:
                    color = 'green'
                pn.color(color)

                pn.begin_fill()
                self.drawBoard(pn)
                pn.end_fill()
            pn.penup()
        pn.hideturtle()

    def boardMapper(self):
        boardMapper = []
        for y in range(350, -351, -100):
            ls = []
            for x in range(-350, 351, 100):
                ls.append((x, y))
            boardMapper.append(ls)
        return boardMapper

    def findIndex(self, x, y, boardMapper):
        for i in range(8):
            for j in range(8):
                if boardMapper[i][j] == (x, y):
                    return i, j

    def drawBoard(self, pn):

        for i in range(4):
            pn.forward(100)
            pn.lt(-90)
        pn.forward(100)

    def drawGrid(self, pen, x, y):
        pass

    def knight_tour(self, n):
        board = [[-1 for i in range(n)] for j in range(n)]
        self.boardMapper = self.boardMapper()
        # using x and y values find the index in the board

        x, y = self.findIndex(self.startX, self.startY, self.boardMapper)
        self.knight_tour_helper(
            n, board, x=x, y=y, counter=0, prevX=0, prevY=0)
        print(board)

    def isSafe(self, x, y, board, n):
        if (x < 0) or (x >= n) or (y < 0) or (y >= n) or board[y][x] != -1:
            return False
        return True

    def removeText(self, x, y):
        # The idea is just repaint the square
        p, q = self.findIndex(x, y, self.boardMapper)
        if (p+q) % 2 == 0:
            color = 'white'
        else:
            color = 'green'

        if x < 0:
            x -= 50
        if y < 0:
            y -= 50
        if x > 0:
            x += 50
        if y > 0:
            y += 50
        pen = turtle.Turtle()
        pen.speed(100)
        pen.penup()
        pen.goto(x, y)
        pen.color(color)
        pen.begin_fill()
        self.drawBoard(pen)
        pen.end_fill()

    def removeNumber(self, counter):
        print(counter)

        self.writer.undo()

    def boardDrawingSound(self):
        playsound('boardDrawing.mp3')

    def knight_tour_helper(self, n, board, x, y, counter, prevX, prevY):
        marker = turtle.Turtle()
        marker.hideturtle()
        marker.width(10)
        marker.color('yellow')
        marker.pencolor('black')
        marker.pensize(10)
        marker.penup()
        marker.hideturtle()
        if counter > 0:
            # place knight
            self.placeKnight2(x, y)

            time.sleep(0.2)

        if counter == n * n:
            return True

        self.removeKnight()
        board[y][x] = counter
        # write the no on the board
        self.placeNumber2(
            counter, self.boardMapper[x][y][0], self.boardMapper[x][y][1], marker)
        time.sleep(0.2)

        for x_move, y_move in zip([-2, -2, -1, -1, 1, 1, 2, 2], [-1, 1, -2, 2, -2, 2, -1, 1]):
            if self.isSafe(x+x_move, y+y_move, board, n):
                if self.knight_tour_helper(n, board, x + x_move, y + y_move, counter + 1, x, y):
                    return True
        board[y][x] = -1
        self.placeKnight2(x, y)
        self.sound()
        time.sleep(.2)
        marker.clear()
        time.sleep(.2)
        self.placeKnight2(prevX, prevY)
        time.sleep(.2)
        return False


if __name__ == '__main__':
    board = ChessBoard()
