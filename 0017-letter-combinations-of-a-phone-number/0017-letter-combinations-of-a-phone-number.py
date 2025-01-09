class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        def two_arr(arr1,arr2):
            temp=[]
            for item_1 in arr1:
                for item_2 in arr2:
                    arr=(item_1+item_2)
                    temp.append(arr)
            return temp
                    
        store={'2':['a','b','c'],
            '3':['d','e','f'],
            '4':['g','h','i'],
            '5':['j','k','l'],
            '6':['m','n','o'],
            '7':['p','q','r','s'],
            '8':['t','u','v'],
            '9':['w','x','y','z'],
        }
        
        result=[]
        if digits=="":
            return result

        elif len(digits)==1:
            return store[digits[0]]

        elif len(digits)==2:
            arr1=store[digits[0]]
            #print(arr1)
            arr2=store[digits[1]]
            #print(arr2)
            return two_arr(arr1,arr2)

        elif len(digits)==3:
            arr1=store[digits[0]]
            arr2=store[digits[1]]
            arr3=store[digits[2]]
            list1=two_arr(arr1,arr2)
            return two_arr(list1,arr3)
        
        elif len(digits)==4:
            arr1=store[digits[0]]
            arr2=store[digits[1]]
            arr3=store[digits[2]]
            arr4=store[digits[3]]

            list1=two_arr(arr1,arr2)
            list2=two_arr(arr3,arr4)
            return two_arr(list1,list2)

        


        




        









       
     
        