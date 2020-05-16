from Crypto.PublicKey import DSA
import hashlib
import random


def hes(niz):
    return hashlib.sha1(niz.encode('utf-8')).hexdigest()


def dn3():

    hashi = set()
    beseda1 = ''
    beseda2 = ''
    seed = random.choice(range(100))

    stevec1 = 0
    while True:
        b1 = str(seed + stevec1) + str(stevec1)
        celi1 = hes(b1)
        delni1 = celi1[0:11]
        if delni1 in hashi:
            beseda1 = b1
            break
        else:
            hashi.add(delni1)
        stevec1 += 1

    stevec2 = 0
    while True:
        b2 = str(seed + stevec2) + str(stevec2)
        celi2 = hes(b2)
        delni2 = celi2[0:11]
        if delni2 == hes(beseda1)[0:11]:
            beseda2 = b2
            break
        else:
            stevec2 += 1

    besedilo = beseda1 + ' ' + beseda2


    pq = DSA.generate(1024)
    p = pq.p
    q = pq.q
    
    a = random.randrange(q)

    h = random.randrange(p)
    alpha = 1
    while alpha == 1:
        alpha = pow(h, int((p-1)/q), p)
    beta = pow(alpha, a, p)

    print('Zasebni ključ a:\n' + str(a))
    print('\nJavni ključ (p, q, alpha, beta):')
    print('{}\n{}\n{}\n{}'.format(p, q, alpha, beta))


    gamma = 0
    delta = 0
    while gamma * delta == 0:
        k = random.randrange(q)
        gamma = pow(alpha, k, p) % q
        k_inv = pow(k, q-2, q)
        h = int(hes(besedilo), 16)
        delta = k_inv * (h + a * gamma) % q
    
    vrstica1 = besedilo + ' ' + str(int(hes(besedilo), 16))
    vrstica2 = '27131106 {} {}'.format(gamma, delta)
    vrstica3 = input('\nVnesi hash prejšnjega bloka: ')
    
    vrstica4 = '"This is how, one sunrise, we cut down them canoes."'
    blok = '{}\n{}\n{}\n{}'.format(vrstica1, vrstica2, vrstica3, vrstica4)
    vrstica5 = hes(blok)
    stevec3 = 0
    while vrstica5[0:7] != '0000000':
        vrstica4 = int(hes(str(stevec3)), 16)
        blok = '{}\n{}\n{}\n{}'.format(vrstica1, vrstica2, vrstica3, vrstica4)
        vrstica5 = hes(blok)
        stevec3 += 1

    print('\nBlok:')
    print('{}\n{}\n{}\n{}\n{}'.format(vrstica1, vrstica2, vrstica3, vrstica4, vrstica5))

    zapisi = input('\nShrani v datoteko? (y/n): ')
    if zapisi == 'y':
        dn3 = open(input('Vnesi ime datoteke: ') + '.txt', 'x')
        dn3.write('Zasebni ključ a:\n' + str(a))
        dn3.write('\n\nJavni ključ (p, q, alpha, beta):\n')
        dn3.write('{}\n{}\n{}\n{}'.format(p, q, alpha, beta))
        dn3.write('\n\nBlok:\n')
        dn3.write('{}\n{}\n{}\n{}\n{}'.format(vrstica1, vrstica2, vrstica3, vrstica4, vrstica5))
        dn3.close

    print('Zaključeno!')






          
