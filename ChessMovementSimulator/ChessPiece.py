from ChessPieceKnight import Knight
from ChessPieceQueen import Queen
from ChessPieceBishop import Bishop
from ChessPieceRook import Rook
from ChessPieceKing import King

class Chess_Piece(object):
    global x
    global y
    global newGame
    global oldCoords
    global myType

    def __init__(self, type, x, y):
        global newGame
        global oldCoords
        global myType
        oldCoords = []
        self.x = x    #A-H inclusive
        self.y = y   #1-8 inclusive
        self.type = type.lower()
        if type == "knight":
            myType = Knight(x, y)
        elif type == "queen":
            myType = Queen(x, y)
        elif type == "bishop":
            myType = Bishop(x, y)
        elif type == "rook":
            myType = Rook(x, y)
        elif type == "king":
            myType = King(x, y)
        newGame = True
                
    def printBoard(self, newGame, x, y, add):

        if newGame == True:
            global oldCoords
            oldCoords = []
            newGame = False
            
        if add == 1:
            oldCoords.append("(" + str(x) + "," + str(y)+ ")")

        print("  1 2 3 4 5 6 7 8")
        for i in range(8):
            print(i + 1, end=" ")
            for j in range(8):
                if i == y-1 and j == x-1:
                    print("+", end=" ")
                else:
                    print("-", end=" ")
            print("   ")
                    
    def movePiece(self, newX, newY):
        global newGame
        newGame = False
        if not (newX <= 0 or newY <= 0):
            self.printBoard(newGame, newX, newY, 1) if myType.moves(self.getX(), self.getY(), newX, newY) else print("Invalid Move\n")
        else:
            print("Invalid Move\n")
        

    def numMoves(self):
        return len(oldCoords)-1

    def lastMove(self):
        return oldCoords[len(oldCoords)-1]
    
    def previousMove(self):
        return oldCoords[len(oldCoords)-2]

    def getX(self):
        return int(self.lastMove()[1:2])

    def getY(self):
        return int(self.lastMove()[3:4])

    def undo(self):
        if self.numMoves() == 0:
            print("\nNothing to undo\n")
        else:
            try:
                del oldCoords[len(oldCoords)-1]
                self.printBoard(newGame, self.getX(), self.getY(), 1)
                del oldCoords[len(oldCoords)-1]
            except:
                print("Can't undo")
                
    def pastMoves(self):
        output = ""
        for i in range(len(oldCoords)):
            if i != 0:
                output += oldCoords[i] + "\n"
        return output

    def startingLoc(self):
        return oldCoords[0]
