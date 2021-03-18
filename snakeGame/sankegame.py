#given a game board, the snake head is represented by "^",">","<","v", --> these determine direction of forward movement
#snake body is represented by "*", normal cells are represented by "."
#each snake cell cannot have more than 2 neighbours(given constraint) --> otherwise there would be more than 1 possible snake orientation
#given a command like "FRLF", F-forward, R-snake head turns 90deg clock wise, L-snake head turns 90deg anticlockwise
#snake follows the command one by one
#game breaks if all commands are followed, or snake eats its own tail, or goes out the board
#find the state of the game right before the game breaks
#represent the snake by its usual notation(if it breaks by finishing all commands) else by X(for each bodypart including head)

def snakeGame(gameBoard, commands):
    head = []
    body = []#contains body in correct order(from head to tail)
    head_pos = ["^",">","v","<"]
    dirr = [(-1,0),(0,1),(1,0),(0,-1)]#this will be used for forward movement
    body_dirr = [(1,0),(0,-1),(-1,0),(0,1)]#this will be used to find the body in correct order
    broke = False #if game brakes by going out of the board or eating its tail
    
    for i in range(len(gameBoard)):
        for j in range(len(gameBoard[i])):
            if gameBoard[i][j] in head_pos:
                head.append(i)
                head.append(j)
                head.append(head_pos.index(gameBoard[i][j]))#most important variable

    #finding the body in CORRECT ORDER(from head to tail) --> most difficult and important task
    pos = head[-1]#pos is direction for moving backwards from head to tail
    i = head[0]
    j = head[1]
    while True:
        if i+body_dirr[pos][0]>=0 and i+body_dirr[pos][0]<len(gameBoard) and j+body_dirr[pos][1]>=0 and j+body_dirr[pos][1]<len(gameBoard[0]) and gameBoard[i+body_dirr[pos][0]][j+body_dirr[pos][1]] == "*":
            body.append([i+body_dirr[pos][0],j+body_dirr[pos][1]])
            i,j = body[-1]
        else:
            if i+body_dirr[(pos+1)%4][0]>=0 and i+body_dirr[(pos+1)%4][0]<len(gameBoard) and j+body_dirr[(pos+1)%4][1]>=0 and j+body_dirr[(pos+1)%4][1]<len(gameBoard[0]) and gameBoard[i+body_dirr[(pos+1)%4][0]][j+body_dirr[(pos+1)%4][1]] == "*":
                pos = (pos+1)%4
            elif i+body_dirr[(pos-1)%4][0]>=0 and i+body_dirr[(pos-1)%4][0]<len(gameBoard) and j+body_dirr[(pos-1)%4][1]>=0 and j+body_dirr[(pos-1)%4][1]<len(gameBoard[0]) and gameBoard[i+body_dirr[(pos-1)%4][0]][j+body_dirr[(pos-1)%4][1]] == "*": 
                pos = (pos-1)%4
            else: break

    #resetting the board to all "."
    for i in range(len(gameBoard)):
        for j in range(len(gameBoard[i])):
            gameBoard[i][j] = "."

    #playing the game
    for i in commands:
        if i == "R":
            head[-1] = (head[-1]+1)%4
        elif i == "L":
            head[-1] = (head[-1]-1)%4
        elif i == "F":
            body_copy = body[:] #if the game breaks we need to keep track of prev positions
            for i in range(len(body)-1,0,-1):
                body[i] = body[i-1] #pos gets shifted
            body[0] = [head[0],head[1]]
            head[0] += dirr[head[-1]][0]
            head[1] += dirr[head[-1]][1]
            if [head[0],head[1]] in body or head[0]<0 or head[0]>=len(gameBoard) or head[1]<0 or head[1]>=len(gameBoard[0]):
                    head[0] -= dirr[head[-1]][0]#undoing the move
                    head[1] -= dirr[head[-1]][1]
                    body = body_copy
                    broke = True
                    break
    if broke:
        for i in body:
            gameBoard[i[0]][i[1]] = "X"
        gameBoard[head[0]][head[1]] = "X"
    if not broke:
        for i in body:
            gameBoard[i[0]][i[1]] = "*"
        gameBoard[head[0]][head[1]] = head_pos[head[-1]]
    return gameBoard

gameBoard = [[".",".",".",".",".",".",".",".","."], 
             [".",".","<","*","*","*",".",".","."], 
             [".",".",".",".",".","*",".",".","."], 
             [".",".",".",".","*","*",".",".","."], 
             [".",".",".",".","*",".","*","*","."], 
             [".",".",".",".","*","*","*",".","."], 
             [".",".",".",".",".",".",".",".","."]]
commands = "LFLFLFFFF"
print(snakeGame(gameBoard,commands))