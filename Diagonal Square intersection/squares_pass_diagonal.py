#find number of squares diagonal passes through for a given rectangular grid -- HARD
#this question includes the 2 extra cells when the diagonal goes through the corner
# but the formula is q(m/q + n/q - 1) == m + n - q, where q is gcd or hcf. explaination below

#First, suppose that N and M have no common factor. Then the diagonal line doesn't go through any intersections, so each time 
# it crosses a horizontal or vertical grid line, it adds 1 to the number of squares touched. And to get from the top left to 
# the bottom right, it must pass through N−1 vertical grid lines and M−1 horizintal grid lines. Counting the orginal square in 
# the top left, this gives a total of 1+(N−1)+(M−1)=N+M−1 squares touched.

#Now suppose that N and M have a common factor. Let q be the largest common factor of N and M. Then N/q and M/q have no common 
#factors, so we can break the problem up into q smaller rectangles strung along the diagonal, each of size N/q×M/q; and in 
#each such rectangle the number of squares visited is N/q+M/q−1. So the total number of squares visited is q×(N/q+M/q−1)=N+M−q.

#Hence in all cases the number of squares touched is N+M−q. 

#now modifying a bit for this question, m + n - q + (q-1)(2) = m + n + q - 2
n = 10
m = 4
import math
print(m+n+math.gcd(m,n)-2)