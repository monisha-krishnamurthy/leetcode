# Generate the combinations of K distinct objects chosen from the N elements
# of a list: (10 Points)
# In how many ways can a committee of 3 be chosen from a group of 12 people? We all know that
# there are C(12,3) = 220 possibilities (C(N,K) denotes the well-known binomial coefficients). We
# need to generate all the possibilities (via backtracking).
# Write a combination predicate which takes the following form:
# combination(X, [x, y, z, ...], L).
# where X is the number of elements to be chosen from the list
# [x, y, z, ...] is the list of elements to be used
# L is the resultant list of distinct objects
# Sample Run:
# ?- combination(3,[a,b,c,d,e,f],L).
# L = [a,b,c] ;
# L = [a,b,d] ;
# L = [a,b,e] ;
# ….

def combination(X, A, L):
    if len(L) == X:
        print(L)
        return
    
    for i in range(len(A)):
        combination(X, A[i+1:], L+[A[i]])
    

if __name__ == "__main__":
    A = ['a', 'b', 'c', 'd', 'e', 'f']
    combination(4, A, [])
