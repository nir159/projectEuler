"""
help functions:

prime_list - returns list of primes from 1 to n
nth_prime - returns the n'th prime number
is_prime - if n is prime returns True

is_triangular - returns True if n triangular
nth_triangular - returns the n'th triangular number

nth_fib - returns the n'th in the Fibonacci sequence
nth_fib_higher_numbers - recursion will exceed after n = 500

recurring_sequence_fraction - returns the length of the recurring seqence in 1/n fraction

get_divisors -  returns a list of all divisors of n
"""

def prime_list(n):
    indexes = [True] * n
    for i in range(3,int(n**0.5)+1,2):
        if indexes[i]:
            indexes[i*i::2*i]=[False]*((n-i*i-1)//(2*i)+1)
    return list([2] + [i for i in range(3,n,2) if indexes[i]])

"""
%2==0 not prime
3*3 - not prime
3*3 + 3*2
3*(3+2) - not prime
3*3 + 3*2 + 3*2....
"""
def is_prime(n):
    if n in prime_list(n+1):
        return True
    return False


def nth_prime(n):
    prime_list = [2]
    num = 3
    while n > len(prime_list):
        for i in prime_list:
            if num % i:
                continue
        else:
            prime_list.append(num)
        num += 2
    return prime_list[n-1]


def is_triangular(n, ver = False):
    num = 0
    i = 1
    while n > num:
        num += i
        i += 1
        if ver == True:
            print(num)
    if n == num:
        return True
    return False
    
    
def nth_triangular(n):
    return n*(n+1)//2
    

INDEX_CACHE = {0:1, 1:1}
def nth_fib(n):
    if n in INDEX_CACHE:
        return INDEX_CACHE[n]
    
    curr = nth_fib(n-1) + nth_fib(n-2)
    INDEX_CACHE[n] = curr
    return curr

def nth_fib_higher_numbers(n):
    a = 1
    b = 1
    curr_n = 2
    while curr_n != n:
        a = a+b
        curr_n += 1
        
        if curr_n == n:
            return a
        
        b = a+b
        curr_n += 1
    return b

def recurring_sequence_fraction(n):
    if n % 2 == 0 or n % 5 == 0 or n == 1:
        return -1
    k = 1
    while pow(10,k,n) != 1:
        k += 1
    return k
    
    
from functools import reduce
def get_divisors(n):
    return list(set(reduce(list.__add__, ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0))))
