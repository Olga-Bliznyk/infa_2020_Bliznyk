N = list(map(int, input().split()))
i = 1
s = []
while i <= N[1]:
    n = int(input())
    s.append(n)
    i += 1
s.sort()
k = 0
sym = 0
for i in range(0, len(s)):
    if s[i] < N[0]:
        sym += s[i]
        if sym < N[0]:
            k += 1
print(k)
