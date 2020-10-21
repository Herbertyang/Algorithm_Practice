#https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/
#test line
class Solution:
    def smallerNumbersThanCurrent(self, nums: list[int]) -> list[int]:
        hash = {}
        for num, value in enumerate(sorted(nums)):
            if value not in hash:
                hash[value] = num
        return [hash[num] for num in nums]


if __name__ == "__main__":
    x = Solution
    res = x.smallerNumbersThanCurrent(x, [1,2,1,1,1,1])
    print(res)
