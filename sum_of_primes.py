# Initialize a list
N = int(input())
primes = []
sum_primes = 0
for possiblePrime in range(2, N):

    # Assume number is prime until shown it is not.
    isPrime = True
    for num in range(2, possiblePrime):
        if possiblePrime % num == 0:
            isPrime = False

    if isPrime:
        primes.append(possiblePrime)


for i in iter(primes):
    sum_primes += i
print(sum_primes)

