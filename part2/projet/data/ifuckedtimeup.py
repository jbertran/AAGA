import csv

timesdict = {}

with open('time.csv', 'r') as f:
    reader = csv.reader(f)
    for size, timeval in reader:
        if not timesdict.get(size):
            timesdict[int(size)] = [float(timeval)]
        else:
            timesdict[int(size)].append(float(timeval))

for size, tlist in timesdict.items():
    timesdict[size] = sum(tlist) / float(len(tlist))

with open('tree_avg_times.csv', 'w') as f:
    for size, tval in timesdict.items():
        f.write('%d, %.5f\n' % (size, tval))
