class Solution:
    def lengthOfLIS(self, nums):
        size = len(nums)
        if size <= 1:
            return size
        
        dp = [1] * size
        for i in range(1, size):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)


