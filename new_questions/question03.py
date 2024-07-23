def calculation(a,b):
    addition= a + b 
    subtraction = a - b
    return addition , subtraction
result = calculation(40 , 10)
print(result)    

def calculation(a, b):
    return a + b, a - b

# get result in tuple format
# unpack tuple
add, sub = calculation(40, 10)
print(add, sub)
