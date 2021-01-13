P, X, Y = float(input()), float(input()), float(input())
S = X * 100 + Y
S = S * (P + 100) / 100
X2 = int(S // 100)
Y2 = int(S % 100)
print(X2, Y2)
