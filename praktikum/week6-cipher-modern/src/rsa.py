# rsa_superlight.py — super ringan (EDUKASI, TIDAK AMAN)
import secrets, math

def egcd(a,b):
    if b==0: return a,1,0
    g,x1,y1=egcd(b,a%b); return g,y1,x1-(a//b)*y1
def modinv(a,m):
    g,x,_=egcd(a,m)
    if g!=1: raise ValueError('no inverse')
    return x % m

def is_probable_prime(n,k=2):
    if n<2: return False
    small=[2,3,5,7,11,13,17,19,23]
    for p in small:
        if n%p==0: return n==p
    d,s=n-1,0
    while d%2==0: d//=2; s+=1
    for _ in range(k):
        a=secrets.randbelow(n-3)+2
        x=pow(a,d,n)
        if x==1 or x==n-1: continue
        for _ in range(s-1):
            x=pow(x,2,n)
            if x==n-1: break
        else:
            return False
    return True

def gen_prime(bits):
    assert bits>=8
    while True:
        p=secrets.randbits(bits)|(1<<(bits-1))|1
        if is_probable_prime(p): return p

def generate_rsa(bits=64):
    h=bits//2
    p=gen_prime(h); q=gen_prime(bits-h)
    while q==p: q=gen_prime(bits-h)
    n=p*q; phi=(p-1)*(q-1); e=65537
    if math.gcd(e,phi)!=1: return generate_rsa(bits)
    return (e,n),(modinv(e,phi),n)

b2i=lambda b:int.from_bytes(b,'big')
i2b=lambda i,l: i.to_bytes(l,'big')
def max_bytes_for_modulus(n): return (n.bit_length()-1)//8

def rsa_encrypt_long(msg,pub):
    e,n=pub; b=msg.encode(); L=max_bytes_for_modulus(n)
    if L<=0: raise ValueError('modulus too small')
    out=[]
    for i in range(0,len(b),L):
        blk=b[i:i+L]; m=b2i(blk); out.append((pow(m,e,n), len(blk)))
    return out

def rsa_decrypt_long(blocks,priv):
    d,n=priv; parts=[]
    for c,l in blocks:
        m=pow(c,d,n); parts.append(i2b(m,l))
    return b''.join(parts).decode('utf-8',errors='ignore')

if __name__=='__main__':
    # gunakan bits kecil agar ringan; ganti ke 128/256 jika CPU kamu kuat
    pub,priv=generate_rsa(bits=64)
    print('n bitlen:', pub[1].bit_length())
    msg=input('Masukkan pesan : ')
    cblocks=rsa_encrypt_long(msg,pub)
    print('Cipher (hex,len):', [(hex(c)[2:],l) for c,l in cblocks])
    print('Dekripsi:', rsa_decrypt_long(cblocks,priv))