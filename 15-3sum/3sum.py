class Solution:
    def threeSum(self, array: List[int]) -> List[List[int]]:
        #sort the given array
        array.sort()
        print(array)
        #build a mapping of values to count
        mapping = defaultdict(int)
        for val in array:
            mapping[val] += 1
        #initialise the result array
        result = []

        #scan through array for the first number
        for i in range(len(array) - 2):
            #make sure the number is not the same as the previous
            if i > 0 and array[i] == array[i-1]:
                continue
            #decrement count of array[i] in mapping
            mapping[array[i]] -= 1

            #looking for the second number
            for j in range(i+1, len(array) -1):
                #make sure the number is not the same as the previous
                if j > i+1 and array[j] == array[j-1]:
                    continue
                #decrement count of array[j] in mapping
                mapping[array[j]] -= 1
                #find the complement in set 
                complement = 0 - array[i] - array[j]
                #complement should not be less than array[i] and array[j]
                if complement < array[i] or complement < array[j]:
                    mapping[array[j]] += 1
                    continue
                if mapping[complement] > 0:
                    #found 1 answer set
                    #add to the list
                    result.append([array[i], array[j], complement])
                mapping[array[j]] += 1 
                #return result after finding all combinations
        return result




