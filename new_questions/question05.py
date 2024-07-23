def out(a,b):
    square = a ** 2
    def add(a , b):
        return  a+b
    fun= add(a,b)
    return fun + 5
result = out(5,10)
print(result)