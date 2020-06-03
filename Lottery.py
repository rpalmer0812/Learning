from random import choice

#lottery possibilities
userlist = [1, 61, 5, 3, 6, 7, 4, 9, 10, 13, 15, 'r', 't', 'v', 'u']

winner = choice(userlist)

def winner(userlist):
    i = 0
    win_list = []
    while i < 4:
        win_list.append(choice(userlist))
        i += 1
    return win_list

winning = winner(userlist)
print(winning)





my_ticket = [3, 5, 7, 4]
count = 0
active = True

while active:
    if my_ticket != winning:
        winning = winner(userlist)
        count += 1
    else:
        print(f"It took {count} times to win the lottery.")
        active = False
