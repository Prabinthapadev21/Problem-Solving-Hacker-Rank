# Computing the sum of the positive,negatiive and zero numbers and computing their ratios.
arr = [1,-1,0,3,-2,0,9]

def sumAndration(arr):
    add = 0
    sub = 0
    zero =0
    n = len(arr)
    for i in arr:
        if i>0:
            add+=1
        elif i<0:
            sub+=1
        else:
            zero+=1
    addration = add/n
    subratio = sub/n
    zeroration = zero/n
    print(f"Positive ratio = {addration:.6f}")
    print(f"Negative ratio = {subratio:.6f}")
    print(f"Zero ratio = {zeroration:.6f}")

sumAndration(arr)