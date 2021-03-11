#given a 2k+1 by 2k+1 matrix, center of star and width of the star, rotate the diagonals, rows and columns coming out of the center
#by t*45 degress clockwise

def starRotation(m, width, center, t):

    t *= 45
    t %= 360
    t //= 45
    
    x_left = center[1] - width//2
    y_top = center[0] - width//2
    x_right = center[1] + width//2
    y_bottom = center[0] + width//2
    
    for j in range(t):
        l = []
        for i in range(width):
            k = m[y_bottom-i][x_left+i]
            l.append(m[y_top+i][x_right-i])
            
            m[y_top+i][x_right-i] = m[y_top+i][center[1]]
            m[y_top+i][center[1]] = m[y_top+i][x_left+i]
            m[y_top+i][x_left+i] = m[center[0]][x_left+i]
            m[center[0]][x_left+i] = k
        
        for j in range(width//2):
            m[center[0]][x_right-j] = l[j]
    
    return m


def staarRotation(m, w, c, t):
    for i in range(1,int((w+1)/2)):
        for _ in range(t%8):
            p = m[c[0]-i][c[1]-i]
            m[c[0]-i][c[1]-i] = m[c[0]][c[1]-i]
            m[c[0]][c[1]-i] = m[c[0]+i][c[1]-i]
            m[c[0]+i][c[1]-i] = m[c[0]+i][c[1]]
            m[c[0]+i][c[1]] = m[c[0]+i][c[1]+i]
            m[c[0]+i][c[1]+i] = m[c[0]][c[1]+i]
            m[c[0]][c[1]+i] = m[c[0]-i][c[1]+i]
            m[c[0]-i][c[1]+i] = m[c[0]-i][c[1]]
            m[c[0]-i][c[1]] = p
    return m