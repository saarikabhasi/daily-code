# arr = [1,2,3] --> [1 ,2 ,4] 
arr = [1,2,9]
n = int(''.join([str(i) for i in arr])) 
res = [i for i in str(n+1)]
print(res)
