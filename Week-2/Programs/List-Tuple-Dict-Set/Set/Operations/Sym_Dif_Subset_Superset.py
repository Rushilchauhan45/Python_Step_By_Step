'''
[1] Symmentric Difference : (A /_\ B)
--> It Returns Elemets Ither in A or B , But not returns both....
--> A ^ B
--> A.symmetric_difference(B) (Builtin Function)
'''

A = {1,2,3,4}
B = {5,2,3,6}

print( A ^ B)
print( A.symmetric_difference(B))


'''
[2] SUBSET : (A < B ) 
--> It Checks If All Elements of A Is Present In B ...
--> A.issubset(B) (Builtin Function)
'''
A = {1,2,3,4}
B = {1,2,3,4}

print(A.issubset(B))

'''
[3] SUPERSET : (A > B)
--> It Checks If All Elements of B is Present In A ...
--> A.superset(B) (Builtin Function)
'''

A = {1,2,3,4}
B = {1,2,3,4}

print(A.issuperset(B))