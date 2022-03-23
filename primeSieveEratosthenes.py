import numpy as np
def prime_sieve(top_lim,limit=500000):
    """ Use the sieve of Erathosthenes to generate an array of primes
    arguments:
    top_lim - the highest number you'd like to generate up to
    limit - the highest number of iterations you're willing to allow (Defaut 500000)"""
    arr = np.concatenate((np.array([2]),np.arange(3,top_lim,2)))
    change=True
    min_num=2
    len_arr = 1
    # will loop up until the sqrt of your top limit
    limit_check = top_lim**0.5
    while change==True:
        # find the lowest number that you haven't already divided by
        min_num = np.min(arr[arr>min_num])
        # sieve - remove all numbers divisible or less than your min
        arr=arr[(arr%min_num!=0)|(arr<=min_num)]
        if min_num>=limit_check:
            change=False
        limit_check+=1
        if limit_check>limit:
            change=False
    # convert to np.float64
    arr=np.array(arr, dtype=np.float64)
    return arr
