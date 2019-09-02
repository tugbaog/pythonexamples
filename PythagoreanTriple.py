N = int(input())
for a in range(N//2):
    for b in range(N//3):
        c = N - a - b
        if c*c == a*a + b*b:
            print(a, b, c)
