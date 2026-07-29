def largest(nums):
    largest=nums[0]
    for num in nums:
        if num>largest:
            largest=num
            return largest
numbers = [10, 5, 25, 8, 15]
result = largest(numbers)
print(result)