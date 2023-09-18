"""
Median of Two Sorted Arrays
===========================

Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

Example 1:

 Input: nums1 = [1,3], nums2 = [2]
 Output: 2.00000
 Explanation: merged array = [1,2,3] and median is 2.

Example 2:

 Input: nums1 = [1,2], nums2 = [3,4]
 Output: 2.50000
 Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.

Constraints:

 nums1.length == m
 nums2.length == n
 0 <= m <= 1000
 0 <= n <= 1000
 1 <= m + n <= 2000
 -106 <= nums1[i], nums2[i] <= 106

"""

def findMedianSortedArrays(nums1, nums2):
    # Ensure nums1 is the smaller array
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1

    m, n = len(nums1), len(nums2)
    low, high = 0, m

    while low <= high:
        partition1 = (low + high) // 2
        partition2 = (m + n + 1) // 2 - partition1

        maxLeft1 = float('-inf') if partition1 == 0 else nums1[partition1 - 1]
        minRight1 = float('inf') if partition1 == m else nums1[partition1]
        
        maxLeft2 = float('-inf') if partition2 == 0 else nums2[partition2 - 1]
        minRight2 = float('inf') if partition2 == n else nums2[partition2]

        if maxLeft1 <= minRight2 and maxLeft2 <= minRight1:
            if (m + n) % 2 == 0:
                return (max(maxLeft1, maxLeft2) + min(minRight1, minRight2)) / 2.0
            else:
                return max(maxLeft1, maxLeft2)
        elif maxLeft1 > minRight2:
            high = partition1 - 1
        else:
            low = partition1 + 1

    raise ValueError("Input arrays are not sorted.")

# nums1 = [1,3]
# nums2 = [2]
nums1 = [1,2]
nums2 = [3,4]
outcome = findMedianSortedArrays(nums1, nums2)

print(outcome)



"""
The code provided above implements the mathematical algorithm known as the **"Median of Two Sorted Arrays"** algorithm. This algorithm is used to find the median of two sorted arrays efficiently. Here's a mathematical description of the algorithm:

**Input**:
- Two sorted arrays: `nums1` of length `m` and `nums2` of length `n`.

**Output**:
- The median of the combined array formed by merging `nums1` and `nums2`.

**Algorithm**:
1. Determine the smaller of the two input arrays (let's assume `nums1` is the smaller one). If not, swap them.

2. Initialize two pointers, `low` and `high`, for binary searching in the smaller array (`nums1`). Set `low` to 0 and `high` to the length of `nums1`.

3. Enter a binary search loop while `low` is less than or equal to `high`.

4. Inside the loop, calculate the partition points, `partition1` and `partition2`, for both arrays:
   - `partition1` is the midpoint of the smaller array (`nums1`) between `low` and `high`.
   - `partition2` is calculated such that the total number of elements on the left side (`maxLeft1` and `maxLeft2`) is equal to the total number of elements on the right side (`minRight1` and `minRight2`).

5. Find the maximum element on the left side (`maxLeft1` and `maxLeft2`) and the minimum element on the right side (`minRight1` and `minRight2`) for both arrays.

6. Check if the partitions are correct: `maxLeft1 <= minRight2` and `maxLeft2 <= minRight1`. If these conditions are met, you've found the correct partition.

7. If the total number of elements (m + n) is even, return the average of the maximum element on the left side and the minimum element on the right side. Otherwise, return the maximum element on the left side.

8. If the partitions are not correct, adjust the binary search:
   - If `maxLeft1` is greater than `minRight2`, move the `high` pointer to the left of `partition1` (reduce the search space).
   - Otherwise, move the `low` pointer to the right of `partition1` (increase the search space).

9. Repeat the binary search until you find the correct partition, or until the `low` pointer is greater than the `high` pointer.

10. If the binary search loop completes without finding the correct partition, raise an error.

This algorithm efficiently finds the median of two sorted arrays in O(log(min(m, n))) time complexity, which is the desired time complexity. It takes advantage of the fact that the median of the combined array is determined by the partitions of both input arrays, and it uses binary search to find these partitions.
"""

def mediasorted(nums1,nums2):
    me = nums1 + nums2
    l = len(me)
    total = sum(me)
    return total / l
outcome = mediasorted(nums1,nums2)

print(outcome)


"""
The code  provided calculates the median by merging both arrays and then computing the average. While this approach can give you the correct median, it's not as efficient as the binary search-based algorithm  explained earlier. The binary search-based algorithm has a time complexity of O(log(min(m, n))), while merging the arrays and calculating the average has a time complexity of O(m + n), which is less efficient, especially for large arrays.

However, if you have relatively small arrays or if you're not concerned about algorithmic efficiency, your code should produce the correct median. Here's the code with a minor improvement to avoid dividing by zero when l is 0:
"""
def mediasorted(nums1, nums2):
    me = nums1 + nums2
    l = len(me)
    
    if l == 0:
        return 0.0  # Handle the case where both input arrays are empty
    
    total = sum(me)
    return total / l
