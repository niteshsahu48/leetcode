class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        blank_list=[]
        for i in range(1,n+1):
            if i%3==0 and i%5==0:
                blank_list.append("FizzBuzz")
            elif i%5==0:
                blank_list.append("Buzz")
            elif i%3==0:
                blank_list.append("Fizz")
            else:
                blank_list.append(str(i))
        return blank_list
        