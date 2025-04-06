class Solution:
    # USING FREQ-MAP AND BUBBLE SORT (FREQ ARRAY)
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = defaultdict(int)
        count_arr = [[] for i in range(len(nums) + 1)]
        
        for num in nums:
            freq_map[num] += 1 

        for key,val in freq_map.items():
            count_arr[val].append(key)

        output = list()
        for i in range(len(count_arr)-1, 0, -1):
            for ele in count_arr[i]:
                output.append(ele)
                if len(output) == k:
                    return output