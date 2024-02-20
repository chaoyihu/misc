from datetime import datetime

def fib_lazy(n):
    if n == 0 or n == 1:
        return n
    return fib_lazy(n - 1) + fib_lazy(n - 2)

memo = {0: 0, 1: 1}
def fib_memo(n):
    if n in memo:
        return memo[n]
    res = fib_memo(n - 1) + fib_memo(n - 2)
    memo[n] = res
    return res

def fib_memo_2(n):
    if n == 0 or n == 1:
        return n
    km1, km2 = 1, 0
    for k in range(2, n + 1):
        res = km1 + km2
        km1, km2 = res, km1
    return res


def matmul_2x2(a, b):
    return [
            [a[0][0] * b[0][0] + a[0][1] * b[1][0],
             a[0][0] * b[0][1] + a[0][1] * b[1][1]],
            [a[1][0] * b[0][0] + a[1][1] * b[1][0],
             a[1][0] * b[0][1] + a[1][1] * b[1][1]]
            ]
 
def fib_fast(n):
    if n == 0:
        return 0

    m = [[1, 1], 
         [1, 0]]
    i = [[1, 0], 
         [0, 1]]
    def matexp(k):
        if k == 0:
            return i
        k, mod = divmod(k, 2)
        r = matexp(k)
        return matmul_2x2(matmul_2x2(r, r), m if mod == 1 else i)
    
    return matexp(n - 1)[0][0]

tests = [2, 20, 200, 2000, 10000]

for n in tests:

    ts = datetime.now()
    print("n = {}, fibonacci - memo_2".format(n))
    res = fib_memo_2(n)
    te = datetime.now()
    print("Time: ", te - ts)
    
    ts = datetime.now()
    print("n = {}, fibonacci - fast".format(n))
    te = datetime.now()
    print("check results:", fib_fast(n) == res)
    print("Time: ", te - ts)
