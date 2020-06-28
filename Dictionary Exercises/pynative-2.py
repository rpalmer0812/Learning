dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}

def merge_dict(d1, d2):
    combined = {**d1, **d2}
    return combined

final = merge_dict(dict1, dict2)
print(final)
