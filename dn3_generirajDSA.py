from Crypto.PublicKey import DSA
from Crypto.Signature import DSS
import hashlib
import random

def generirajDSA():
    # Generira praštevili p in q:
    pq = DSA.generate(1024)
    p = pq.p
    q = pq.q
    
    # Generira zasebni ključ a:
    a = random.randrange(q)

    # Generira alpha in beta:
    h = random.randrange(p)
    alpha = 1
    while alpha == 1:
        alpha = pow(h, int((p-1)/q), p)
    beta = pow(alpha, a, p)

    # Natisne javni ključ (p, q, alpha, beta) in zasebni ključ a:
    print('Zasebni ključ a:\n' + str(a))
    print('\nJavni ključ (p, q, alpha, beta):')
    print('{}\n{}\n{}\n{}'.format(p, q, alpha, beta))
