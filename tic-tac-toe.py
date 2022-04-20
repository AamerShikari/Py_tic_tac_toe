import re

pattern = re.compile("^([A-C][1-3]+)+$")
board = {
    "A1": " ", 
    "A2": " ", 
    "A3": " ", 
    "B1": " ", 
    "B2": " ", 
    "B3": " ", 
    "C1": " ", 
    "C2": " ", 
    "C3": " "
}
fresh_board = board.copy()

def print_board(table):
    print( "     A   B   C")
    print(f"1)   {table['A1']} | {table['B1']} | {table['C1']} ")
    print( "    -----------")
    print(f"2)   {table['A2']} | {table['B2']} | {table['C2']} ")
    print( "    -----------")
    print(f"3)   {table['A3']} | {table['B3']} | {table['C3']} ")

def game_over(table, char):
    if table["A1"] == char and table["A2"] == char and table["A3"] == char: #Horizontal 1
        return True
    elif table["B1"] == char and table["B2"] == char and table["B3"] == char: #Horizontal 2 
        return True
    elif table["C1"] == char and table["C3"] == char and table["C3"] == char: #Horizontal 3
        return True
    elif table["A1"] == char and table["B2"] == char and table["C3"] == char: #Diagonal 1
        return True
    elif table["C1"] == char and table["B2"] == char and table["A3"] == char: #Diagonal 2
        return True
    elif table["A1"] == char and table["B1"] == char and table["C1"] == char: #Vertical 1
        return True
    elif table["A2"] == char and table["B2"] == char and table["C2"] == char: #Vertical 2
        return True
    elif table["A3"] == char and table["B3"] == char and table["C3"] == char: #Vertical 3
        return True
    else: 
        return False

def tie(table):
    for key, val in table.items(): 
        if val == " ":
            return False
    return True

def play_again():
    while True:
        response = input("\n Play Again? (Y/N): ")
        if response.strip() == "Y":
            startGame()
            return False
        elif response.strip() == "N":
            print("Alright, see ya later!")
            return True
        else:
            print("Invalid Input! Try Again!")
    return False


def startGame():
    p1 = True
    print("-----------------------")
    print("Let's play Tic-Tac_Toe!")
    print("-----------------------")
    print( "\nHere is the setup: ")
    print_board(fresh_board)
    print("\nIf you ever want to quit just enter q!")


p1 = True
startGame()


while True: 
    if p1:
        response = input("Player X's Move (example B2): ")
    else: 
        response = input("Player O's Move (example B2): ")
    
    response = response.strip()
    if (response == "q"):
        print("Alright, see ya later!")
        break

    if not pattern.match(response):
        print("Looks like the format of that position was invalid! Try again!")
        continue
    
    if board[response] != " ":
       print("That spots already taken! Try again!")
       continue

    board[response] = "X" if p1 else "O"

    print_board(board)
    if game_over(board, "X" if p1 else "O"):
        if p1: 
            print("CONGRATS PLAYER X! YOU WON!")
        else:
            print("CONGRATS PLAYER O! YOU WON!")

        if play_again():
            break
        board = fresh_board

    if tie(board): 
        print("woah WoAh WOAH, YOU TWO TIED!")

        if play_again():
            break
        board = fresh_board

    p1 = False if p1 else True    


