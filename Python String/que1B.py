str1 = "JohnDipPeta"
str2 = "JaSonAy"
def get_middle_three_charactor(str1):
    mi = int(len(str1)/2)
    res = str1[mi -1:mi+2]
    print("Middle three charactorare:",res)
get_middle_three_charactor("johnDipPeta")
get_middle_three_charactor("JaSonAy")