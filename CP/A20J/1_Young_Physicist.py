su=0
arr=list()
n=int(input())
for _ in range(n):
    ar = list(map(int,input().split()))
    arr.append(ar)
x,y,z=0,0,0
for i in range(n):
    x+=arr[i][0]
    y += arr[i][1]
    z += arr[i][2]
if x==0 and y==0 and z==0:
    print("YES")
else:
    print("NO")