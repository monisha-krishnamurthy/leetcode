class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * (n+1)

        dp[0] = 0
        dp[1] = nums[0]

        #dp at every index will store an intermediary value upto that index, 
        #may or maynot be inclusive 
        #[1 100 20] dp = [1 100 100]

        for i in range(2, n+1):
            dp[i] = max(dp[i-1], dp[i-2]+nums[i-1]) 
        return dp[-1] 