size=input().split()
M=int(size[0])
N=int(size[1])
midlimit=int(M/2)
string=".|."
def center_welcome(M,N):
    
    print("WELCOME".center(N,"-"))
def upper_print(midlimit,N):
    for i in range(midlimit):
        
        print((string*(2*i+1)).center(N,"-"))
def lower_print(midlimit,M, N):
    c=midlimit-1
    for i in range(M,midlimit+1,-1):
        print((string*(2*c+1)).center(N,"-"))
        c=c-1
upper_print(midlimit,N)
center_welcome(M,N)
lower_print(midlimit,M,N)
