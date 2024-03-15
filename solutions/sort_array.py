# Sort array without built-in sort methods. In this example, we will use selection sort and bubble sort algorithms to sort our array.
#
# In selection sort, we select the smallest and swap it with the current array and we will keep doing it for each element.
# Please watch this video for a visual explanation.
# https://www.youtube.com/watch?v=3hH8kTHFw2A&ab_channel=CS50

# In bubble sort, we bubble out the biggest values to the right side by looping over our array and switching
# two pairs of elements if they are not in the correct order. Please watch this video for a visual explanation.
# https://www.youtube.com/watch?v=RT-hUXUWQ2I&ab_channel=CS50


def selection_sort(nums):
    # Iterate through the entire array
    for i in range(len(nums)):
        # Assume the current position is the minimum
        min_index = i
        # Check the rest of the array to find if there's a smaller number
        for j in range(i + 1, len(nums)):
            if nums[j] < nums[min_index]:
                min_index = j
        # Swap the found minimum element with the first element
        nums[i], nums[min_index] = nums[min_index], nums[i]
    return nums


def bubble_sort(nums):
    n = len(nums)
    # Traverse through all elements in the array
    for i in range(n):
        # Last i elements are already in place
        for j in range(0, n - i - 1):
            # Traverse the array from 0 to n-i-1
            # Swap if the element found is greater than the next element
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
    return nums


# Example array
nums = [64, 34, 25, 12, 22, 11, 90]

# Sorting with Selection Sort
sorted_nums_selection = selection_sort(nums.copy())
# Sorting with Bubble Sort
sorted_nums_bubble = bubble_sort(nums.copy())

# sorted_nums_selection, sorted_nums_bubble
# Both the Selection Sort and Bubble Sort algorithms have successfully sorted the example array. Here are the sorted arrays:

# Sorted with Selection Sort: [11, 12, 22, 25, 34, 64, 90]
# Sorted with Bubble Sort: [11, 12, 22, 25, 34, 64, 90]
# Both methods result in the same sorted array, demonstrating their effectiveness in sorting the numbers in ascending order.
