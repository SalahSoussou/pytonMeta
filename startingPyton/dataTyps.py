# === Lists === #
list1 = [1, 3 , 4,'HI', True]

print(*list1) #1 3 4 HI True
print(list1, sep= " ") # [1, 3, 4, 'HI', True]

list1.insert(3,5) # (index, value)
print(*list1) #1 3 4 5 HI True

list1.append(6)
print(*list1) #1 3 4 5 HI True 6


list2 = [100.00,7,0,["test", 'hello'], 5]

for e in list2:
    print(e)
"""
100.0
7
0
['test', 'hello']
5
"""

# === Tuples === #
# tule valus is imutabl
my_tupel = (1,'string', 4.5, True)
print(my_tupel) #(1, 'string', 4.5, True)
print(my_tupel[1]) # string
print(my_tupel.count('string'))
print(my_tupel.index(4.5))# 2

# === Sets === #

my_set =        {1, 2, 3, 4, 5, 5}

print(my_set) # {1, 2, 3, 4, 5} ^  no repitation

my_set.add(6)
print(my_set) # {1, 2, 3, 4, 5, 6}

my_set.remove(2)
print(my_set) # {1, 3, 4, 5, 6}

my_set.discard(3)
print(my_set) # {1, 4, 5, 6}

print(my_set.union({7, 8, 9}))# {1, 4, 5, 6, 7, 8, 9}
print(my_set | {10, 11})# {1, 4, 5, 6, 10,11}

# === Dictionaries === #

my_dec = {1: 'Coffee', 2: 'Tea', 3:'Juice'}
print(my_dec[2])

my_dec[2] = 'Mint Tea'
print(my_dec)

nums = 43
for i in nums:
    print(i)
