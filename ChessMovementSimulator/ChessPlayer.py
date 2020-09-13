from ChessPiece import Chess_Piece

Name = str(input("Enter your username: "))

class Chess_Player(object):

    global newGame

    def __init__(self, username):
        self.username = username

    def startGame(self):
            global newGame
            newGame = False
            
            print("Welcome, " + self.username + ", to the game of not-chess.")
            print("Avatar types: \n    knight\n    queen\n    bishop\n    rook\n    king")

            userInput = str(input("Pick your avatar type: "))
            userInput = userInput.strip().lower()
            userInput2 = int(input("Pick your starting X coordinate(1-8): "))
            userInput3 = int(input("Pick your starting Y coordinate(1-8): "))
            
            while not((userInput2 <= 8 and userInput2 >= 1) and (userInput3 <= 8 and userInput3 >= 1)):
                print("Invalid cooridinates")
                userInput2 = int(input("Pick your starting X coordinate(1-8): "))
                userInput3 = int(input("Pick your starting Y coordinate(1-8): "))
                
            print("Type 'q' or 'quit' to quit")
            userInput4 = "Start"

            userInput = Chess_Piece(userInput, userInput2, userInput3)
            userInput.printBoard(True, userInput2, userInput3, 1)

            while userInput4 != "q" and userInput4 != "quit":  
                print("Menu: move piece\n      undo\n      stats\n      show board\n      new game\n      quit")
                userInput4 = str(input("Pick an option from the menu above: "))
                userInput4 = userInput4.strip().lower()

                if "move" in userInput4:
                   userInput2 = int(input("Enter new X cooridinate: "))
                   userInput3 = int(input("Enter new Y cooridinate: "))

                   userInput.movePiece(userInput2, userInput3)
                if "undo" in userInput4:
                    userInput.undo()
                if "stats" in userInput4:
                    print("\n——Statistics——")
                    print("¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯")
                    print("Starting location: " + str(userInput.startingLoc()))
                    print("Total moves: " + str(userInput.numMoves()))
                    print("Past moves: \n" + str(userInput.pastMoves()))
                if "show" in userInput4:
                    userInput.printBoard(False, userInput2, userInput3, 0)
                if "new" in userInput4:
                    newGame = True
                    break
            self.new_game(newGame)
                
    def new_game(self, x):
        if x == True:
            self.startGame()
            
Name = Chess_Player(Name)
Name.startGame()
