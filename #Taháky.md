# <h1 align="center"> **Táhaky** </h1>
# Tomáš Vrabec 1IT
## **PYTHON - úvod**
### Tento tahák obsahuje všechno potřebné v Pythonu.
# **Proměnné**
 - Slouží k ukládání dat do paměti
 - **Základ** pythonu
```python
# Definování proměnných
x = 10        # Celé číslo (int)
y = 3.14      # Desetinné číslo (float)
z = "Ahoj"    # Řetězec (string)
is_active = True  # Boolean (True/False)
```
# **Aritmetické operace**
* Běžné matematické operace, které můžeme provádět s čísly
* **Dělení** `/` vždy vrací desetinné číslo, zatímco `//` provádí celé dělení
* Operátor `%` nám dává **zbytek po dělení**
```python
a = 10
b = 3

print(a + b)  # Sčítání (13)
print(a - b)  # Odčítání (7)
print(a * b)  # Násobení (30)
print(a / b)  # Dělení (3.3333)
print(a // b) # Celé dělení (3)
print(a % b)  # Zbytek po dělení (1)
print(a ** b) # Umocnění (1000)
```
# **Podmínky a Logické operace** 
* **Podmínky** slouží k **rozhodování**, pokud je podmínka splněna
* **If-elif-else** nám umožňuje řídit průběh programu na základě různých hodnot proměnné
```python
x = 10

if x > 5:
    print("x je větší než 5")
elif x == 5:
    print("x je přesně 5")
else:
    print("x je menší než 5")
```
* Python používá **odsazení** místo složených závorek `{}`
# **Logické operátory**
* `and` – Pravda, pokud **obě podmínky** jsou pravdivé
* `or` – Pravda, pokud **alespoň jedna** podmínka je pravdivá
* `not` – Opačná hodnota výrazu
```python
a = True
b = False

print(a and b)  # AND (False)
print(a or b)   # OR (True)
print(not a)    # NOT (False)
```
# **Cykly** **(Loops)**
* Umožňuje opakování kódu, dokud je splněna podmínka
## **For Cyklus**
* Používá se převážně u seznamů a řetězců
```python
for i in range(5):  # range(5) = [0, 1, 2, 3, 4]
    print(i)
```
## **While Cyklus**
* Používá se, když **nevíme přesný počet opakování** a potřebujeme běžet podle podmínky
```python
x = 0
while x < 5:
    print(x)
    x += 1
```
## Řízení průběhu cyklu
 ```python
 for i in range(10):
    if i == 5:
        break  # Ukončí cyklus
    if i == 3:
        continue  # Přeskočí aktuální iteraci
    print(i)
```
* `break` – okamžitě ukončí smyčku
* `continue` – přeskočí aktuální iteraci a pokračuje další
# **Funkce**
* Funkce umožňují rozdělit program na menší části a **znovu
používat kód**
```python
def greet(name):
    return f"Ahoj, {name}!"

print(greet("Tom"))  # Ahoj, Tom!
```
# **Textové řetězce (Strings)**
* Práce s textem která je velmi používaná
```python
text = "  Hello World!  "

print(text.strip())  # Odstranění mezer
print(text.lower())  # Malá písmena
print(text.upper())  # Velká písmena
print(text.split())  # Rozdělení podle mezer
```
* Stringy **nelze měnit přímo**, ale můžeme vytvořit novou upravenou kopii
* `strip()` odstraní **nežádoucí mezery** na začátku a konci textu
# **Vstupy**
* Vstupy umožňují zadávat data během běhu programu
```python
name = input("Zadej své jméno: ")
print(f"Ahoj, {name}!")
```
# **Výstupy**
* K **výpisu** textu slouží funkce `print()`
```python
name = "Tom"
age = 15
print("Jmenuji se", name, "a je mi", age, "let.")
```
# <h3 align="center"> **Toto jsou všechny moje taháky** </h3>
