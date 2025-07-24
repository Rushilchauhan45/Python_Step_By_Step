'''
[1] UNION : (A U B)
--> Combines All Unique Elements...
--> A | B (Operator Form)
--> A.union(B) (Builtin Function)
'''

A = {1,2,3,4,5}
B = {6,7,8,9,10}

print(A | B)
print(A.union(B))

'''
[2] INTERSECTION : (A Intersection B)
--> It Gives Only Common elemets..
--> A & B (Operator Form)
--> A.intersection(B) (Builtin Function)
'''

A = {1,2,3,4,5}
B = {6,1,8,3,10}

print( A & B )
print(A.intersection(B))