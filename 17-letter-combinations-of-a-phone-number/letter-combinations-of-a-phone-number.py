class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digits_map = {2:["a","b","c"], 3:["d","e","f"], 4:["g","h","i"], 5:["j","k","l"], 
                    6:["m","n","o"], 7:["p","q","r","s"], 8:["t","u","v"], 9:["w","x","y","z"]}

        if digits == "":
            return []
        def generate_combination(index, digits, output_list, output=""):
            if index == len(digits):  # Base case: When the required length is achieved
                print(output)
                output_list.append(output) 
                return
        
            digit = digits[index] 
            for char in digits_map[int(digit)]:
                generate_combination(index+1, digits, output_list, output + char)
            # generate_combination(1, digits, output_list, a)
            #     generate_combination(2, digits, output_list, ad)
            #     generate_combination(2, digits, output_list, ae)
            #     generate_combination(2, digits, output_list, af)
            # generate_combination(1, digits, output_list, b)
            # generate_combination(1, digits, output_list, c) 

        output_list = []
        generate_combination(0, digits, output_list, output="")
        return output_list 
