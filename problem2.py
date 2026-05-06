def min_operations(arr, k):
    remainder = arr[0] % k

    for num in arr:
        if num % k != remainder:
            return -1

    arr.sort()
    median = arr[len(arr) // 2]

    operations = 0
    for num in arr:
        operations += abs(num - median) // k

    return operations


n = int(input())
arr = list(map(int, input().split()))
k = int(input())

print(min_operations(arr, k))
