# Given a non-empty array of integers nums, 
# every element appears twice except for one. Find that single one.

# Example 1:

# Input: nums = [2,2,1]
# Output: 1

# Simple Solution

def singleNumber(nums):
    freq = {}

    for num in nums:
        if num not in freq:
            freq[num] = 1
        else:
            freq[num] += 1

    for key,value in freq.items():
        if value == 1:
            return key

print(singleNumber([3,3,4,4,2]))


# XOR Solution

# The XOR operator returns 1 if the two bits being compared are different, and 0 if they are the same.
# if we XOR all the numbers in the array together, 
# the duplicates will cancel each other out and we will be left with the number that appears only once.

def singleNumber(nums):
    ans = 0
    for num in nums:
        ans ^= num
    return ans

print(singleNumber([3,3,4,4,2]))

# Set Solution

def singleNumber(nums):
    return 2 * sum(set(nums)) - sum(nums)

print(singleNumber([3,3,4,4,2]))