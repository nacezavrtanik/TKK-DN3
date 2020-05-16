import random
import hashlib


def podpisiDSA(besedilo, a, p, q, alpha, beta):
    k = random.randrange(q)
    print('Število k: ' + str(k))
    gamma = pow(alpha, k, p) % q
    print('Število gamma: ' + str(gamma))
    k_inv = pow(k, q-2, q)
    print(k, k_inv, k*k_inv %q)
    h = int(hashlib.sha1(besedilo.encode('utf-8')).hexdigest(), 16)
    delta = k_inv * (h + a * gamma) % q
    print('Število delta: ' + str(delta))

    if gamma * delta == 0:
        podpisiDSA(besedilo, a, p, q, alpha, beta)
    else:
        print(gamma, delta)
        
