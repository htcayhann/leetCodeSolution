class Solution(object):
    def minimumIndex(self, nums):
        from collections import defaultdict

        freq = {num:0 for num in nums}
        for i in range(len(nums)):
            freq[nums[i]] += 1

        max_freq = max(freq.values())
        dominant = -1

        for num,count in freq.items():
            if count == max_freq:
                dominant = num
                break
        
        total_dom = max_freq
        left_dom = 0
        n = len(nums)

        for i in range(n):
            if nums[i] == dominant:
                left_dom += 1

            if(left_dom * 2 >(i+1) and (total_dom - left_dom)*2>(n-i-1)):
                return i

        return -1           
    
        