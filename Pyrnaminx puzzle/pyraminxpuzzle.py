faceColors = ["R","G","Y","O"]

def rotate(move,faces):
    face1,face2,face3 = faces
    face1[0],face2[4],face3[8] = face3[8],face1[0],face2[4]
    if move.islower():
        face1[1],face2[6],face3[3] = face3[3],face1[1],face2[6]
        face1[2],face2[5],face3[7] = face3[7],face1[2],face2[5]
        face1[3],face2[1],face3[6] = face3[6],face1[3],face2[1]
    return [face1,face2,face3]

def pyraminxPuzzle(faceColors,moves):
    pyraminx = [[i]*9 for i in faceColors]
    upper,bottom,left,right = pyraminx
    for move in moves[::-1]:
        side = move[0].upper()
        if side == "U":
            faces = [upper,left,right]
        if side == "B":
            faces = [bottom,right,left]
        if side == "L":
            faces = [left,upper,bottom]
        if side == "R":
            faces = [right,bottom,upper]
        faces = rotate(move[0],faces)
        if len(move) == 2:
            faces = rotate(move[0],faces)
    print(upper)
    print(bottom)
    print(left)
    print(right)
    return [upper,bottom,left,right]
pyraminxPuzzle(faceColors,["b'", "u'", "R"])