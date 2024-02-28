# Submitted
import ipaddress

num_cases = int(input())

for _ in range(num_cases):
    addy = input()

    try:
        a = ipaddress.ip_address(addy)
        print("VALID")
    except:
        print("INVALID")