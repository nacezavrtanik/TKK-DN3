from Crypto.PublicKey import DSA
import random

# Generira praštevili p in q:
pq = DSA.generate(1024)
p = pq.p
q = pq.q

# Generira zasebni ključ a:
a = random.randrange(q)

# Generira števili alpha in beta:
h = random.randrange(p)
alpha = 1
while alpha == 1:
    alpha = pow(h, int((p-1)/q), p)
beta = pow(alpha, a, p)

# Izpiše generirana ključa:
print('Zasebni ključ a:\n' + str(a))
print('\nJavni ključ (p, q, alpha, beta):')
print('{}\n{}\n{}\n{}'.format(p, q, alpha, beta))

# Generirana ključa shrani v datoteko 'dsa.txt':
zapisi = input('\nŽeliš generirana ključa shraniti v novo datoteko dsa.txt? (y/n): ')
if zapisi == 'y':
    dsa = open('dsa.txt', 'a')
    dsa.write('{}\n\n{}\n{}\n{}\n{}'.format(a, p, q, alpha, beta))
    dsa.close()
input('Zaključeno!')
