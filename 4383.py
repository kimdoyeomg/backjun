n, k = map(int, input().split())
arr=[i for i in range(1,n+1)]
ans=[]
num=k-1

for i in range(n):
    if len(arr)>num:
        ans.append(arr.pop(num))
        num +=k-1
    elif len(arr)<=num:
        num=num%len(arr)
        ans.append(arr.pop(num))
        num +=k-1
print("<", ', '.join(str(i) for i in ans), ">", sep="")