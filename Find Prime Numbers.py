value = int(input("Enter A Maximum Number: "))
print('''--------------------------
--------------------------''')
prime_nums = []

for i in range(2, value):
    for j in range(2, i):
        if (i % j) == 0:
            break
    else:
        prime_nums.append(i)

print(f'Prime Numbers Under {value} Are: {prime_nums}')
