num_cases = int(input())

for _ in range(num_cases):
    s1 = input()
    s2 = input()

    counter = 0
    length = len(s1)
    
    for i in range(len(s1)):
        new_s = s1[:i] + s1[(i + 1):]
        
        if new_s == s2:
            counter += 1

    for i in range(max(counter, length), 0, -1):
        if counter % i == 0 and length % i == 0:
            counter = int(counter / i)
            length = int(length / i)

    print(f"{counter}/{length}")