text="Dzień dobry, zapraszam serdecznie na zebranie wychowawcy z rodzicami. "

c = text[6:11]
print(c)

odwrocony = c[::-1]
print(odwrocony)

dl = len(text)
print(dl)

polowa_tekstu = dl // 2

do_polowy = text[0:polowa_tekstu]
od_polowy = text[polowa_tekstu:-1]
print(do_polowy)
print(od_polowy)

tab = text.split(' ')
print(tab)

tab1 = ' '.join(tab)
print(tab1)

lw = text.lower()
up = text.upper()
print(lw)
print(up)

print("dobry" in text)
print("z" in text)

print(text.find("dobry"))
print(text.find("z"))
print(text.index("dobry"))
print(text.index("z"))
print(text.count("z"))

text2 = "     "+text+"     "
print(text2)
print(text2.strip())

print(text.isdigit())
print(text.isalpha())
print(text.isalnum()) #cyfry i liczby
