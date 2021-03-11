#given position of a black pawn and a white pawn determine whose going to win
#black pawn moves from top row to bottom row, white from bottom row to top row
# initally 1st and 8th row are never occupied
def pawnRace(white, black, toMove):
    
    def make_move(player,w_pos,b_pos):
        print(player,w_pos,b_pos)
        other_player = "w" if player=="b" else "b"
        
        #reached the end
        if player == "b" and b_pos[1] == "2": return player
        if player == "w" and w_pos[1] == "7": return player
            
        #if adjacent
        if abs(ord(w_pos[0]) - ord(b_pos[0])) == 1:
            if ord(w_pos[1]) - ord(b_pos[1]) == -1: return player
            if abs(ord(w_pos[1]) - ord(b_pos[1])) == 5: return other_player
            
            if b_pos[1] == "7":
                if abs(ord(w_pos[1]) - ord(b_pos[1])) == 2 and player=="w": return "b"#if player=b move 2
                if abs(ord(w_pos[1]) - ord(b_pos[1])) == 3 and player=="b": return "b"#if player=w move 2
                if abs(ord(w_pos[1]) - ord(b_pos[1])) > 3: return "b"

            if w_pos[1] == "2":
                if abs(ord(w_pos[1]) - ord(b_pos[1])) == 2 and player=="b": return "w"#if player=w move 2
                if abs(ord(w_pos[1]) - ord(b_pos[1])) == 3 and player=="w": return "w"#if player=b move 2
                if abs(ord(w_pos[1]) - ord(b_pos[1])) > 3: return "w"  
                    
        #same col - NOT ALWAYS DRAW: WASTED 40000 coins to find this edge case
        if b_pos[0] == w_pos[0]:
            if int(b_pos[1]) < int(w_pos[1]):
                if 8-int(w_pos[1])==int(b_pos[1])-1: return player
                if 8-int(w_pos[1])<int(b_pos[1])-1: return "w"
                if int(b_pos[1])-1<8-int(w_pos[1]): return "b"
            return "draw"

        #make move
        if player == "w":
            if w_pos[1] == "2":
                w_pos = w_pos[0] + str(int(w_pos[1])+2)
            else: w_pos = w_pos[0] + str(int(w_pos[1])+1)
            a = make_move("b",w_pos,b_pos)
        if player == "b":
            if b_pos[1] == "7":
                b_pos = b_pos[0] + str(int(b_pos[1])-2)
            else: b_pos = b_pos[0] + str(int(b_pos[1])-1)
            a = make_move("w",w_pos,b_pos)

        return a
    
    result = make_move(toMove,white,black)
    if result == "b": result = "black"
    if result == "w": result = "white"
    return result
print(pawnRace("c5","d7","w"))