def sum(n):
    if n==1:
        return 0
    return n + sum(n-1)

print(sum(5))

