class Solution:
    def compress(self, chars: List[str]) -> int:
        if len(chars)==1:
            return 1

        length = len(chars)
        index = 1
        iteration = 0
        char = chars[0]
        count = 1
        while (iteration < length-1):
            iteration += 1
            if chars[index] == char:
                count+=1
                if index+1 < len(chars) and chars[index+1] == char:
                    chars.pop(index)
                else:
                    arr = list(str(count))
                    chars[index] = arr[0]
                    if len(arr)>1:
                        for i in arr[1:]:
                            chars.insert(index+1, i)
                            index+=1                  
                    count=1
                    if index+2<len(chars):
                        char = chars[index+1]
                        index+=2
            else:
                if index+1<len(chars):
                    char = chars[index]
                    index+=1
            
        return len(chars)