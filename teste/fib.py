def fib(n):
    """
    Retorna o n-esimo numero de Fibonacci.
    """

    if n <= 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)
    
