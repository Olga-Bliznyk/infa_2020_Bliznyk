n = int(input())
prs = []
for i in range(n):
    prs.append(input().split())
for i in prs:
    i[1] = int(i[1])
prs.sort(key=lambda i: i[1], reverse=True)
for i in prs:
    print(i[0])
