from math import *
import timeit
#Description : Write a program that computes and prints the 1000th prime number.

#Initialize variables
print "The following is the 1000th prime number:"
primes = [3]
#index number
number = 3
#Total quantity of primes to find
N = 1000

#Generate odd integers greater than 1
#Check if prime list is equal to the quantity desired
while len(primes) < (N-1):
#Check if number is odd
    oddFlag = number%2
    if oddFlag:
        #Check if number is prime
        for prime in primes:
            #Module against all previously captured prime numbers
            primeFlag = number%prime
            if not primeFlag:
                    break
        if primeFlag:
            primes.append(number)
    number = number + 1
#Re-insert the only even entry into begining of list
primes.insert(0,2)
print primes[N-1]