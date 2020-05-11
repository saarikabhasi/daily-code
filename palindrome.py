#Given a string, find the length of the longest substring without repeating characters.
#Example:
#Input: "banana"
#Output: "anana"

#Input: "million"
#Output: "illi"
import re
class Solution:
    def longestPalidrome(self,s):
        if s==s[::-1]:return s
        sets =set(s)
        print(sets)
        m = 0
        n = len(s)
        l ={}
        for i in sets:
            
            start = s.find(i) 
            print(i,s,start) 
            end = (n-1)-s[::-1].find(i)
            print(i,s[::-1],end)
            if start !=end and m<end-start:
                m = end-start
                print(n,start-n,end-n+1)
                print(s[start:end+1], "rev",s[-end:-start])
                if n%2!=0:
                    if s[start:end+1] == s[start-n:end-n+1]: 
                        l[m]=(s[start:end+1])
                else:
                    if s[start:end+1] ==  s[-end:-start+1]:
                        l[m]= (s[start:end+1])

            
        print(l,max(l))
        return l[max(l)]
        
            
        



# s =1 e =4
#  n =7 s= -6 e = -3 
# even n = 6 : s = 1 e = 5
#s = -5 e = -1



if __name__ == '__main__':
    s = "banana"
    print(str(Solution().longestPalidrome(s)))

