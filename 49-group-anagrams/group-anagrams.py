class Solution:
    #given a string, find a freq array of its characters
    def freqArray(self, s1: str):
        #initialise char array to an empty array of size 26
        chArray = [0]*26
        #iterate through the string
        for ch in s1:
            #convert the char to an index and increment the corresponding value at the index  
            chArray[ord(ch) - ord('a')] += 1
        return chArray

    #method to group strings that are anagrams of each other
    def groupAnagrams(self, arr: List[str]) -> List[List[str]]:
        #initialise a hashmap to store the char freq as key and the string as value
        mapping = defaultdict(list)
        #iterate over the strings in the input array
        for str in arr:
            #convert array to its freq list
            charMap = self.freqArray(str)
            #appending to the hashmap
            mapping[tuple(charMap)].append(str)

        output = list()
    #iterate over the values of hashmap to return the result
        for value in mapping.values():
            output.append(tuple(value))
        return output	

