from typing import List


# Leave this empty for your implementation
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i in range(len(nums) - 1):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left = i + 1
            right = len(nums) - 1

            while left < right:
                Sum = nums[left] + nums[right] + nums[i]
                if Sum > 0:
                    right -= 1
                elif Sum < 0:
                    left += 1
                else:
                    res.append([nums[left], nums[right], nums[i]])
                    left += 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
        return res
