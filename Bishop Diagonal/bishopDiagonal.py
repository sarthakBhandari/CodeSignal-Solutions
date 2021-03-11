#if two bishops lie on same diagonal, they will move to the opposite ends of the diagonal. Find the final posiitons
import string
def bishopDiagonal(b1, b2):
    a = string.ascii_lowercase
    #do they even lie on the same diagonal?
    c = abs(ord(b1[0]) - ord(b2[0])) == abs(int(b1[1]) - int(b2[1]))
    if not c:
        return sorted([b1,b2])
    else:
        #positive gradient
        if (a.find(b1[0])-a.find(b2[0]))/(int(b1[1])-int(b2[1]))>0:
            i,j = a.find(b1[0]),int(b1[1])
            while True:
                if j == 1 or i==0: break
                i -= 1
                j -= 1
            v1 = a[i] + str(j)
            k,l = a.find(b2[0]), int(b2[1])
            while True:
                if k==7 or l==8: break
                k += 1
                l += 1
            v2 = a[k] + str(l)
        #negative gradient
        else:
            i,j = a.find(b1[0]),int(b1[1])
            while True:
                if i==7 or j==1: break
                i += 1
                j -= 1
            v1 = a[i] + str(j)
            k,l = a.find(b2[0]), int(b2[1])
            while True:
                if k==0 or l==8: break
                k -= 1
                l += 1
            v2 = a[k] + str(l)
    return sorted([v1,v2])
print(bishopDiagonal("a1","h8"))