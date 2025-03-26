class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        output_list = []
        self.recursive(n, 0, "", output_list)
        return output_list

    def recursive(self, no_of_pairs, brackets_to_be_closed, output, output_list):
        if no_of_pairs == 0 and brackets_to_be_closed == 0:
            output_list.append(output)
            return 

        if brackets_to_be_closed != 0:
            self.recursive(no_of_pairs, brackets_to_be_closed - 1, output + ")", output_list)
        if no_of_pairs != 0:
            self.recursive(no_of_pairs-1, brackets_to_be_closed + 1, output + "(", output_list)
        # if no_of_pairs != 0 and brackets_to_be_closed != 0:
        #     self.recursive(no_of_pairs - 1, brackets_to_be_closed + 1, output + "(", output_list)
        #     self.recursive(no_of_pairs, brackets_to_be_closed - 1, output + ")", output_list) 

