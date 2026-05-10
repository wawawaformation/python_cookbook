# Mémo Python — méthodes courantes

Mémo pratique pour coder avec les types courants : `int`, `float`, `str`, `list`, `dict`.

---
<details>
<summary>
int
</summary>
Les entiers ont peu de méthodes utilisées au quotidien. On utilise surtout les opérateurs.

### `int(value)`

```python
int("42")
```

**Retour :** `int`

**Fait :** convertit une valeur en entier si possible.

```python
int("42")  # 42
```

---

### `n.bit_length()`

```python
n = 8
n.bit_length()
```

**Retour :** `int`

**Fait :** retourne le nombre de bits nécessaires pour représenter l’entier.

```python
(8).bit_length()  # 4 car 8 = 1000 en binaire
```

Usage plutôt rare.
</details>

---
<details>
<summary>
float
</summary>
### `float(value)`

```python
float("3.14")
```

**Retour :** `float`

**Fait :** convertit une valeur en nombre décimal si possible.

```python
float("3.14")  # 3.14
```

---

### `round(number, digits)`

```python
round(3.14159, 2)
```

**Retour :** `int` ou `float`

**Fait :** arrondit un nombre.

```python
round(3.14159, 2)  # 3.14
round(3.6)         # 4
```

---

### `x.is_integer()`

```python
x = 3.0
x.is_integer()
```

**Retour :** `bool`

**Fait :** indique si le float représente un entier.

```python
(3.0).is_integer()  # True
(3.5).is_integer()  # False
```
</details>

---
<details>

<summary>
Les string
</summary>
### `s.strip()`

```python
s.strip()
```

**Retour :** `str`

**Fait :** retire les espaces au début et à la fin.

```python
"  hello  ".strip()  # "hello"
```

---

### `s.lower()`

```python
s.lower()
```

**Retour :** `str`

**Fait :** met la chaîne en minuscules.

```python
"Hello".lower()  # "hello"
```

---

### `s.upper()`

```python
s.upper()
```

**Retour :** `str`

**Fait :** met la chaîne en majuscules.

```python
"Hello".upper()  # "HELLO"
```

---

### `s.split()`

```python
s.split()
```

**Retour :** `list[str]`

**Fait :** découpe une chaîne en liste.

```python
"hello world".split()  # ["hello", "world"]
```

Avec séparateur :

```python
"a,b,c".split(",")  # ["a", "b", "c"]
```

---

### `separator.join(items)`

```python
" ".join(items)
```

**Retour :** `str`

**Fait :** assemble une liste de chaînes en une seule chaîne.

```python
" ".join(["hello", "world"])  # "hello world"
```

Attention : les éléments doivent être des strings.

---

### `s.replace(old, new)`

```python
s.replace("old", "new")
```

**Retour :** `str`

**Fait :** remplace du texte.

```python
"hello world".replace("world", "Python")  # "hello Python"
```

---

### `s.startswith(prefix)`

```python
s.startswith("abc")
```

**Retour :** `bool`

**Fait :** vérifie si la chaîne commence par une valeur.

```python
"main.py".startswith("main")  # True
```

---

### `s.endswith(suffix)`

```python
s.endswith(".csv")
```

**Retour :** `bool`

**Fait :** vérifie si la chaîne se termine par une valeur.

```python
"data.csv".endswith(".csv")  # True
```

---

### `s.find(value)`

```python
s.find("x")
```

**Retour :** `int`

**Fait :** retourne la position de la première occurrence. Retourne `-1` si absent.

```python
"hello".find("e")  # 1
"hello".find("z")  # -1
```

---

### `s.count(value)`

```python
s.count("a")
```

**Retour :** `int`

**Fait :** compte le nombre d’occurrences.

```python
"banana".count("a")  # 3
```

---

### `s.isdigit()`

```python
s.isdigit()
```

**Retour :** `bool`

**Fait :** vérifie si la chaîne contient uniquement des chiffres.

```python
"123".isdigit()  # True
"12a".isdigit()  # False
```

---

### `s.isalpha()`

```python
s.isalpha()
```

**Retour :** `bool`

**Fait :** vérifie si la chaîne contient uniquement des lettres.

```python
"abc".isalpha()   # True
"abc123".isalpha() # False
```

---

### `s.capitalize()`

```python
s.capitalize()
```

**Retour :** `str`

**Fait :** met la première lettre en majuscule et le reste en minuscules.

```python
"hello".capitalize()  # "Hello"
```
</details>

---
<details>
<summary>
Les listes
</summary>

### `lst.append(x)`

```python
lst.append(x)
**Retour :** `None`

**Fait :** ajoute un élément à la fin de la liste.

```python
lst = [1, 2]
lst.append(3)
# lst = [1, 2, 3]
```

---

### `lst.extend(items)`

```python
lst.extend(items)
```

**Retour :** `None`

**Fait :** ajoute plusieurs éléments à la fin de la liste.

```python
lst = [1, 2]
lst.extend([3, 4])
# lst = [1, 2, 3, 4]
```

---

### `lst.pop()`

```python
lst.pop()
```

**Retour :** l’élément retiré

**Fait :** retire et retourne le dernier élément.

```python
lst = [1, 2, 3]
x = lst.pop()
# x = 3
# lst = [1, 2]
```

Avec index :

```python
lst.pop(0)  # retire le premier élément
```

---

### `lst.remove(x)`

```python
lst.remove(x)
```

**Retour :** `None`

**Fait :** retire la première occurrence de `x`.

```python
lst = [1, 2, 2, 3]
lst.remove(2)
# lst = [1, 2, 3]
```

Erreur si la valeur n’existe pas.

---

### `lst.sort()`

```python
lst.sort()
```

**Retour :** `None`

**Fait :** trie la liste sur place.

```python
lst = [3, 1, 2]
lst.sort()
# lst = [1, 2, 3]
```

Avec ordre inverse :

```python
lst.sort(reverse=True)
```

---

### `sorted(lst)`

```python
sorted(lst)
```

**Retour :** nouvelle `list`

**Fait :** retourne une nouvelle liste triée sans modifier l’originale.

```python
lst = [3, 1, 2]
new_lst = sorted(lst)
# new_lst = [1, 2, 3]
# lst = [3, 1, 2]
```

---

### `lst.reverse()`

```python
lst.reverse()
```

**Retour :** `None`

**Fait :** inverse la liste sur place.

```python
lst = [1, 2, 3]
lst.reverse()
# lst = [3, 2, 1]
```

---

### `lst.index(x)`

```python
lst.index(x)
```

**Retour :** `int`

**Fait :** retourne l’index de la première occurrence de `x`.

```python
lst = ["a", "b", "c"]
lst.index("b")  # 1
```

Erreur si la valeur n’existe pas.

---

### `lst.count(x)`

```python
lst.count(x)
```

**Retour :** `int`

**Fait :** compte combien de fois `x` apparaît.

```python
[1, 2, 2, 3].count(2)  # 2
```

---

### `lst.clear()`

```python
lst.clear()
```

**Retour :** `None`

**Fait :** vide la liste.

```python
lst = [1, 2, 3]
lst.clear()
# lst = []
```

---

### `list1 + list2`

```python
list3 = list1 + list2
```

**Retour :** nouvelle `list`

**Fait :** concatène deux listes sans modifier les originales.

```python
[1, 2] + [3, 4]  # [1, 2, 3, 4]
```
</details>

---


<details>
<summary>
Les dictionnaires
</summary>

### `d.keys()`

```python
d.keys()
```

**Retour :** `dict_keys`

**Fait :** retourne une vue des clés.

```python
{"a": 1, "b": 2}.keys()
# dict_keys(['a', 'b'])
```

---

### `d.values()`

```python
d.values()
```

**Retour :** `dict_values`

**Fait :** retourne une vue des valeurs.

```python
{"a": 1, "b": 2}.values()
# dict_values([1, 2])
```

---

### `d.items()`

```python
d.items()
```

**Retour :** `dict_items`

**Fait :** retourne une vue des couples `(clé, valeur)`.

```python
{"a": 1, "b": 2}.items()
# dict_items([('a', 1), ('b', 2)])
```

Très utile avec unpacking :

```python
for key, value in d.items():
    print(key, value)
```

---

### `d.get(key, default)`

```python
d.get("age", None)
```

**Retour :** la valeur, ou `default` si la clé n’existe pas

**Fait :** lit une valeur sans lever `KeyError` si la clé est absente.

```python
row = {"email": "a@test.com"}
row.get("age", None)  # None
```

---

### `d.pop(key)`

```python
d.pop("a")
```

**Retour :** la valeur supprimée

**Fait :** retire une clé et retourne sa valeur.

```python
d = {"a": 1, "b": 2}
x = d.pop("a")
# x = 1
# d = {"b": 2}
```

Avec valeur par défaut :

```python
d.pop("missing", None)
```

---

### `d.update(other_dict)`

```python
d.update({"c": 3})
```

**Retour :** `None`

**Fait :** ajoute ou remplace des clés.

```python
d = {"a": 1}
d.update({"b": 2})
# d = {"a": 1, "b": 2}
```

Si la clé existe déjà :

```python
d.update({"a": 99})
# d["a"] vaut maintenant 99
```

---

### `d.setdefault(key, default)`

```python
d.setdefault("count", 0)
```

**Retour :** la valeur de la clé

**Fait :** crée la clé avec une valeur par défaut si elle n’existe pas.

```python
d = {}
d.setdefault("count", 0)
# d = {"count": 0}
```

Si la clé existe déjà, elle n’est pas remplacée.

---

### `d.clear()`

```python
d.clear()
```

**Retour :** `None`

**Fait :** vide le dictionnaire.

```python
d = {"a": 1}
d.clear()
# d = {}
```
</details>

---

<details>
<summary>
Les sets
</summary>

## Les set
```python
s = {1, 2, 3}
```
👉 Un set, c’est :

- pas de doublons
- pas d’ordre garanti

### Méthodes importantes
```python
s.add(x)        # ajoute un élément
s.remove(x)     # supprime (erreur si absent)
s.discard(x)    # supprime (pas d'erreur si absent)
s.pop()         # enlève un élément au hasard
s.clear()       # vide le set
```

### Opérations puissantes

```python
a = {1, 2, 3}
b = {3, 4, 5}
a | b   # union -> {1, 2, 3, 4, 5}
a & b   # intersection -> {3}
a - b   # difference -> {1, 2}
```

</details>

---

<details>
<summary>
Opérations très courantes
</summary>

### `len(value)`

```python
len(value)
```

**Retour :** `int`

**Fait :** donne la taille.

```python
len("abc")        # 3
len([1, 2, 3])    # 3
len({"a": 1})     # 1
```

---

### `x in value`

```python
x in value
```

**Retour :** `bool`

**Fait :** teste la présence.

```python
"a" in "cat"       # True
2 in [1, 2, 3]     # True
"email" in row     # teste la présence de la clé dans un dict
```

---

### `type(value)`

```python
type(value)
```

**Retour :** un type Python

**Fait :** indique le type d’une valeur.

```python
type("hello")  # <class 'str'>
type([1, 2])   # <class 'list'>
```

---

### `isinstance(value, type)`

```python
isinstance(value, str)
```

**Retour :** `bool`

**Fait :** vérifie si une valeur est d’un certain type.

```python
isinstance("hello", str)  # True
isinstance(42, int)       # True
```

---

## À retenir

Méthodes qui modifient souvent sur place et retournent `None` :

```python
list.append()
list.extend()
list.sort()
list.reverse()
list.clear()
dict.update()
dict.clear()
```

Fonctions/méthodes qui retournent une nouvelle valeur :

```python
str.strip()
str.lower()
str.split()
" ".join(...)
sorted(...)
dict.get(...)
```

Attention :

```python
dict.pop(...)
```

retourne une valeur, mais modifie aussi le dictionnaire sur place.
</details>