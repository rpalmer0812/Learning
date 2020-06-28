#!/Users/jc/opt/anaconda3/bin/python



from tcp_latency import *
import subprocess
import re
import statistics
from datetime import datetime

now = datetime.now()
print(f"\n{now}")
print("Network Performance Check")

process = subprocess.run('python tcp_latency.py --run 50 8.8.8.8', shell=True, stdout=subprocess.PIPE, universal_newlines=True)
output = process.stdout

final = re.findall(r'(?<=time=)[0-9.]+', output)
new_final = [float(i) for i in final]

def Average(lst):
    sum = 0
    for i in lst:
        sum += float(i)
    avg = sum / len(lst)
    return avg

#median_ping = round(statistics.median(new_final))
max_ping = round(float(max(new_final)))
min_ping = round(float(min(new_final)))
avg_ping = round(float(Average(new_final)))

def outliers(lst):
    outlier_list = []
    for i in lst:
        if i > (2 * avg_ping):
            outlier_list.append(i)
    return (outlier_list)

outlier_list = outliers(new_final)

if len(outlier_list) != 0:
    print(f"\nOutlier pings include:")
    print(outlier_list)
else:
    pass

print(f"\nMaximum ping: {max_ping}")
print(f"Minimum ping: {min_ping}")
#print(f"\nMedian ping: {median_ping}")
print(f"Average ping: {avg_ping}\n")

print("Network diagnosis:")
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

speedtest_process = subprocess.run('speedtest-cli --server 2629', shell=True, check=True, stdout=subprocess.PIPE, universal_newlines=True)
speedtest_output = speedtest_process.stdout

speedtest_final = re.findall(r'.+?(?=Mbit)', speedtest_output)

print(speedtest_final)
