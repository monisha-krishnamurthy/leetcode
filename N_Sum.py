def NSum(arr, target):
    backtracking(arr, target, [])

def backtracking(arr, target, temp=[]):   
    # while writing recursive functions, 
    # step 1: identify arguments and purpose  
    # step 2: identify base condition -- to obtain result and terminate the loop
    if target == 0:
        print(temp)
        return
    
    # if target never becomes 0, then it becomes negative and len(arr) == 0
    if len(arr) == 0:
        return

    # backtracking considering that particular element & w/o considering it 
    # can't use temp.append() because append function will return None at every stage
    backtracking(arr[1:], target-arr[0], temp + [arr[0]])
    backtracking(arr[1:], target, temp)

if __name__ == "__main__":
    arr = [-2,-1,-3]
    target = -6 
    NSum(arr, target)

