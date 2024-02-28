# Wrong answer (not sure why)
num_cases = int(input())

for _ in range(num_cases):
    volume, rate_in, rate_out = map(int, input().split())
    waste = round(volume / (rate_in - rate_out) * rate_out)
    print(waste)
