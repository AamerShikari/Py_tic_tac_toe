import re
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

def printBoard(table):
    print( "     A   B   C")
    print(f"1)   {table['A1']} | {table['B1']} | {table['C1']} ")
    print( "    -----------")
    print(f"2)   {table['A2']} | {table['B2']} | {table['C2']} ")
    print( "    -----------")
    print(f"3)   {table['A3']} | {table['B3']} | {table['C3']} ")

def gameOver(table, char):
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


pattern = re.compile("^([A-C][1-3]+)+$")
print("-----------------------")
print("Let's play Tic-Tac_Toe!")
print("-----------------------")

print( "\nHere is the setup: ")
printBoard(board)
print("\n If you ever want to quit just enter q!")

p1 = True
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

    printBoard(board)
    if gameOver(board, "X" if p1 else "O"):
        if p1: 
            print("CONGRATS PLAYER X! YOU WON!")
        else:
            print("CONGRATS PLAYER O! YOU WON!")
        break
    if tie(board): 
        print("woah WoAh WOAH, YOU TWO TIED!")

    p1 = False if p1 else True    


