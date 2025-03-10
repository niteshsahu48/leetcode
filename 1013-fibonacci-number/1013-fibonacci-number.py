class Solution:
    def fib(self, n: int) -> int:
        """if n <= 0:
            return 0
        elif n == 1:
            return 1

        a = 0
        b = 1
        c = 0
        for _ in range(2, n + 1):
            a = c
            c = b
            b = a + b  

        return b"""

        if n <= 1:
            return n
        return self.fib(n-1)+self.fib(n-2)

        
        

        