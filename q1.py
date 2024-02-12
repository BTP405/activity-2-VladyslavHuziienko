import math

def isPrime(x):
    """ Checking if number is prime
        isPrime() function takes one argument x - the nubmer it checks, the result - True if prime, False if not prime
        The function tries to find if the number x can be divided by any number in [2, x) without a remainder,
        if there is no such number, x - is a prime number.
    """
    for i in range(2, math.floor((x**0.5)+1)):
        if(x % i == 0):
            return False
    return True

def getPrimeNumbers(n):
    """ Getting the list of prime numbers
        getPrimeNumbers function takes on argument n - upper limit of the list, and returns the list of prime numbers between 2 and n
        The function iterates from 2 to n, and executes isPrime function for each number. If the return of isPrime is True, the number is added
        to the list.
    """
    prime_nums = []
    for i in range(2, n+1):
        if isPrime(i):
            prime_nums.append(i)
    return prime_nums

results = getPrimeNumbers(1000)
print(results)