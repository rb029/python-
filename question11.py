lower = int(input("Enter the lower limit:")) 
upper = int(input("Enter the upper limit:"))
for num in range (lower , upper+1):
    if num > 1:
        for j in range (2,num):
            if num % j == 0:
                break
        else:
            print(num)    
start = 25
end = 50
print("Prime numbers between " , start , "and", end ,"are:")
for num in range (start, end+1):
    if num > 1:
        for i in range (2,num):
            if(num%i)==0:
                break
        else:
            print(num)    
        
           


