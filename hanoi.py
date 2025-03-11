# 2. Tower of Hanoi: (10 Points)
# Program the Tower of Hanoi puzzle. You must use a, b, c as your peg names. Your output should
# be a bunch of ‘move’ statements like ‘move a to b’ (which means moving the top disk from peg a
# to peg b). You can use Prolog's ‘write’ predicate to output a string or a variable to the screen. The
# ‘nl’ predicate outputs a newline to screen.
# Note: The goal predicate will take the form:
# hanoi(X, a, c, b).
# where X is a variable (the number of discs)

def hanoi(X, peg1, peg2, peg3):
    if X == 0:
        return 
    
    hanoi(X-1, peg1, peg3, peg2)
    print(f"move {peg1} to {peg3}")
    hanoi(X-1, peg2, peg1, peg3)

if __name__ == "__main__":
    hanoi(3, "a", "b", "c")
