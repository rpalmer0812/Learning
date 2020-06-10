#CODEWARS

#accum("abcd") -> "A-Bb-Ccc-Dddd"
#accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
#accum("cwAt") -> "C-Ww-Aaa-Tttt"

s = 'abcd'
userlist = []

def accum(s):
    for i in s:
        userlist.append(i)
    return userlist

final = accum(s)
print(final)

def answer(a):
    for i in a:
        a * ()
