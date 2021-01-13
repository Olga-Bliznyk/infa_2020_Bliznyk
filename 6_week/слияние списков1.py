def merge(a, b):
    i = 0
    j = 0
    k = 0
    c = list(range(len(a)+len(b)))
    while i < len(a) and j < len(b):
            if a[i] <= b[j]:
                c[k] = a[i]
                i += 1
            else:
                c[k] = b[j]
                j += 1
            k += 1
    c[k:] = a[i:] + b[j:]
    return c

A = list(map(int, input().split()))
B = list(map(int, input().split()))
print(*merge(A, B))
