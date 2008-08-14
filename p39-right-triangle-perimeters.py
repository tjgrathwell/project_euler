# * Recall that all primitive Pythagorean Triples, a^2 + b^2 = c^2 arise from the
# * form a = m^2 - n^2, b = 2mn, c = m^2 + n^2. Where m > n > 0 and m, n coprime,
# * and one of m or n is even.

from collections import defaultdict

def triangle(m,n):
    """ Not all non-primitive Pythagorean triples can be generated with this formula, but every primitive triple (possibly after exchanging a and b) arises in this fashion from a unique pair of coprime numbers m , n. """
    a = (m*m - n*n)
    b = 2 * m * n
    c = (m*m + n*n)
    return [a,b,c]

all_triangles = {}
triangles_by_length = defaultdict(list)
a,b,c = triangle(2,1)
m,n = 2,2
while True:
    a,b,c = sorted(triangle(m,n))
    triangle_length = a+b+c
    
    if triangle_length > 1000:
        if n == 1:  # we've gone as far as we can
            break
        else:       # trying the next m with a lower n might produce more results 
            m += 1
            n = 1
            continue
    else:
        bigger_length = triangle_length
        i = 1
        # This code is SUPER MESSY. It should be folded into a function similars(m,n,up_to=N) that finds all similar triangles starting with the primitive m,n and multiplying up.
        while bigger_length < 1000:
            an,bn,cn = a*i, b*i, c*i
            
            if (an,bn,cn) not in all_triangles:
                all_triangles[(an,bn,cn)] = 1
                triangles_by_length[bigger_length] += [(an,bn,cn)]

            i += 1
            bigger_length = triangle_length * i

    # set up next triangle
    if m == n:
        m += 1
        n = 1
    else:
        n += 1
        
max = 0
peri = 0
for k in triangles_by_length.keys():
    num = len(triangles_by_length[k])
    if num > max:
        max = num
        peri = k
    
print peri