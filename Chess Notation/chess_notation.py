#chess notation
#r-rook,n-kinght,k-king,q-queen,p-pawn,b-bishop. lower case for black and upper case for white. consecutive spaces given as numbers
#the chess board is rotated 90 clockwise, find the new notation

#Approach
#put the values is a matrix form. chess board is 8 by 8
#rotate the matrix and then extract the values

notation = "bN2nrp1/n1nQn1n1/p1bPRPrb/n2Q1Nrb/Bn1nBRnB/Q1n1N1b1/qk1n1R2/Q1n2n1Q"
notation = [*notation]
matrix = [[]*8 for _ in range(8)]
j = 0
for i in notation:
    if len(matrix[j])==8: j+=1
    if i == "/": continue
    try:
        a = int(i)
        matrix[j] += a*"0"
    except ValueError:
        matrix[j].append(i)

result = ""
for i in zip(*matrix):
    #matrix[k] = list(i)[::-1]
    #k += 1
    result += "".join(i[::-1])
    result += "/"

p = 0
res = ""
for i in range(len(result)):
    if result[i] == "0": p+=1
    elif p and result[i]!= "0":
        res += str(p)
        p = 0
    if result[i] != "0": res += result[i]
print(res)
print(result)
