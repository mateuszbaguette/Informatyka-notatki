import random
N=20

def losuj(A):
    for i in range(N):
        A[i]=random.randint(0,49)
def wypisz(A):
    for i in range(N):
        print(A[i],end='')
    print()

def DNSPNM(A):
    maks_dl=1
    akt_dl=1
    for i in range(1,N):
        if A[i]>=A[i-1]:
            akt_dl+=1
            if(akt_dl>maks_dl):
                maks_dl=akt_dl
        else:
            akt_dl=1
    return maks_dl

random.seed()
A=[0]*N
losuj(A)
wypisz(A)
print("DNSPNM: ", DNSPNM(A))
