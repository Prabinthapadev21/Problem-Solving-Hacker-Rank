# big array sum.

arr = [100001,1000001,100001,110100,101101]

def bigarraySum(arr):
    sum = 0
    for i in arr:
        sum +=i
    return sum
    
result = bigarraySum(arr)
print(f"Big array sum is {result}")