hap = 0
n,m = map(int,input().split())
arr = list(map(int,input().split()))
set_n = set(map(int,input().split()))
set_m = set(map(int,input().split()))
for i in arr:
    if i in set_n:
        hap+=1
    elif i in set_m:
        hap-=1
print(hap)
