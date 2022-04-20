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
    print(f"1)   {table['A1']} | {table['A2']} | {table['A3']} ")
    print( "    -----------")
    print(f"2)   {table['B1']} | {table['B2']} | {table['B3']} ")
    print( "    -----------")
    print(f"3)   {table['C1']} | {table['C2']} | {table['C3']} ")

print("-----------------------")
print("Let's play Tic-Tac_Toe!")
print("-----------------------")

print( "\nHere is the setup: ")
printBoard(board)


