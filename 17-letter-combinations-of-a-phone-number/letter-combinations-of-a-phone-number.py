class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digits_map = {2:["a","b","c"], 3:["d","e","f"], 4:["g","h","i"], 5:["j","k","l"], 
                    6:["m","n","o"], 7:["p","q","r","s"], 8:["t","u","v"], 9:["w","x","y","z"]}
        output_list = []
        self.recursive(list(digits), digits_map, "", output_list)
        return output_list

    def recursive(self, digits, digits_map, output, output_list):
        if len(digits) == 0:
            if output:
                output_list.append(output) 
            return 

        digit = int(digits[0])
        for alphabet in digits_map[digit]:
            self.recursive(digits[1:], digits_map, output + alphabet, output_list)