
class NextGreaterElemtent:
    def nextGreaterElement(self, num1, num2):
        n = len(num2)
        lst = []
    
        for i in num1:
            k = num2.index(i)+1
            #print(k)
            found = 0
            for j in range(k, n):
                print(j)
                if num2[j] > i:
                    lst.append(num2[j])
                    found = 1
                    break
            if found == 0:
                lst.append(-1)
        return lst
        
n1 = [4,1,2]
n2 = [1,3,4,2]
l = []
lst = NextGreaterElemtent.nextGreaterElement(l,n1,n2)
print(lst)

