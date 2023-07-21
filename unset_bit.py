def unset_bit(A, B):
    n = (1 << B)
    if A & n:
        A = A & ~n
    return A
A = int(input())
B = int(input())
print(unset_bit(A, B))
