M = int(input())
array = list(map(int, input().split()))
array.sort()
N = int(input())
answer = list(map(int, input().split()))

def binary_search(array, target, start, end):
    if start > end:
        return "no"
    mid = (start + end) // 2
    if array[mid] == target:
        return "yes"
    elif array[mid] > target:
        return binary_search(array, target, start, mid -1)
    else:
        return binary_search(array, target, mid+1, end)


for a in answer:
    p = binary_search(array, a, 0, M-1)
    print(p, end=" ")