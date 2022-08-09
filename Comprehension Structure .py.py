# List Comprehension 
test = [i for i in range(10)]
print (test)

# Dict Comprehension
test2 = {i : i*2 for i in range(10)}
print(test2)

# Lamda
f = lambda x : x*2
print(f(2))

# map
test3 = list(map(lambda x : x+1 , [1,2,3]))
print(test3)