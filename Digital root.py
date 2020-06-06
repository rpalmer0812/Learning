#CODEWARS

#Digital root is the recursive sum of all the digits in a number.

#Given n, take the sum of the digits of n. If that value has more than one digit, continue reducing in this way until a single-digit number is produced. This is only applicable to the natural numbers.


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
