# Computing the absolute difference of the two diagonal matrices.

arr = [
    [1,2,9],
    [4,5,6],
    [7,8,9]
]

def absolutedifference(arr):
    n = len(arr)
    sum1 = 0
    sum2 = 0
    for i in range (n):
        sum1 += arr[i][i]
        sum2 += arr[i][n-1-i]
    return abs(sum1-sum2)

result = absolutedifference(arr)
print(f"The absolute difference is {result}")
