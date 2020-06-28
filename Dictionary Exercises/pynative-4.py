import pprint

employees = ['Kelly', 'Emma', 'John']
defaults = {"designation": 'Application Developer', "salary": 8000}

final = {}

final = dict.fromkeys(employees, defaults)

pprint.pprint(final)
