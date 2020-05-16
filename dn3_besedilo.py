import hashlib


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


# 1. OPOMBA:
# Funkcijo 'kvazi_trk' sem najprej napisal brez parametra 'osnova',
# a je našla besedi, ki sta navedeni že v 2. bloku blockchaina.

# 2. OPOMBA:
# Funkcijo 'kvazi_trk' bi se dalo posplošiti tako, da bi zahtevali
# število bitov ujemanja namesto število ujemanja v hex. Za določeno
# število bitov ujemanja je trenutno treba vzeti ustrezno veliko število
# ujemanja v hex, kar pa potencialno naredi več, kot je zahtevano.
