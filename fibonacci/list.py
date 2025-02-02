# Simple algorithm of Fibonacci sequence
#-----------------------------------------------
# Time: O(n)
# Space O(1)
#-----------------------------------------------
def fib_alg(n):
    if n < 2:
        return n

    first, next = 0, 1

    for i in range(n-1):
        first, next = next, first + next

    return next


print(fib_alg(7)) # -->> 13
print(fib_alg(20)) # -->> 6765
print(fib_alg(100)) # -->> 354224848179263111168





# -->>> The Binet formula, sums and representations of generalized Fibonacci-number
# URL - https://www.sciencedirect.com/science/article/pii/S0195669807000595
#-----------------------------------------------
# Time: O(1)
# Space O(1)
#-----------------------------------------------

def binet_fibonacci(n):
    sqrt5 = 5**0.5
    prev = (1 + sqrt5) / 2
    next = (1 - sqrt5) / 2

    return int((prev**n - next**n) / sqrt5)

print(binet_fibonacci(7)) # -->> 13
print(binet_fibonacci(20)) # -->> 6765
print(binet_fibonacci(100)) # -->> 354224848179263111168

# Recursive Fibonacci sequence
#-----------------------------------------------
"""
Time: O(2^n) --->> Time Complexity:The time complexity of this function is O(2^n). 
                    his is because each call to `fib_rec` results in two additional calls for `n-1` and `n-2`.
                    This leads to an exponential growth in the number of function calls as `n` increases.
                    Specifically, the number of calls grows like a binary tree, where each level
                    of the tree corresponds to a decrease in `n` by 1 or 2.
"""
# Space O(n)
#-----------------------------------------------

def fib_rec(n):
    if n < 2:
        return n
    return fib_alg(n-1) + fib_alg(n-2)

print(fib_rec(7)) # -->> 13
print(fib_rec(20)) # -->> 6765
print(fib_rec(100)) # -->> 354224848179263111168




def fib_with_big_numbers(x):
  if x < 2:
    return x
  else:
    return my_fib_helper(x)[0]

def my_fib_helper(x):
  if x == 1:
    return (1, 0)
  if x % 2 == 1:
    (p,q) = my_fib_helper(x-1)
    return (p+q,p)
  else:
    (p,q) = my_fib_helper(x/2)
    return (p*p+2*p*q,p*p+q*q)




# --> Problem: Need to find last digit in result n-fib sequence
def fib_digit(n):
        return an[n%60]

an = [0, 1, 1, 2, 3, 5, 8, 3, 1, 4, 5, 9, 4, 3, 7, 0, 7,
      7, 4, 1, 5, 6, 1, 7, 8, 5, 3, 8, 1, 9, 0, 9, 9, 8,
      7, 5, 2, 7, 9, 6, 5, 1, 6, 7, 3, 0, 3, 3, 6, 9, 5,
      4, 9, 3, 2, 5, 7, 2, 9, 1, 0]

 # else variant
a,b = 0,1
for _ in range(1,int(input())):
    a, b = b, (a+b)%10
print(b)












