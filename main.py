#This is a main code python file . The output and user interface was very normal.


def sum(a,b,c):
    return a+b+c

def printBoard(xState,zState):
    zero= 'X' if xState[0] else ('0' if zState[0] else 0)
    one = 'X' if xState[1] else ('0' if zState[1] else 1)
    two= 'X' if xState[2] else ('0' if zState[2] else 2)
    three= 'X' if xState[3] else ('0' if zState[3] else 3)
    four= 'X' if xState[4] else ('0' if zState[4] else 4)
    five= 'X' if xState[5] else ('0' if zState[5] else 5)
    six= 'X' if xState[6] else ('0' if zState[6] else 6)
    seven= 'X' if xState[7] else ('0' if zState[7] else 7)
    eight= 'X' if xState[8] else ('0' if zState[8] else 8)


    print(f"{zero} | {one} | {two} ")
    print(f"--|---|---")
    print(f"{three} | {four} | {five} ")
    print(f"--|---|---")
    print(f"{six} | {seven} | {eight} ")


def checkwin(xState, zState):
    xwins = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
    for win in xwins:
        if(sum(xState[win[0]],xState[win[1]], xState[win[2]]) == 3):
            print("1 won the match")
            return 1
        elif(sum(zState[win[0]],zState[win[1]], zState[win[2]]) == 3):
            print("0 won the match")
            return 0
    return -1


if __name__== "__main__":
    xState =[0,0,0,0,0,0,0,0,0]
    zState =[0,0,0,0,0,0,0,0,0]
    turn = 1 #1for X  0 for 0

    print("Welcome to Game")
    while (True):
        print("X's Chance")
        printBoard(xState,zState)
        if(turn == 1):
            print("X's Chance")
            value = int(input("Please enter value"))
            xState[value] = 1
        else:
            print("0's Chance")
            value = int(input("Please Enter a Value:"))
            zState[value] = 1
        
        cwin = checkwin(xState,zState)
        if(cwin != -1):
            print("Match over")
            break
        turn = 1 - turn