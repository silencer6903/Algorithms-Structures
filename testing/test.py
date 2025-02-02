import time
from matplotlib import pyplot as plt



def timed(f, n, n_iter=10):

    inf = float('inf')
    for i in range(n_iter):
        t0 = time.perf_counter()
        f(n)
        t1 = time.perf_counter()
        inf = min(inf, t1 - t0)
    return inf


def decor_fib(f):
    d = {}
    def wrapper(*args, **kwargs):
        n = args[0]
        if n not in d:
            d[n] = f(n)
        return d[n]

    return wrapper

h = {}
def rec_fib(n):
    if n < 2:
        return n
    if n not in h: h[n] = rec_fib(n-1) + rec_fib(n-2)
    return h[n]


def fib(k):
    p, n = 0, 1
    for i in range(k-1):
        p, n = n, n+p
    return n

def graf(funks, args):
    for f in funks:
        plt.plot(args, [timed(f, arg) for arg in args], label=f.__name__)
    plt.legend()
    plt.grid(True)
    plt.show()


graf([fib, rec_fib], list(range(7)))
