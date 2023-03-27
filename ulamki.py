l1 = 5
m1 = 7

l2 = 3
m2 = 6

def nwd(a, b):
    if b == 0:
        return a
    return nwd(b, a % b)

NWD = nwd(l2, m2)

def dodawanie(l1, m1, l2, m2):
    wm = m1 * m2
    l1 *= m2
    l2 *= m1
    licznik = l1 + l2
    mianownik = wm
    NWD = nwd(licznik, mianownik)
    print(f"Suma ulamkow: {licznik // NWD}/{mianownik // NWD}")

#dodawanie(l1, m1, l2, m2)

class ulamek():
    pass

u1 = ulamek()
u1.licz = 5
u1.mian = 7

u2 = ulamek()
u2.licz = 3
u2.mian = 6

def nwd_ob(u):
    if u.mian == 0:
        return u.licz
    return nwd_ob(u.mian, u.licz % u.mian)

def skracaj_ob(u):
    NWD = nwd(u.licz, u.mian)
    u.licz //= NWD
    u.mian //= NWD
    return u

# skrocony = skracaj_ob(u2)
# print(skrocony.licz)
# print(skrocony.mian)

def dodawanie_ob(u1, u2):
    u = ulamek()
    if u1.mian == u2.mian:
        wm = u1.mian
    else:
        wm = u1.mian * u2.mian
    u1.licz *= u2.mian
    u2.licz *= u1.mian
    u.licz = u1.licz + u2.licz
    u.mian = wm
    u = skracaj_ob(u)
    print(f"Suma ulamkow: {u.licz}/{u.mian}")

dodawanie_ob(u1, u2)

def odejmowanie_ob(u1, u2):
    u = ulamek()
    if u1.mian == u2.mian:
        wm = u1.mian
    else:
        wm = u1.mian * u2.mian
    u1.licz *= u2.mian
    u2.licz *= u1.mian
    u.licz = u1.licz - u2.licz
    u.mian = wm
    u = skracaj_ob(u)
    print(f"Różnica ulamkow: {u.licz}/{u.mian}")

u1 = ulamek()
u1.licz = 5
u1.mian = 7

u2 = ulamek()
u2.licz = 3
u2.mian = 6

odejmowanie_ob(u1, u2)

def mnozenie_ob(u1, u2):
    u = ulamek()
    u.licz = u1.licz * u2.licz
    u.mian = u1.mian * u2.mian
    u = skracaj_ob(u)
    print(f"Iloczyn ulamkow: {u.licz}/{u.mian}")

u1 = ulamek()
u1.licz = 5
u1.mian = 7

u2 = ulamek()
u2.licz = 3
u2.mian = 6

mnozenie_ob(u1, u2)

def dzielenie_ob(u1, u2):
    u = ulamek()
    u.licz = u1.licz * u2.mian
    u.mian = u1.mian * u2.licz
    u = skracaj_ob(u)
    print(f"Iloraz ulamkow: {u.licz}/{u.mian}")

u1 = ulamek()
u1.licz = 5
u1.mian = 7

u2 = ulamek()
u2.licz = 3
u2.mian = 6

dzielenie_ob(u1, u2)
