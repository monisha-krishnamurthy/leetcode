class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        output = dict()
        for i in arr:
            if i in output:
                output[i] +=1
            else:
                output[i] = 1
        print(output)
        result = set()
        for j in output:
            result.add(output[j])
        print(result)

        if len(result) == len(output):
            return True
        else:
            return False