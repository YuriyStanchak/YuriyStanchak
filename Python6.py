A = int(input())
B = int(input())
C = int(input())

while A < B:
    print(A, '<', B)
    A += C

if A== B:
    print(A, '=', B)
elif A > B:
    print(A, '>', B)
