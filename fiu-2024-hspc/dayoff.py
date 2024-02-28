# Note: This one was written by my teamate
lol=input()
stones=list(map(int,input().split()))
dp=[]
for i in range(len(stones)):
    dp.append([])
    dp[i].append(0)
    dp[i].append(0)

for i in range(len(dp)-1,-1,-1):
    yourScore=0
    if i+3<len(dp):
        possible=[dp[i+1][0],dp[i+2][0],dp[i+3][0]]
        bestScore=min(possible)
        bestIndex=possible.index(bestScore)
        if bestIndex==0:
            yourScore+=stones[i]
        elif bestIndex==1:
            yourScore+=stones[i]+stones[i+1]
        elif bestIndex==2:
            yourScore+=stones[i]+stones[i+1]+stones[i+2]
        dp[i][0]=yourScore+dp[i+bestIndex+1][1]
        dp[i][1]=bestScore

    elif i+2<len(dp):
        possible=[dp[i+1][0],dp[i+2][0],0]
        bestScore=min(possible)
        bestIndex=possible.index(bestScore)
        if bestIndex==0:
            yourScore+=stones[i]
        elif bestIndex==1:
            yourScore+=stones[i]+stones[i+1]
        dp[i][0]=yourScore
        dp[i][1]=bestScore

    elif i+1<len(dp):
        possible=[dp[i+1][0],0]
        bestScore=min(possible)
        bestIndex=possible.index(bestScore)
        if bestIndex==0:
            yourScore+=stones[i]
        dp[i][0]=yourScore
        dp[i][1]=bestScore

    else:
        dp[i][0]=stones[i]

if dp[0][0]>dp[0][1]:
    print("Aaarush")
elif dp[0][0]<dp[0][1]:
    print("Bronit")
else:
    print("Tie")
