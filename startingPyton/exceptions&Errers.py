def divide(a,b):
    return a/b
    
try:
    ans = divide(40, 0)
except Exception as e:
    print('!! =>  ',e)
    print(e.__class__)