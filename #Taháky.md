# <h1 align="center"> **Táhaky** </h1>
# Tomáš Vrabec 1IT

## **PYTHON**
### **Úvod do pythonu**
- If, Elif, Else
## Příklad zde:
```python
a = 10
b = 5
if a > b:
    print("a je větší než b")
elif a < b:
    print("b je větší než a")
else:
    print("a je rovno b")
    
```
## **Práce s texte**m
- Strip, Lower, Split

## Strip
- Odstranění bílých znaků na začátku a konci textu
```python
text = "  Dobrý den!  "
text = text.strip()
print(text)  # "Dobrý den!"
```
## Lower
- Převede text na malá písmena:
```python
text = "AHOJ"
text = text.lower()
print(text)  # "ahoj"
```
## Split
- Rozdělení textu podle mezery:
```python
text = "Ahoj všichni"
seznam_slov = text.split()
print(seznam_slov)  # ["Ahoj", "všichni"]
```
# **Základní syntaxe**
```python
# Jednoduchý výpis do konzole
print("Hello, World!")

# Proměnné
x = 10
y = "Python"
z = 3.14
```
# **Datové typy**
```python
integer = 42           # Celé číslo
floating = 3.14        # Desetinné číslo
string = "Ahoj"        # Řetězec
list_example = [1, 2, 3] # Seznam
```
# **Operace**
```python
a = 10
b = 3

print(a + b)  # Sčítání
print(a - b)  # Odčítání
print(a * b)  # Násobení
print(a / b)  # Dělení
print(a // b) # Celé dělení
print(a % b)  # Zbytek po dělení
print(a ** b) # Umocnění
```
## **Porovnávací operace**
```python
print(a == b)  # Rovnost
print(a != b)  # Nerovnost
print(a > b)   # Větší než
print(a < b)   # Menší než
print(a >= b)  # Větší nebo rovno
print(a <= b)  # Menší nebo rovno
