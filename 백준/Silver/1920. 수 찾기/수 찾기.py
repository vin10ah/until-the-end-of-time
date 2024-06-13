N = int(input())
nums = list(map(int,input().split()))
M = int(input())
tasks = list(map(int,input().split()))

nums.sort()

def bisearch(arr, target):
    start = 0
    end = len(arr)-1

    while start <= end:
        mid = (start+end) // 2
        if arr[mid]==target:
            return mid
        elif arr[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    
    return -1

for task in tasks:
    if bisearch(nums, task)==-1:
        print(0)
    else:
        print(1)