def second_largest(nums):
    nums = list(set(nums))  # Remove duplicates
    nums.sort()
    if len(nums) < 2:
        return "No second largest element."
    return nums[-2]

# Example usage
lst = list(map(int, input("Enter list elements separated by space: ").split()))
print("Second largest:", second_largest(lst))
