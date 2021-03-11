#the crossword must contain exactly four words;
#these four words should form four pairwise intersections;
#all words must be written either left-to-right or top-to-bottom;
#the area of the rectangle formed by empty cells inside the intersections isn't equal to zero.
#Given 4 words, find the number of ways to make a crossword following the above-described rules. 
#Note that two crosswords which differ by rotation are considered different.




def crosswordFormation(words):
    from itertools import permutations as perms
    from collections import defaultdict as ddic
    ans = 0
    for p in perms(words):
        M = ddic(int)
        a,b,c,d = p
        for i in range(2, min(len(a),len(b))):
            for p in range(len(a) - i):
                for q in range(len(b) - i):
                    M[a[p],a[p+i],b[q],b[q+i]] += 1
        for i in range(2, min(len(c),len(d))):
            for p in range(len(c) - i):
                for q in range(len(d) - i):
                    ans += M[c[p],d[q],c[p+i],d[q+i]]
    return ans
print(crosswordFormation(["crossword", "square", "formation", "something"]))



from itertools import permutations as perms
words = ["crossword","square","formation","something"]
counter = 0

for W in perms(words):
    h1,v1,v2,h2 = W
    for i in range(len(h1)-2):
        for k in range(0,len(v1)-2):
            if v1[k] == h1[i]:
                for j in range(i+2,len(h1)):
                    for l in range(0,len(v2)-2):
                        if v2[l] == h1[j]:
                            hoffset,voffset = j-i,l-k
                            for m in range(0,len(h2)-hoffset):
                                for n in range(k+2,len(v1)):
                                    try: v2[n+voffset]
                                    except: break
                                    else:
                                        if h2[m]==v1[n] and h2[m+hoffset]==v2[n+voffset]:
                                            counter += 1
print(counter)