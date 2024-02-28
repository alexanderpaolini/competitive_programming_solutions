# Note: This solution is wrong
m, n = map(int, input().split())
submissions = []
for i in range(m):
    submissions.append(input().split())
for i in range(len(submissions)):
    for j in range(len(submissions[i])):
        submissions[i][j] = int(submissions[i][j])
submissions = sorted(submissions)

def find_least_server(servers):
    """ Returns the index of the server that has the least current """
    min_time = servers[0][1]
    min_index = 0
    for i, s in enumerate(servers):
        if s[1] < min_time:
            min_time = s[1]
            min_index = i
    return min_index

# Total
# Current
arr = []
for _ in range(n):
    arr.append([0, 0])

time = 1
while len(submissions):
    # remove 1 from current for all
    for i in range(len(arr)):
        if arr[i][1]:
            arr[i][1] -= 1
    
    # for all subs matching time
    for sub in list(filter(lambda x: x[0] == time, submissions)):
        # find least
        least_server = arr[find_least_server(arr)]
        least_server[0] += sub[1]
        least_server[1] += sub[1]
    
    time += 1

print(" ".join(list(map(lambda x: str(x[0]), arr))))
