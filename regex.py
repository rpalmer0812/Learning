final = ['18.76', '17.96', '16.47', '16.35', '19.88', '18.58', '17.18', '22.05', '19.11', '19.32', '17.05', '18.32', '19.14', '46.42', '17.99', '16.59', '21.15', '18.24', '42.27', '17.68', '19.85', '16.57', '16.81', '20.77', '18.81', '20.5', '18.68', '16.97', '17.34', '16.45', '20.97', '16.95', '16.63', '27.77', '1027.09', '17.33', '17.17', '17.11', '19.46', '34.97', '19.75', '16.24', '17.01', '21.4', '19.13', '17.76', '16.89', '18.1', '18.31', '20.85']

new_list = [float(i) for i in final]
print(new_list)

min_ping = min(new_list)

print(min_ping)
