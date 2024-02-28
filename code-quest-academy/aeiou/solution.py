# Submitted
import sys

numStrings = int(input())

for i in range(numStrings):
    print(
        len(list(filter(lambda x: x in [
            'a', 'e', 'i', 'o', 'u'], list(input()))))
    )
