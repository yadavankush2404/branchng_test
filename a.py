def first(arr,x,n):
    low =0
    high=n-1
    res=-1
    while(low<=high):
        mid = (low+high)//2
        if arr[mid]==x:
            res = mid
            high = mid-1
        elif arr[mid]<x:
            low = mid+1
        elif arr[mid] >x:
            high =mid -1;
    return res;

def sumi(arr):
    return sum(arr)

# Driver code
arr = [1, 2, 2, 2, 2, 3, 4, 7, 8, 8]
n = len(arr)
x = 2
 
print("First Occurrence =", first(arr, x, n))
print("Sum of n is : ", sumi(arr))
