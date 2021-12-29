
def checkWin(board, boardSize, winCondition): 
    # a tuple - (if win exists, returns 1 if player1 wins 0 if player2/CPU wins)
    # check rows and cols
    for i in range(boardSize):
        streak = 0
        if(board[i][0] != 0):
            streak = 1
        for m in range(1, boardSize):
            if(board[i][m] == 0):
                streak = 0
            elif(board[i][m] != board[i][m - 1]):
                streak = 1
            else:
                streak += 1
                if(streak == winCondition):
                    return (1, board[i][m] == 1)
        streak = 0
        if(board[0][i] != 0):
            streak = 1
        for n in range(1, boardSize):
            if(board[n][i] == 0):
                streak = 0
            elif(board[n][i] != board[n - 1][i]):
                streak = 1
            else:
                streak += 1
                if(streak == winCondition):
                    return (1, board[n][i] == 1)
    # check diagonals
    for i in range(boardSize):
        streak = 0
        if(board[i][0] != 0):
            streak = 1
        for m in range(1, boardSize - i):
            if(board[i + m][m] == 0):
                streak = 0
            elif(board[i + m][m] != board[i + m - 1][m - 1]):
                streak = 1
            else:
                streak += 1
                if(streak == winCondition):
                    return (1, board[i + m][m] == 1)
    for i in range(boardSize):
        streak = 0
        if(board[0][i] != 0):
            streak = 1
        for n in range(1, boardSize - i):
            if(board[n][i + n] == 0):
                streak = 0
            elif(board[n][i + n] != board[n - 1][i + n - 1]):
                streak = 1
            else:
                streak += 1
                if(streak == winCondition):
                    return (1, board[n][i + n] == 1)
    for i in range(boardSize):
        streak = 0
        if(board[i][0] != 0):
            streak = 1
        for m in range(1, i + 1):
            if(board[i - m][m] == 0):
                streak = 0
            elif(board[i - m][m] != board[i - m + 1][m - 1]):
                streak = 1
            else:
                streak += 1
                if(streak == winCondition):
                    return (1, board[i - m][m] == 1)
    for i in range(boardSize):
        streak = 0
        if(board[boardSize - 1][i] != 0):
            streak = 1
        for m in range(2, boardSize - i + 1):
            if(board[boardSize - m][i + m - 1] == 0):
                streak = 0
            elif(board[boardSize - m][i + m - 1] != board[boardSize - m + 1][i + m - 2]):
                streak = 1
            else:
                streak += 1
                if(streak == winCondition):
                    return (1, board[boardSize - m][i + m - 1] == 1)
    return (0, 0)

def botMove(board, depth, boardSize, winCondition):
    bestScore = float('inf') # bot wants to minimize score, player wants to maximize
    row, col = -1, -1

    gameWon, player = checkWin(board, boardSize, winCondition) # check if game is already won first
    if(gameWon):
        return row, col

    for i in range(boardSize):
        for j in range(boardSize):
            if(board[i][j] == 0):                 # visit each available cell
                board[i][j] = 2
                score = minimax(board, depth-1, boardSize, winCondition, False, float('-inf'), float('inf'))
                board[i][j] = 0
                if(score < bestScore):
                    bestScore = score
                    row, col = i, j

    return row, col

def minimax(board, depth, boardSize, winCondition, bot, alpha, beta):

    gameWon, player = checkWin(board, boardSize, winCondition)
    if(gameWon): 
        if(player == 1): return 1 * (depth + 1)    # positive score if player wins, negative if bot wins
        else: return -1 * (depth + 1)                # multiply by depth to prioritize winning in the fewest moves possible (+1 to avoid multiplying by 0)

    elif(depth == 0):                            # tie score set as 0
        return 0

    flag = False
    if(bot): # bot's turn (minimizing)
        bestScore = float('inf')
        for i in range(boardSize):
            for j in range(boardSize):
                if(board[i][j] == 0):
                    board[i][j] = 2
                    bestScore = min(bestScore, minimax(board, depth-1, boardSize, winCondition, False, alpha, beta))
                    board[i][j] = 0
                    beta = min(beta, bestScore)
                    if(beta <= alpha):
                        break

    else: # player's turn (maximizing)
        bestScore = float('-inf')
        for i in range(boardSize):
            for j in range(boardSize):
                if(board[i][j] == 0):
                    board[i][j] = 1
                    bestScore = max(bestScore, minimax(board, depth-1, boardSize, winCondition, True, alpha, beta))
                    board[i][j] = 0
                    alpha = max(alpha, bestScore)
                    if(beta <= alpha):
                        break

    return bestScore
