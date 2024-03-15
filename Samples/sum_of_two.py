# Sum of two. Write a method that accepts an int[] array and an int number, and find 2 elements in the array that
# sum is equal to the given int. Assume that an input array will have only one pair of numbers that sum equal
# to our given number. It will always have this pair. See input and output examples. I use the Brute Force algorithm.

# Method 1: Brute Force
# The brute force method involves checking all possible pairs in the array to find the pair that sums up to the target number.
# Time Complexity: O(n^2), where n is the number of elements in the array. This is because it involves a nested loop to compare each element with every other element.

def find_pair_brute_force(nums, target):
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] + nums[j] == target:
                return nums[i], nums[j]


# Method 2: Sorting and Two-Pointers
# First, sort the array, then use two pointers to find the two numbers. One pointer starts at the beginning of the array, and the other starts at the end. Move the pointers towards each other based on the sum of their corresponding elements compared to the target sum.
# Time Complexity: O(n log n) due to the sorting step. The two-pointer approach itself is O(n), making this more efficient than the brute force approach for large arrays.
def find_pair_two_pointers(nums, target):
    nums.sort()
    left, right = 0, len(nums) - 1
    while left < right:
        current_sum = nums[left] + nums[right]
        if current_sum == target:
            return nums[left], nums[right]
        elif current_sum < target:
            left += 1
        else:
            right -= 1


# Method 3: Hash Table
# Use a hash table to store the elements of the array as you iterate. For each element, check if the complement (target - element) exists in the hash table.
# Time Complexity: O(n), where n is the number of elements in the array. This is the most efficient method in terms of time complexity among the three, as it only requires a single pass through the array.

def find_pair_hash_table(nums, target):
    complements = {}
    for num in nums:
        complement = target - num
        if complement in complements:
            return complement, num
        complements[num] = True

# Each of these methods has its advantages and trade-offs. The brute force method is simple but slow for large arrays. The sorting and two-pointers approach is faster but modifies the array, which might not be desirable in all cases. The hash table method offers the best time complexity without altering the array but requires additional space for the hash table.
