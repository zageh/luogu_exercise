#ai写的，看懂不难，但我写不出来，太复杂了

MOD=10**9+7

S=1*16+2*240+3*3840+4*61440

base=(8*S*pow(65536,7,MOD)+7*pow(65536,8,MOD))%MOD

def best_save(mask):
    best=0
    i=0
    while i<8:
        if (mask>>i)&1:
            j=i
            while j+1<8 and ((mask>>(j+1))&1):
                j+=1
            k=j-i+1
            if k==8:
                save=13
            elif i==0 or j==7:
                save=2*k-2
            else:
                save=2*k-1
            if save>best:
                best=save
            i=j+1
        else:
            i+=1
    return best

sub=0
for mask in range(256):
    z=mask.bit_count()
    nz=8-z
    sub=(sub+best_save(mask)*pow(65535,nz,MOD))%MOD

ans=(base-sub)%MOD
print(ans)