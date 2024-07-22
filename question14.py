num = 76542
num1 = 0
while num>0 :
    x = num %10
    num1 =(num1 * 10 ) + x
    num = num // 10
print ("Reverse Number", num1)    
