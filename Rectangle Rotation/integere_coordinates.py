#find the number of integer coordinates in a rectangle that is rotated by 45 degrees
import math
a = 6
b = 4
count = 0
maxx = math.floor((a+b)/(2*math.sqrt(2)))
p = a/math.sqrt(2)
q = b/math.sqrt(2)
for x in range(-int(maxx),int(maxx)+1):
    for y in range(-int(maxx),int(maxx)+1):
        if (y<=p-x) and (y>=x-q) and (y<=x+q) and (y>=-x-p):
            #print(x,y)
            count += 1
print(count)
#or
def rectangleRotation(a, b):
    [m, n] = [int(math.floor(x / math.sqrt(2))) for x in (a, b)]
    return m * n + (m + 1) * (n + 1) - (m + n) % 2

def f(a,b):#only valid for 45 degrees
    root2 = math.sqrt(2)
    odd_points = (2*math.floor(a/2 * 1/root2) + 1)*(2*math.floor(b/2 * 1/root2) + 1)
    even_points = (2*math.floor((a/2 + 1/root2)*1/root2))*(2*math.floor((b/2 + 1/root2)*1/root2))
    return odd_points + even_points
print(f(6,4))