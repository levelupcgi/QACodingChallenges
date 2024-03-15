# Find the second min/max number from an array. Write a method that accepts an int array as an argument
# and returns a second or n min/max number from the given array.

# Finding the second minimum or maximum number in an array can be approached in several ways, each with different computational complexities. Here are three methods to accomplish this, ranging from straightforward to more efficient in terms of time complexity.

# Method 1: Sorting
# The simplest approach is to sort the array and then pick the second smallest or second largest element directly.
# Time Complexity: O(n log n), where n is the number of elements in the array. This is due to the sorting operation, typically implemented with algorithms like quicksort or mergesort.


def find_second_min_max_sorting(nums):
    if len(nums) < 2:
        return None  # Handle arrays with fewer than 2 elements
    nums.sort()
    return nums[1], nums[-2]  # Second minimum and second maximum


# Method 2: Two Passes
# Perform two passes through the array: one to find the minimum/maximum and another to find the second minimum/maximum excluding the first minimum/maximum found.
# Time Complexity: O(n) for each of the four operations (min, max, filtered min, filtered max), so it's effectively O(n), but with a higher constant factor due to multiple passes.

def find_second_min_max_two_passes(nums):
    if len(nums) < 2:
        return None  # Handle arrays with fewer than 2 elements

    # Find min and max in the first pass
    min_val, max_val = min(nums), max(nums)

    # Filter out the min and max and find the new min and max in the second pass
    second_min = min(x for x in nums if x != min_val)
    second_max = max(x for x in nums if x != max_val)

    return second_min, second_max


# Method 3: One Pass
# Iterate through the array once, tracking the minimum and second minimum (or maximum and second maximum) as you go.
# Time Complexity: O(n), where n is the number of elements in the array. This is the most efficient in terms of time complexity, as it only requires a single pass through the array and no additional data structures.

def find_second_min_max_one_pass(nums):
    if len(nums) < 2:
        return None  # Handle arrays with fewer than 2 elements

    # Initialize the first and second min and max
    min_val = second_min = float('inf')
    max_val = second_max = float('-inf')

    for num in nums:
        # Update min and second min
        if num < min_val:
            second_min, min_val = min_val, num
        elif min_val < num < second_min:
            second_min = num

        # Update max and second max
        if num > max_val:
            second_max, max_val = max_val, num
        elif max_val > num > second_max:
            second_max = num

    return second_min, second_max

# Each method has its use cases depending on the situation, such as the size of the input data, the requirement for the data order, and whether additional memory usage is a concern.
