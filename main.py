# To calculate sum of 3 numbers
def sum(a, b, c):
    return a + b + c

# To print updated board
def printBoard(xValue, oValue):
    zero = 'X' if xValue[0] else ('O' if oValue[0] else 0)
    one = 'X' if xValue[1] else ('O' if oValue[1] else 1)
    two = 'X' if xValue[2] else ('O' if oValue[2] else 2)
    three = 'X' if xValue[3] else ('O' if oValue[3] else 3)
    four = 'X' if xValue[4] else ('O' if oValue[4] else 4)
    five = 'X' if xValue[5] else ('O' if oValue[5] else 5)
    six = 'X' if xValue[6] else ('O' if oValue[6] else 6)
    seven = 'X' if xValue[7] else ('O' if oValue[7] else 7)
    eight = 'X' if xValue[8] else ('O' if oValue[8] else 8)
    print(f"{zero} | {one} | {two} ")
    print("--|---|---")
    print(f"{three} | {four} | {five} ")
    print("--|---|---")
    print(f"{six} | {seven} | {eight} ")

# To check the winner
def checkWin(xValue, oValue):
    wins = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    for w in wins:
        if sum(xValue[w[0]], xValue[w[1]], xValue[w[2]]) == 3:
            print("X won the match!")
            return 1
        if sum(oValue[w[0]], oValue[w[1]], oValue[w[2]]) == 3:
            print("O won the match!")
            return 0
    return -1

# Main function
if __name__ == "__main__":
    xValue = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    oValue = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    tLeft = 9  # number of remaining turns
    turn = 1  # 1 for X and 0 for O
    print("Let's play Tic Tac Toe!")
    while True:  # loop turns one by one
        printBoard(xValue, oValue)
        if turn == 1:  # turn of user X
            output = int(input("Please enter the value for X: "))
            if oValue[output] == 0:
                xValue[output] = 1
            else:
                continue
            tLeft = tLeft-1
        elif turn == 0:  # turn of user 0
            output = int(input("Please enter the value for 0: "))
            if xValue[output] == 0:
                oValue[output] = 1
            else:
                continue
            tLeft = tLeft - 1
        else:  # wrong input case
            print("Wrong input!")
            continue
        win = checkWin(xValue, oValue)
        if win != -1 or tLeft == 0:  # when nobody wins
            print("Match over")
            break
        turn = 1 - turn

