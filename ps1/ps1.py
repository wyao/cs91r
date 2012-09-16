import random
from optparse import OptionParser
import bintrees #from http://pypi.python.org/pypi/bintrees/0.3.0
from timeit import Timer

def bin_search(lst,n):
    l,r = 0,len(lst)

    while (l<r):
        m = (l+r)/2
        val = lst[m]
        if val < n:
            l = m +1
        elif val > n:
            r = m
        else:
            return True
    return False

if __name__ == '__main__':
    # Parse options
    parse = OptionParser()

    parse.add_option('-n', type='int', default=100,
        help='Size of unique random sample')
    parse.add_option('-m', type='int', default=10,
        help='Size of unique lookup sample')
    parse.add_option('-r', type='int', default=1000,
        help='Maximum range of samples')
    parse.add_option('-i', type='int', default=100,
        help='Number of iterations to perform each time test')    

    (options, args) = parse.parse_args()
    iterations = options.i

    print 'Sample Size:', options.n, ' Lookup Size: ', options.m, \
        ' Sample Range:', options.r, ' Iterations:', iterations

    # Generate unique numbers
    unsorted = random.sample(xrange(100000), options.n)

    # Sorted list
    ordered = list(unsorted)
    ordered.sort()

    # Hash table
    hashT = {}
    for i in ordered:
        hashT[i] = True

    # Red black binary search tree
    rbTree = bintrees.RBTree(hashT)

    # Generate random numbers to look up
    lookup = [random.randint(0,options.r-1) for _ in xrange(options.r)]

    # Perform lookup on unordered list
    result = []
    setup1 = """
from __main__ import lookup
from __main__ import unsorted
"""
    unsorted_lookup = """
for i in lookup:
    i in unsorted
"""
    result.append((Timer(unsorted_lookup, setup1).timeit(iterations) / iterations, \
        'unordered list'))

    
    # Perform binary search lookup on sorted list
    setup2 = """
from __main__ import lookup
from __main__ import ordered
from __main__ import bin_search
"""
    ordered_lookup = """
for i in lookup:
    bin_search(ordered, i)
"""
    result.append((Timer(ordered_lookup, setup2).timeit(iterations) / iterations, \
        'ordered list'))

    # Perform lookup on hash table
    setup3 = """
from __main__ import lookup
from __main__ import hashT
"""
    hashT_lookup = """
for i in lookup:
    hashT.has_key(i)
"""
    result.append((Timer(hashT_lookup, setup3).timeit(iterations) / iterations, \
        'hash table'))

    # Perform lookup on rbTree
    setup4 = """
from __main__ import lookup
from __main__ import rbTree
"""
    rbTree_lookup = """
for i in lookup:
    rbTree.get(i)
"""
    result.append((Timer(rbTree_lookup, setup4).timeit(iterations) / iterations, \
        'rbTree'))

    # Present result
    result.sort()

    for i in result:
        print i[1] + ',',
    print
    for i in result:
        print i[0],
    print

    """
    # Sanity check
    w = [i in unsorted for i in lookup]
    x = [bin_search(ordered, i) for i in lookup]
    y = [hashT.has_key(i) for i in lookup]
    z = [rbTree.get(i)==True for i in lookup]

    assert(w==x==y==z)
    """