#!/usr/bin/env python

print("How many primes do you want to find?")

target = int(raw_input())

print("")

primes = 0

i = 2

while primes < target:
    
    prime = True

    for j in range(2,i):
        if i % j == 0:
            prime = False
            break

    if prime:
        primes = primes + 1
        print("[{}] {}").format(primes,i)

    i = i+1
