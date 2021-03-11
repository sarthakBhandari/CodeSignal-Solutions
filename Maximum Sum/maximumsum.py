#given integers in an array a, and different index ranges in an array q. Eg: a = [1,2,3], q = [[0,1],[1,2]]
#sort the array a in such a way that sum of all range queries is maximum, return the total sum


#sorts the array and also finds the sum
from collections import defaultdict as ddic

a = [9, 7, 2, 4, 4]
q = [[1, 3], [1, 4], [0, 2]]

D = ddic(int)

#specifying index by range overlapping value
for i in range(len(a)):
    c = 0
    for j in q:
        if i in range(j[0],j[1]+1): c += 1
    D[i] += c

#sorting the dictionary by value
b = sorted(D.items(), key = lambda kv:(kv[1]))
vals = sorted(a)

#sorting a
while len(vals):
    a[b.pop(-1)[0]] = vals.pop(-1)

#finding the sum
s = 0
for i in q:
    s += sum(a[i[0]:i[1]+1])
print(s)



#different sol
def maximumSum(A, Q):
    c = [0]*len(A)
    for l, r in Q:
        for i in range(l, r+1):
            c[i] += 1
    return sum(a*b for a, b in zip(sorted(A), sorted(c)))
    