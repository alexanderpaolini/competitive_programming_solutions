r, s = map(int, input().split())

# (area of table - (length - diameter)) / over area of table

print((s ** 2 - max(0, s - 2 * r) ** 2) / s ** 2)