# Computing the sum of elements of the array.

arr = [1,2,3,4,5]
length = len(arr)

def arraysum(arr,length):
    sum = 0
    for i in range(length):
        sum += arr[i]
    return sum

result = arraysum(arr,length)
print(f"Array elements sum is {result}")