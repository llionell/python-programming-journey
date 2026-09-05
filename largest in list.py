def largest_in_list(nums):
    largest = nums[0]
    for n in nums:
        if n > largest:
            largest =n
    return largest
print(largest_in_list([24, 50, 12, 75, 30]))