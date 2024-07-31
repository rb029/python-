input_str = "PYnative29@#8496"
total = 0 
cnt = 0
for char in input_str:
    if char.isdigit():
        total+= int(char)
        cnt+= 1
avg = total/cnt
print("Sum is :", total, "Average is :",avg)

import re

input_str = "PYnative29@#8496"
digit_list = [int(num) for num in re.findall(r'\d', input_str)]
print('Digits:', digit_list)

# use the built-in function sum
total = sum(digit_list)

# average = sum / count of digits
avg = total / len(digit_list)
print("Sum is:", total, "Average is ", avg)