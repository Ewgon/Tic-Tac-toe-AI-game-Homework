"""
Tic Tac Toe Player
"""

import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    count = 0
    for i in range(len(board)):
        for j in range(len(board[i])):
            if (board[i][j] == EMPTY):
                count += 1
    if ((count % 2) == 0):
        return O
    else:
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    set = []
    for i in range(len(board)):
        for j in range(len(board[i])):
            if (board[i][j] == EMPTY):
                set.append((i, j))
    return set


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if (action == None):
        raise Exception("Action is not defined")
    if (action[0] > len(board)-1):
        raise Exception("Action out ouf bound")
    elif (action[1] > len(board[action[0]])):
        raise Exception("Action out ouf bound")
    elif (board[action[0]][action[1]] != EMPTY):
        #raise Exception("Location not EMPTY")
        return board
    else:
        stateBoard = [i.copy() for i in board]
        stateBoard[action[0]][action[1]] = player(stateBoard)
        print(stateBoard)
    return stateBoard


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    countXRow, countORow = 0, 0
    countXCol, countOCol = 0, 0
    countXDiag1, countODiag1 = 0, 0
    countXDiag2, countODiag2 = 0, 0
    for i in range(len(board)):
        countXRow, countORow = 0, 0
        countXCol, countOCol = 0, 0
        for j in range(len(board[i])):
            if (board[i][j] == X):
                countXRow += 1
                if (i == j):
                    countXDiag1 += 1
            elif (board[i][j] == O):
                countORow += 1
                if (i == j):
                    countODiag1 += 1
            if (board[j][i] == X):
                countXCol += 1
                if (i + j == len(board)-1):
                    countXDiag2 += 1
            elif (board[j][i] == O):
                countOCol += 1
                if (i + j == len(board)-1):
                    countODiag2 += 1
        if (countXRow == 3 or countXCol == 3 or countXDiag1 == 3 or countXDiag2 == 3):
            return X
        if (countORow == 3 or countOCol == 3 or countODiag1 == 3 or countODiag2 == 3):
            return O
    return None

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if (winner(board) != None):
        return True
    count = 0
    for i in range(len(board)):
        for j in range(len(board[i])):
            if (board[i][j] == EMPTY):
                count += 1
    if (count == 0):
        return True
    else:
        return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    winnerPlayer = winner(board)
    if (winnerPlayer == X):
        return 1
    elif (winnerPlayer == O):
        return -1
    else:
        return 0


def maxValue(board):
    if(terminal(board)):
        return utility(board)
    else:
        bestvalue = -999
        value = -999
        for action in actions(board):
            value = max(value, minValue(result(board, action)))
            if(value > bestvalue):
                    bestvalue = value
        return(value)


def minValue(board):
    if(terminal(board)):
        return utility(board)
    else:
        bestvalue = +999
        value = +999
        for action in actions(board):
            value = min(value, maxValue(result(board, action)))
            if(value < bestvalue):
                    bestvalue = value
        return(value)


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if(terminal(board)):
        return None
    else:
        return runMinimax(board)[1]
        #return runMinimaxAlphaBetaPruning(board, -999, +999)[1]


def runMinimax(board):
    if(terminal(board)):
        return (utility(board), (-1,-1))

    else:
        if(player(board) == X):
            bestvalue = -999
            move = (-1, -1)
            for action in actions(board):
                value = runMinimax(result(board, action))[0]
                if(value > bestvalue):
                    bestvalue = value
                    move = action
            return(bestvalue, move)

        else:
            bestvalue = +999
            move = (-1, -1)
            for action in actions(board):
                value = runMinimax(result(board, action))[0]
                if(value < bestvalue):
                    bestvalue = value
                    move = action
            return(bestvalue, move)




#
#  I tried to make Alpha-Beta Pruning but does not seems to work
#

# def runMinimaxAlphaBetaPruning(board, a, b):
#     if(terminal(board)):
#         return (utility(board), (-1,-1))

#     else:
#         if(player(board) == X):
#             bestvalue = -999
#             move = (-1, -1)
#             for action in actions(board):
#                 value = runMinimaxAlphaBetaPruning(result(board, action), a, b)[0]
#                 if(value > bestvalue):
#                     bestvalue = value
#                     move = action
#                 if( bestvalue <= a):
#                     return(bestvalue, move)
#                 b = max(b, value)
#             return(bestvalue, move)

#         else:
#             bestvalue = +999
#             move = (-1, -1)
#             for action in actions(board):
#                 value = runMinimaxAlphaBetaPruning(result(board, action), a, b)[0]
#                 if(value < bestvalue):
#                     bestvalue = value
#                     move = action
#                 if( bestvalue >= b):
#                     return(bestvalue, move)
#                 a = max(a, value)
#             return(bestvalue, move)