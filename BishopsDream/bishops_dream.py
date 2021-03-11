#bishops dream
#given a m*n board with mirrors along each edge, bishop moves like light but in only diagonal directions,
#it reflects like light when it encounters an edge
#given board size like [3,7], initialposition like [1,2] and initialdireciton = [1,1]
#find its position after k moves
#this problem can be extended to million dimensions and million moves and still a simple solution
def chessBishopDream(boardSize, initPosition, initDirection, k):
    final_pos = []
    #considering one direction at a time
    for i in range(2):
        new_pos = initPosition[i] + k*initDirection[i]
        new_pos %= boardSize[i]*2
        #for remainder greater than board size
        if new_pos >= boardSize[i]:
            new_pos = boardSize[i]*2 - new_pos - 1
        final_pos.append(new_pos)
    return final_pos
print(chessBishopDream([17, 19],[16, 18],[1, 1],239239239))