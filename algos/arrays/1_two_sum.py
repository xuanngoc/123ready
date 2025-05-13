from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # for i in range(len(nums)):
        #     for k in range(i+1, len(nums)):
        #         if nums[i] + nums[k] == target:
        #             return [i, k]

        remaining = {}
        for i, num in enumerate(nums):
            if remaining.get(num, None) is not None:
                return [remaining[num], i]
            else:
                remaining[target - num] = i 
                    

if __name__ == '__main__':
    print(Solution().twoSum([2, 7, 11, 15], 9))
