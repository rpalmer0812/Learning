from tcp_latency import *
import subprocess
import re
import statistics

process = subprocess.run('python tcp_latency.py --run 50 8.8.8.8', shell=True, check=True, stdout=subprocess.PIPE, universal_newlines=True)
output = process.stdout


final = re.findall(r'(?<=time=)[0-9.]+', output)

#print(final)

new_final = [float(i) for i in final]
#print(new_final)

#def toInt(lst):
#    for i in lst:
#        new_final = float(final.pop(i))
#    return new_final

#new_list = toInt(final)
#print(new_list)

def Average(lst):
    sum = 0
    for i in lst:
        sum += float(i)
    avg = sum / len(lst)
    return avg

def median_value(userlist):
    med_ping = 0
    med_ping = statistics. median(userlist)
    return med_ping

m_value = median_value(final)


median_ping = median_value(new_final)
max_ping = round(float(max(new_final)))
min_ping = round(float(min(new_final)))
avg_ping = round(float(Average(new_final)))

print(f"\nMaximum ping: {max_ping}")
print(f"Minimum ping: {min_ping}")
print(median_ping)
print(f"\nAverage ping: {avg_ping}")

if avg_ping < 20 and max_ping < 25:
    print("Internet is looking good.\n")
elif avg_ping < 20 and max_ping > 24:
    print("Internet is generally smooth with some odd spikes.\n")
elif avg_ping > 39 and max_ping > 24:
    print("Internet is extremely congested.\n")
elif avg_ping > 19 and max_ping > 24:
    print("Internet is congested and is noticeably impacted.\n")

#Regex.Match(@"""id"":143331539043251,", @"""id"":([0-9]+),").Groups[1].Value

#ping_output = subprocess.run('python tcp_latency.py --run 5 8.8.8.8', shell=True)

#print(ping_output)
