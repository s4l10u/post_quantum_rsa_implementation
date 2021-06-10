import  numpy as np
import gmpy2 
from gmpy2 import mpz
B=64
PBYTES=B/8
K=64

primes=[]


def random_prime():
    while 1:
       p=mpz(int('0x'+np.random.bytes(PBYTES).encode('hex'),16)).bit_set(int(0))
       if gmpy2.t_mod(p,3)==2:
         if gmpy2.is_prime(p)== true:
            return p



def complet_bit(p,nbt_bit):
    c=p.digits(2)
    if len(c)< nbt_bit :
        while len(c)<nbt_bit:
            c='0'+c
    return c


def public_and_secrete_keys(liste):
    mult=[]
    i=1
    prod=karatsuba()
    #9 etapte pour calcule le produit sous forme d'arbre inverse de 512 nombre primier 
    # En effet on a 512=2^9

    while i <= 9:
        j=0
        while j < len(liste):
            mult.append(prod.multiply(liste[j],liste[j+1]))
            j+=2
        liste=mult
        mult=[]
        #print(p)
        i+=1
    
    pk=mpz(liste[0])
    # sk de taille 3k(B/8) byte
    sk="".join([complet_bit(i,B) for i in primes ])

    sk+="".join([complet_bit(gmpy2.invert(gmpy2.c_div(N,i),i),B) for i in primes])

    sk+=complet_bit(N,K*B)

    mpz(int(sk,base=2))
    return [pk,sk]

for x in range(0,K):
    p=random_prime()
    if (mpz(p) in primes) == False:
        primes.append(p)
