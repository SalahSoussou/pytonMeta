def find_factorial(n):
    if n==1:
        return 1
    else:
        return n*find_factorial(n-1)

print(find_factorial(5))
print(find_factorial(6))

# reves a string 

trial = "reversal"
print(trial[::-1])

def revers_recusrsional(str):
    if len(str) == 0:
        return str
    else:
        return revers_recusrsional(str[1:]) + str[0]

print(revers_recusrsional("hello word"))

