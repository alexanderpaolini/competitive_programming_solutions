# Submitted
num_cases = int(input())

for _ in range(num_cases):
    str1,str2 = input().split("|")
    anagram = True
    if str1 == str2:
        anagram = False
    
    l1 = list(str1)
    l2 = list(str2)
    for c in l1:
        if c in l2:
            l2.remove(c)
        else: 
            anagram = False
    
    if len(l2) > 0:
        anagram = False

    str3 = "ANAGRAM" if anagram else "NOT AN ANAGRAM"
    print(f"{str1}|{str2} = {str3}")