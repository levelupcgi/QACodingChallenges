# Max/min number from an array. Write a method that will accept an array of int as an argument and
# it returns the max/min number from a given array.

# Method 1: Using Built-in Functions
# The simplest way is to use Python's built-in max() and min() functions.
# This approach is very straightforward and efficient for most cases, but it technically iterates through the list twice.
# Time Complexity: O(n) for each function, but since they're called separately, the array is traversed twice.
def find_max_min(nums):
    return max(nums), min(nums)


# Method 2: Manual Iteration
# You can manually iterate through the list once, comparing each element to the current max and min values you've found.
# Time Complexity: O(n), where n is the number of elements in the array.
# This method only requires a single pass through the array, making it more efficient in terms of the number of
# iterations than using separate max() and min() calls.
def find_max_min_manual(nums):
    if not nums:
        return None, None  # Handle empty array
    max_num = min_num = nums[0]
    for num in nums[1:]:
        if num > max_num:
            max_num = num
        elif num < min_num:
            min_num = num
    return max_num, min_num

# Method 3: Sorting
# Another option is to sort the array first, then pick the first and last elements as the min and max, respectively.
# Time Complexity: O(n log n), where n is the number of elements in the array.
# This is due to the sorting operation, which typically involves algorithms like quicksort or mergesort behind the scenes.
#

def find_max_min_sorting(nums):
    nums.sort()
    return nums[-1], nums[0] if nums else (None, None)


# Method 4: Divide and Conquer
# A more complex method involves using a divide and conquer strategy to find the max and min.
# This involves recursively dividing the array into halves, finding the max and min in each half, and then combining the results.
# Time Complexity: O(n), similar to the manual iteration method, but with added overhead due to recursive calls.
# This method is theoretically more efficient for very large datasets due to its divide and conquer approach but
# may not outperform the manual iteration in practice due to recursion overhead.
def max_min_divide_conquer(nums, start, end):
    if start == end:  # Only one element
        return nums[start], nums[start]
    elif end == start + 1:  # Two elements
        return (max(nums[start], nums[end]), min(nums[start], nums[end]))
    else:
        mid = (start + end) // 2
        max1, min1 = max_min_divide_conquer(nums, start, mid)
        max2, min2 = max_min_divide_conquer(nums, mid+1, end)
        return max(max1, max2), min(min1, min2)

def find_max_min_divide_conquer(nums):
    if not nums:
        return None, None
    return max_min_divide_conquer(nums, 0, len(nums)-1)


# Each of these methods has its use cases depending on the situation, such as the size of the data, the need for speed, and whether memory efficiency is a concern.

