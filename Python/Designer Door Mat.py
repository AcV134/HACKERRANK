# Enter your code here. Read input from STDIN. Print output to STDOUT
def creator(l,b):
    hy = '-'
    mid = '.|.'
    for i in range(l//2):
        print((mid*(i*2+1)).center(b,hy))
    print('WELCOME'.center(b,hy))
    for i in range(l//2-1,-1,-1):
        print((mid*(i*2+1)).center(b,hy))
        
    
l,b = map(int,input().split())
creator(l,b)
