from typing import List


def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    m_ = m - 1
    n_ = n - 1
    last_idx = m + n - 1
    while n_ >= 0:
        if m_ >= 0 and (nums1[m_] > nums2[n_]):
            nums1[last_idx] = nums1[m_]
            m_ -= 1
        else:
            nums1[last_idx] = nums2[n_]
            n_ -= 1
        last_idx -= 1


if __name__ == '__main__':
    # nums1 = [1,2,3,0,0,0]
    # m = 3
    # nums2 = [2,5,6]
    # n = 3

    # nums1 = [1]
    # m = 1
    # nums2 = []
    # n = 0

    # nums1 = [0]
    # m = 0
    # nums2 = [1]
    # n = 1

    nums1 = [4,0,0,0,0,0]
    m = 1
    nums2 = [1,2,3,5,6]
    n = 5

    merge(nums1, m, nums2, n)
    print(nums1)