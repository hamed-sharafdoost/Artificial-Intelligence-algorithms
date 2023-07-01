import random as rand
from colorama import Fore
import copy as cop
N = 8
board = [[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]]

def MakeRandomMove(chessboard):
    for i in range(N):
        chessboard[i][rand.randint(0,7)] = 1
    return chessboard

def Printboard(chessboard):
    for i in chessboard:
        for j in i:
            if j == 1:
                print(f"{Fore.CYAN}{j}{Fore.WHITE} ",end = " ")
            else:
                print(f"{j} ", end =" ")
        print()
        print("----------------------------")

def CalculateConflicts(chessboard):
    attacks = 0
    for i in range(N):
        row = 0
        conflict = 0
        while(row < N):
            if chessboard[row][i] == 1:
                conflict+=1
            row+=1
        if conflict > 1:
                attacks +=(conflict * (conflict - 1))/2
        #Calculate diaognal from the left-bottom corner
        row = N - 1 - i
        col = 0
        conflict = 0
        while(col < (N - i) and row >= 0):
            if chessboard[row][col] == 1:
                conflict+=1
            row-=1
            col+=1
        if conflict > 1:
            attacks +=(conflict * (conflict - 1))/2
        #Calculate diaognal from the left-top corner
        row = i
        col = 0
        conflict = 0
        while(col < (N - i) and row < N):
            if chessboard[row][col] == 1:
                conflict+=1
            row+=1
            col+=1
        if conflict > 1:
            attacks +=(conflict * (conflict - 1))/2
        #Calculate diaognal from the right-bottom corner
        row = N - 2 - i
        col = N - 1
        conflict = 0
        while(col > i and row >= 0):
            if chessboard[row][col] == 1:
                conflict+=1
            row-=1
            col-=1
        if conflict > 1:
            attacks +=(conflict * (conflict - 1))/2
        #Calculate diaognal from the right-top corner
        row = i + 1
        col = N - 1
        conflict = 0
        while(col > i and row < N):
            if chessboard[row][col] == 1:
                conflict+=1
            row+=1
            col-=1
        if conflict > 1:
            attacks +=(conflict * (conflict - 1))/2
    return attacks

def Findqueens(chessboard):
    queenplace = [] #Indicies indicate row and elemnets of list indicate which column the queen is belonged to
    for row in chessboard:
        for queen in row:
            if queen == 1:
                queenplace.append(row.index(queen))
    return queenplace

def Getneighbor(gameboard):
    last = list()
    opstate = gameboard
    neighbor = gameboard
    opconflicts = CalculateConflicts(opstate)
    queenplace = Findqueens(neighbor)
    for i in range(N):
        for j in range(N):
            if j != queenplace[i]:
                neighbor[i][j] = 1
                neighbor[i][queenplace[i]] = 0
                temp = CalculateConflicts(neighbor)
                if temp <= opconflicts:
                    opstate = cop.deepcopy(neighbor)
                    opconflicts = temp
                neighbor[i][j] = 0
                neighbor[i][queenplace[i]] = 1
    last = opstate
    return last
def Comaprestate(current,neighbor):
    currentstate = Findqueens(current)
    neighborstate = Findqueens(neighbor)
    for i in range(N):
        if currentstate[i] != neighborstate[i]:
            return False
    return True

def Hillclimbing(chessboard):
    neighbor = list()
    while(True):
        neighbor = Getneighbor(chessboard)
        if CalculateConflicts(neighbor) == 0:
            print("Problem is solved and solution is here :")
            Printboard(neighbor)
            break
        else:
            chessboard = [[ 0 for x in range(N)] for y in range (N)]
            chessboard = MakeRandomMove(chessboard)



Printboard(MakeRandomMove(board))
Hillclimbing(board)
# print(f"current conflicts :{CalculateConflicts(board)}")
# print("optimal neighbor is :")
# neighbor = Getneighbor(board)
# Printboard(neighbor)
# print(f"neighbor conflics is : {CalculateConflicts(neighbor)}")