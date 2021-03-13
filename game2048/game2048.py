#game 2048
#shift all values in the matrix up down left or right
#if the colliding values are same then double them, collison happens b/w two at a time & starts from extreme edge to the direction of movement
#given a state of the game and a set of moves find the final state
#play the game online at http://gabrielecirulli.github.io/2048/

def pack(l): #this function sends the row to the left
    original = len(l)#initial length
    T = [i for i in l if i!=0] #getting rid of any zeros
    i = 0
    while i < len(T) -1:
        if T[i] == T[i+1]:
            T[i],T[i+1] = 0, 2*T[i]
            i += 1
        i += 1
    new = [i for i in T if i!=0] #getting rid of any zeros after doubling the values
    new += [0]*(original - len(new))
    return new
def game2048(grid,path):
    for i in path:
        if i == "L":
            grid = [pack(row) for row in grid]
        if i == "R":
            grid = [pack(row[::-1])[::-1] for row in grid] #sending to the right is same as sending rev to the left and rev it again
        if i == "U": #same as left applied to the cols
            grid = list(map(list,zip(*[pack(col) for col in zip(*grid)])))
        if i == "D":#same as right applied to the cols
            grid = list(map(list,zip(*[pack(col[::-1])[::-1] for col in zip(*grid)])))
    return grid

grid = [[0,0,0,2], 
 [0,0,4,2], 
 [0,0,4,2], 
 [0,0,4,2]]
path = "DRRD"

print(game2048(grid,path))
