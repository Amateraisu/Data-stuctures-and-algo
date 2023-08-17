

n, q = input().split()
res = []
array = input().split()
array = [int(x) for x in array]
print(array)
for i in range(q):
    query = input().split()
    query = [int(x) for x in query]
    if query[0] == 1:
        # increase a, b
    elif query[1] == 2:
        # set each value to x
    else:
        # calculate the sum in range(a, b)