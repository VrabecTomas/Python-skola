text = "ahoj jak se mas"
posun = 3

# Šifrování
sifra = ""
for znak in text:
    if znak.isalpha():
        sifra += chr((ord(znak) - ord('a') + posun) % 26 + ord('a'))
    else:
        sifra += znak

print("Zašifrovaný text:", sifra)

# Dešifrování
desifra = ""
for znak in sifra:
    if znak.isalpha():
        desifra += chr((ord(znak) - ord('a') - posun) % 26 + ord('a'))
    else:
        desifra += znak

print("Dešifrovaný text:", desifra)
