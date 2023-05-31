list = []

for i in range(5):
    list_num = int(input('Enter 5 Numbers To Add In List: '))
    list.append(list_num)

print('''========================
========================''')

list.sort()
print(list)
print(f'The 2nd Highest Number In The list Is {list[-2]}')
