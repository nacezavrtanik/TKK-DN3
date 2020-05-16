from Crypto.PublicKey import DSA
from Crypto.Signature import DSS
import hashlib
import random


# Hash danega niza s funkcijo SHA-1, v hex:
def hes(niz):
    return hashlib.sha1(niz.encode('utf-8')).hexdigest()


# Generira besedi, ki za začneta z 'osnova', njuni hash
# vrednosti pa se v hex ujemata v prvih 'uj' znakih.
def kvazi_trk(osnova='', uj=11):

    hashi = set()
    beseda1 = ''
    beseda2 = ''

    # 1. KORAK:
    # Generira zaporedje besed in določi prvo besedo,
    # katere hash se ujema v želenem številu znakov
    # z le-tem neke prejšnje besede.
    stevec1 = 0
    while True:
        b1 = osnova + str(stevec1)
        celi1 = hes(b1)
        delni1 = celi1[0:uj]
        if delni1 in hashi:
            print(b1, delni1, celi1)
            beseda1 = b1
            break
        else:
            hashi.add(delni1)
        stevec1 += 1

    # 2. KORAK:
    # Poišče tisto prejšnjo besedo, s katero se ujema
    # beseda iz 1. koraka. Za to je vselej potrebnih
    # manj korakov kot v 1. koraku.
    stevec2 = 0
    while True:
        b2 = osnova + str(stevec2)
        celi2 = hes(b2)
        delni2 = celi2[0:uj]
        if delni2 == hes(beseda1)[0:uj]:
            print(b2, delni2, celi2)
            beseda2 = b2
            break
        else:
            stevec2 += 1

    # Natisne prvo vrstico, kot jo zahteva naloga:
    print('\n1. vrstica:')
    besedilo = beseda1 + ' ' + beseda2
    vrstica1 = besedilo + ' ' + str(int(hes(besedilo), 16))
    print(vrstica1)



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

    print('')
    print(vrstica1)
    print('27131106 {} {}'.format(gamma, delta))
    print('hash prejšnjega bloka')
    print('poljubni tekst')
    print('hash tega bloka')





















          
