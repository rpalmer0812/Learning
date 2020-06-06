def make_list(numbers):
    a = []
    for i in str(numbers):
        a.append(i)
    return a

n = input("Give me a number: ")

while len(str(n)) != 1:
    b = make_list(n)
    n = 0
    for items in b:
        n += int(items)

print(n)
