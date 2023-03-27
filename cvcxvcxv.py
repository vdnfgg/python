def nwd(a, b):
    if b == 0:
        return a
    return nwd(b, a % b)

class Ulamek():
    def __init__(self, licz, mian):
        self.licz = licz
        self.mian = mian

    def skracaj(self):
        NWD = nwd(self.licz, self.mian)
        self.licz //= NWD
        self.mian //= NWD
        return self

    def dodawanie(self, u):
        if self.mian == u.mian:
            mianownik = self.mian
        else:
            mianownik = self.mian * u.mian
        self.licz *= u.mian
        u.licz *= self.mian
        licznik = self.licz + u.licz
        self.licz = licznik
        self.mian = mianownik
        self.skracaj()

    def odejmowanie(self, u):
        if self.mian == u.mian:
            mianownik = self.mian
        else:
            mianownik = self.mian * u.mian
        self.licz *= u.mian
        u.licz *= self.mian
        licznik = self.licz - u.licz
        self.licz = licznik
        self.mian = mianownik
        self.skracaj()

    def mnozenie(self, u):
        self.licz *= u.licz
        self.mian *= u.mian
        self.skracaj()

    def dzielenie(self, u):
        self.licz *= u.mian
        self.mian *= u.licz
        self.skracaj()


#dodawanie
u = Ulamek(6, 12)
u2 = Ulamek(3, 8)

u.dodawanie(u2)
print(f"Suma: {u.licz}/{u.mian}")


#odejmowanie
u = Ulamek(6, 12)
u2 = Ulamek(3, 8)

u.odejmowanie(u2)
print(f"Różnica: {u.licz}/{u.mian}")


#mnozenie
u = Ulamek(6, 12)
u2 = Ulamek(3, 8)

u.mnozenie(u2)
print(f"Iloczyn: {u.licz}/{u.mian}")


#dzielenie
u = Ulamek(6, 12)
u2 = Ulamek(3, 4)

u.dzielenie(u2)
print(f"Iloraz: {u.licz}/{u.mian}")
