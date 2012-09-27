import csv
import random
import string
from timeit import Timer

def randomKey(n):
    s = ''
    for i in xrange(n):
        s += random.choice(string.lowercase)
    return s

if __name__ == '__main__':
    for n in [10,100,500,1000,2000,5000,10000,50000,100000,500000,1000000,5000000]:
        print n
        keys = set()
        for i in xrange(n):
            keys.add(randomKey(10))

        # Write random key, values to csv
        with open('flatfile.csv', 'wb') as f:
            writer = csv.writer(f)
            for s in keys:
                writer.writerow([s,s[::-1]])

        setup = """
from __main__ import csv, keys, random, n
"""
        lookup = """
# Read csv to produce dictionary
d = {}
with open('flatfile.csv', 'rb') as f:
    reader = csv.reader(f)
    for row in reader:
        d[row[0]] = row[1]

# Timed lookups
l = list(keys)
for i in xrange(n/4):
    d[random.choice(l)]
"""
        print Timer(lookup, setup).timeit(5) / 5