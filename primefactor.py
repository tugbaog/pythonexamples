N = int(input())

primeFactor = []

for i in range(N//2):
    if N % 2 == 0:
        primeFactor.append(2)
        N = N / 2

for i in range(3, int(N)+1, 2):
    if N % i == 0:
        primeFactor.append(i)
        N = N/i

print(primeFactor)
