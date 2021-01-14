def namber():
    w = set(range(1, int(input()) + 1))
    n = input().split()
    while n != 'HELP':
        answer = str(input())
        if answer == "YES":
            w &= set(map(int, n))
        elif answer == "NO":
            w -= set(map(int, n))
        n = input().split()
        if str(n[0]) == 'HELP':
            return map(int, w)


print(*sorted(namber()))
