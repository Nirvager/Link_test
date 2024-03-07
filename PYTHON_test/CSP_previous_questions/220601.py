import math
n = int(input())
a = list(map(int, input().split()))
average = sum(a) / n
total = 0
for num in a:
    total += (num - average) ** 2
total /= n
for num in a:
    print((num - average) / math.sqrt(total))