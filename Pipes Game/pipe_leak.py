#there are 7 types of pipes in the game
#1 - vertical pipe, 2 - horizontal pipe, 3-6 - corner pipes, and 
#7 - two pipes(one hor & one ver) crossed in the SAME cell (note that these pipes are not connected)
#for a given arrangement return the numbers of cells with water if all pipes reach their destination
#else return -X where X is the number of cells with water before something goes wrong(leak, or wrong destination)


state = ["Aa7272727777"]



from collections import defaultdict as ddic
import string
def pipesGame(state):
    sources = []#contains the id of source and its coordinates
    for i in range(len(state)):
        for j in range(len(state[0])):
            if state[i][j] in string.ascii_lowercase: sources.append([state[i][j].upper(),i,j])
            state[i] = [j for j in state[i]]#turning the map into a matrix
    if len(sources)==0: return 0 #no source then 
    
    D = ddic(int)#this keeps track of seven-type pipes

    #this contains the no.of pipes after starting along a path where a pipe hits a leak or reaches wrong destination
    leak = []
    def play_game(i,j,pipe,source,last_move=None):
        #print(i,j,last_move,pipe)

        #if u reach the end
        if i<0 or i>=len(state) or j<0 or j>=len(state[0]):
            leak.append(pipe-1)
            return (pipe-1,source,"reached the end")
        #keeping track of seventype pipe -- put this statement below above - cost me 40k coins
        if state[i][j] == "7":
            D[(i,j,last_move)] += pipe
    
        #if u reach a sink
        if state[i][j] in string.ascii_uppercase:
            if state[i][j] == source:
                return (pipe-1,source,"right destination")
            else:
                leak.append(pipe-1)
                return(pipe-1,source,"wrong destination")
        #if u reach an actual leak
        if state[i][j] == "0":
            leak.append(pipe-1)
            return (pipe-1,source,"leak")

        if pipe==0: #when u take a corner pipe on first move the count is decreased by 1
            if (last_move=="U" and i>=1 and state[i-1][j] in ["1","4","3","7"]):
                if state[i-1][j]=="1" or state[i-1][j]=="7": r = play_game(i-1,j,pipe+1,source,"U")
                elif state[i-1][j] == "4": r = play_game(i-1,j-1,pipe+2,source,"L")
                elif state[i-1][j] == "3": r = play_game(i-1,j+1,pipe+2,source,"R")
            elif (last_move=="D" and i+1<len(state) and state[i+1][j] in ["1","5","6","7"]):
                if state[i+1][j]=="1" or state[i+1][j]=="7": r = play_game(i+1,j,pipe+1,source,"D")
                elif state[i+1][j] == "5": r = play_game(i+1,j-1,pipe+2,source,"L")
                elif state[i+1][j] == "6": r = play_game(i+1,j+1,pipe+2,source,"R")
            elif (last_move=="R" and j+1<len(state[0]) and state[i][j+1] in ["2","4","5","7"]):
                if state[i][j+1]=="2" or state[i][j+1]=="7": r = play_game(i,j+1,pipe+1,source,"R")
                elif state[i][j+1] == "4": r = play_game(i+1,j+1,pipe+2,source,"D")
                elif state[i][j+1] == "5": r = play_game(i-1,j+1,pipe+2,source,"U")
            elif (last_move=="L" and j >= 1 and state[i][j-1] in ["2","3","6","7"]):
                if state[i][j-1]=="2" or state[i][j-1]=="7": r = play_game(i,j-1,pipe+1,source,"L")
                elif state[i][j-1] == "3": r = play_game(i+1,j-1,pipe+2,source,"D")
                elif state[i][j-1] == "6": r = play_game(i-1,j-1,pipe+2,source,"U")
            else: return 0
        else:
            if state[i][j] == "1":
                r = play_game(i+1,j,pipe+1,source,"D") if last_move=="D" else play_game(i-1,j,pipe+1,source,"U")
            elif state[i][j] == "2":
                r = play_game(i,j+1,pipe+1,source,"R") if last_move=="R" else play_game(i,j-1,pipe+1,source,"L")
            elif state[i][j] == "3":
                r = play_game(i,j+1,pipe+1,source,"R") if last_move=="U" else play_game(i+1,j,pipe+1,source,"D")
            elif state[i][j] == "4":
                r = play_game(i+1,j,pipe+1,source,"D") if last_move=="R" else play_game(i,j-1,pipe+1,source,"L")
            elif state[i][j] == "5":
                r = play_game(i-1,j,pipe+1,source,"U") if last_move=="R" else play_game(i,j-1,pipe+1,source,"L")
            elif state[i][j] == "6":
                r = play_game(i,j+1,pipe+1,source,"R") if last_move=="D" else play_game(i-1,j,pipe+1,source,"U")
            elif state[i][j] == "7":
                if last_move=="U": r = play_game(i-1,j,pipe+1,source,"U")
                elif last_move=="D": r = play_game(i+1,j,pipe+1,source,"D")
                elif last_move=="R": r = play_game(i,j+1,pipe+1,source,"R")
                elif last_move=="L": r = play_game(i,j-1,pipe+1,source,"L")
        return r

    pipes = []#keeps track of pipe lengths of ALL PATHS, note: pipe 7 could be repeated
    initial_move = ["R","L","U","D"] #check all directions from the source
    for i in sources:
        for j in initial_move:
            a = play_game(i[1],i[2],0,i[0],j)
            if a: pipes.append(a)

    counter = 0#counts pipes with water, note: pipe 7 could be repeated
    for i in pipes:
        if leak: counter -= min(min(leak),i[0])#if leak choose the smallest b/w (leak constant,finished_path)
        else: counter += i[0]#if no leak just add the lenght of path/no.of pipes. Note that seven-type pipe maybe be repeated

    E = ddic(int)
    seven = 0#this will be number of extra "seven-type pipes"
    for i,j in D.items():
        if not E[i[:2]]: E[i[:2]] += j
        elif E[i[:2]]:
            if leak:#only reduce if if passes through both "sevent-type" pipes before hitting leak somewhere
                if max(E[i[:2]],j) <= min(leak): seven += 1
            else: seven += 1
    print(counter)
    print(seven)
    if counter==0: return 0
    return counter - seven if counter > 0 else counter + seven