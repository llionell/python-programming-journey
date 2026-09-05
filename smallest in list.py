def smallest_in_list(nums):
    smallest = nums[0]
    for n in nums:
        if n < smallest:
            smallest = n
    return smallest
print(smallest_in_list([24, 50, 12, 5, 100]))
    