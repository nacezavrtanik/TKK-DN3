import hashlib
import random


# Izračuna hash (SHA-1) niza, v hex:
def hes(niz):
    return hashlib.sha1(niz.encode('utf-8')).hexdigest()


# Podpise besedilo z DSA (SHA-1):
def podpisiDSA(tekst, a, p, q, alpha, beta):
    gamma = 0
    delta = 0
    while gamma * delta == 0:
        k = random.randrange(q)
        gamma = pow(alpha, k, p) % q
        k_inv = pow(k, q-2, q)
        h = int(hes(tekst), 16)
        delta = k_inv * (h + a * gamma) % q
    return(gamma, delta)
    

# Generira naslednji blok blockchaina:
def blockchain():

    print('Računam...')

# Priprava besedila:
    hashi = set()
    beseda1 = ''
    beseda2 = ''
    seed = random.randrange(1000)

    # Prva beseda:
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
        
    # Druga beseda:
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
            
    # Besedilo:
    besedilo = beseda1 + ' ' + beseda2

# Prebere ključa za DSA iz datoteke 'dsa.txt':
    dsa = open('dsa.txt', 'r')
    A = int(dsa.readline())
    dsa.readline()
    P = int(dsa.readline())
    Q = int(dsa.readline())
    Alpha = int(dsa.readline())
    Beta = int(dsa.readline())
    dsa.close()

# Podpiše besedilo:
    (Gamma, Delta) = podpisiDSA(besedilo, A, P, Q, Alpha, Beta)

# Vrstice 1, 2, 3:
    vrstica1 = besedilo + ' ' + str(int(hes(besedilo), 16))
    vrstica2 = '27131106 {} {}'.format(Gamma, Delta)
    vrstica3 = input('Vnesi 5. vrstico prejšnjega bloka: ')

    print('Računam...')

# Vrstici 4, 5:
    vrstica4 = '"This is how, one sunrise, we cut down them canoes."'
    blok = '{}\n{}\n{}\n{}'.format(vrstica1, vrstica2, vrstica3, vrstica4)
    vrstica5 = hes(blok)
    stevec3 = 0
    while vrstica5[0:7] != '0000000':
        vrstica4 = stevec3
        blok = '{}\n{}\n{}\n{}'.format(vrstica1, vrstica2, vrstica3, vrstica4)
        vrstica5 = hes(blok)
        stevec3 += 1
        
# Izpiše blok:
    print('\nBlok:')
    print('{}\n{}\n{}\n{}\n{}'.format(vrstica1, vrstica2, vrstica3, vrstica4, vrstica5))

# Izpisan blok shrani v datoteko z izbranim imenom:
    zapisi = input('\nShrani v datoteko? (y/n): ')
    if zapisi == 'y':
        dn3 = open(input('Vnesi ime datoteke: ') + '.txt', 'x')
        dn3.write('{}\n{}\n{}\n{}\n{}'.format(vrstica1, vrstica2, vrstica3, vrstica4, vrstica5))
        dn3.close

    input('Zaključeno!')


blockchain()
