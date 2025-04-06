class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = defaultdict(int)
        for ele in nums:
            freq_map[ele] += 1

        # to append key,value of hashmap into a tuple
        # for k, v in my_dict.items():   //use .items() to unpack k,v pairs in a hashmap
        #     tuple_list.append((k, v))

        # sorting a dictionary based on its values whose output will be a tuple
        sorted_list = sorted(freq_map.items(), key=lambda x:x[1], reverse = True) 
        # print(sorted_list) ---- [(1, 3), (2, 2), (3, 1)] for input [1,1,1,2,2,3]

        output = list() 
        for i in range(k):
            output.append(sorted_list[i][0])
        return output
