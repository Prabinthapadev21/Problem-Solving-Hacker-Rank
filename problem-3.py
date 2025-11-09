# comparing the marks of two friends and counting which friend scored highest score.

a = [1,2,3]
b = [3,2,1]

def marksComparision(a,b):
    acount = 0
    bcount = 0
    for i,j in zip(a,b): #here zip method is used to compare values at the same time.
            if i>j:
                acount+=1
            else:
                bcount+=1
    return acount,bcount

result = marksComparision(a,b)
print(result)
        
