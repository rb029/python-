def find_digit_chars_symbols(sample_str):
    char_count = 0
    digit_count=0
    symbol_count=0
    for char in sample_str:
        if char.isalpha():
            char_count+=1
        elif char.isdigit():
            digit_count+=1
        else:
            symbol_count+=1
    print("Chars =",char_count, "digits =",digit_count,"Symbols =",digit_count)
sample_str ="P@yn2at&#i5ve"
print("total counts of chare , Digits and Symbols \n")
find_digit_chars_symbols(sample_str)