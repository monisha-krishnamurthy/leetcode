class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = defaultdict(int)
        for ele in nums:
            freq_map[ele] += 1
        
        # pair_list = list()
        # for key,val in freq_map.items():
        #     pair_list.append((key,val))

        sorted_list = sorted(freq_map.items(), key=lambda x:x[1], reverse = True) 

        output = list()
        for i in range(k):
            output.append(sorted_list[i][0])
        return output
