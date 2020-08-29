x = list(map(int, input().split()))

n = x[0]
k = x[1]

y = n % k
if y < abs(y - k):
    print(y)
else:
    print(abs(y - k))


'''

while True:
    temp_y = y

    if temp_y % k == 0:
        y = 0
        break

    y = abs(y - k)
    if temp_y < y:
        y = temp_y
        break
    else:
        continue

print(y)
'''
