def mix_mixstring(s1,s2):
    first_char = s1[0] + s2[0]
    middle_char = s1[int(len(s1) / 2):int(len(s1) / 2) + 1] + s2[int(len(s2) / 2):int(len(s2) / 2) + 1]
    last_char = s1[len(s1) - 1] +s2[len(s2)-1]
    res = first_char + middle_char + last_char
    print("Mix string is :",res)
s1 ="America"
s2="Japan"
mix_mixstring(s1,s2)     