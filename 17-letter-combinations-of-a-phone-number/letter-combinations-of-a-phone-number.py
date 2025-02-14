class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digits_map = {2:["a","b","c"], 3:["d","e","f"], 4:["g","h","i"], 5:["j","k","l"], 
                    6:["m","n","o"], 7:["p","q","r","s"], 8:["t","u","v"], 9:["w","x","y","z"]}

        if digits == "":
            return []
        def generate_binary(n, digits, output_list, output=""):
            if n == len(digits):  # Base case: When the required length is achieved
                print(output)
                output_list.append(output) 
                return

            # Include '0' and recurse
            digit = digits[n] 
            for s in digits_map[int(digit)]:
                generate_binary(n+1, digits, output_list, output + s)

        output_list = []
        generate_binary(0, digits, output_list, output="")
        return output_list 
