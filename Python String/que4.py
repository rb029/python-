str1= "PYnAtivE"
print('Orijional String:',str1)
lower=[]
upper=[]
for char in str1:
    if char.islower():
        lower.append(char)
    else:
        upper.append(char)
sorted_string = ''.join(lower+upper)
print('Result',sorted_string)    