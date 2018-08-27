# medianoftwoarrays.py

# There are two sorted arrays nums1 and nums2 of size m and n respectively.

# Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

# Example 1:
# nums1 = [1, 3]
# nums2 = [2]

# The median is 2.0
# Example 2:
# nums1 = [1, 2]
# nums2 = [3, 4]

# The median is (2 + 3)/2 = 2.5
import time

def solution(nums1, nums2):
    res = nums1 + nums2
    res.sort()
    if len(res) % 2 == 0:
        return (res[int(len(res)//2)] + res[len(res)//2 - 1])/2
    else:
        return float(res[len(res)//2])


def main():
    nums1 = [1, 2, 5, 6]
    nums2 = [3, 4]
    print(solution(nums1, nums2))

    nums1 = [1, 2]
    nums2 = [1,2,3]
    print(solution(nums1, nums2))

    nums1 = [1]
    nums2 = [1]
    print(solution(nums1, nums2))

    nums1 = [1, 1]
    nums2 = [1, 1]
    print(solution(nums1, nums2))


    nums1 = [1, 2]
    nums2 = [3, 4]
    print(solution(nums1, nums2))

    nums1 = [4]
    nums2 = [1, 2, 3]
    print(solution(nums1, nums2))

    nums1 = [1, 2]
    nums2 = [-1, 3]
    print(solution(nums1, nums2))


st = time.time()
main()
print("\n{} second\n".format(time.time() - st))