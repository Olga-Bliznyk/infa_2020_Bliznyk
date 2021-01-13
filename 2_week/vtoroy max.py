N = int(input())
big_est = 0
sub_big_est = 0
while N != 0:
    if N >= big_est:
        sub_big_est = big_est
        big_est = N
    elif N >= sub_big_est:
        sub_big_est = N
    N = int(input())
print(sub_big_est)
