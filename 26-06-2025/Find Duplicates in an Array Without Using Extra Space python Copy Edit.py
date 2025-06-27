def find_duplicates(nums):
    print("Duplicates are:")
    for i in range(len(nums)):
        index = abs(nums[i])
        if nums[index] >= 0:
            nums[index] = -nums[index]
        else:
            print(index, end=" ")

# Example usage
arr = list(map(int, input("Enter numbers (0 to n-1): ").split()))
find_duplicates(arr.copy())  # copy to avoid modifying original list
