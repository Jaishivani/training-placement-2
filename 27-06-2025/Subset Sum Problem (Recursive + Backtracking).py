def is_subset_sum(arr, n, target):
    if target == 0:
        return True
    if n == 0:
        return False
    if arr[n-1] > target:
        return is_subset_sum(arr, n-1, target)
    return is_subset_sum(arr, n-1, target) or is_subset_sum(arr, n-1, target-arr[n-1])

arr = list(map(int, input("Enter array: ").split()))
target = int(input("Enter target sum: "))
print("Subset with sum exists?" , is_subset_sum(arr, len(arr), target))
