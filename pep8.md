---
theme: gaia
_class: lead
paginate: true
backgroundColor: #fff
---

![bg left:40% 80%](https://mypy.readthedocs.io/en/stable/_static/mypy_light.svg)
#### Clean code & code style ~ Jan Havlík `xhavlik@mendelu.cz`

---
# **Co nás čeká**

- PEP 8 - základy psaní kódu v Pythonu 
- Tooling:
    - `isort`
    - `black`
    - `pylint`
    - `mypy`
    - `flake8`
- Pomocník - AI?

---
# **PEP 8**

- `P`ython `E`nhancement `P`roposals
- základní pravidla psaní kódu
- předpoklad - kód se více čte, než píše ~ hlavní je **čitelnost**
- konzistence pomáhá s čitelností kódu (kdy se nemusí vyplatit být konzistentní - držet se za každou cenu PEP8?)

---
# **Zen of Python (PEP 20)**

```
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
```

---
# **PEP 8 - Struktura kódu**

### Odsazení

- 4 mezery

    ```
    # Zarovnání s oddělovačem (závorkou)
    foo = long_function_name(var_one, var_two,
                            var_three, var_four)

    # Přidání 4 dalších mezer (extra úroveň zanoření) pro oddělení od kódu
    def long_function_name(
            var_one, var_two, var_three,
            var_four):
        print(var_one)
    ```

---
# **PEP 8 - Struktura kódu**

- `if` podmínka

    ```
    # Bez indentace
    if (this_is_one_thing and
        that_is_another_thing):
        do_something()

    # S komentářem - podpoří rozdělení kódu a podmínky
    if (this_is_one_thing and
        that_is_another_thing):
        # Since both conditions are true, we can frobnicate.
        do_something()
    ```

---
# **PEP 8 - Struktura kódu**

### Odsazení

- inicializace dat

    ```
    my_list = [
        1, 2, 3,
        4, 5, 6,
    ]
    result = some_function_that_takes_arguments(
        'a', 'b', 'c',
        'd', 'e', 'f',
    )
    ```

---
# **PEP 8 - Struktura kódu**

### Taby nebo mezery?
- vždy mezery, taby pouze v případě, že už to tak někdo *špatně* napsal
    - nelze mixovat mezi sebou

### Délka řádku
- 79 znaků (pro komentáře 72)

---

# **PEP 8 - Struktura kódu**

### Importy

- v následujícím pořadí:
    1. Standardní knihovny
    2. Knihovny třetích stran (`pypi`)
    3. Lokální moduly

- samostatně, na každém řádku
    ```
    import os
    import sys
    ```
    takto **ne**:
    ```
    import os, sys
    ```

---

# **PEP 8 - Struktura kódu**

### Importy

-  nepoužívat wildcart import (všeho)
    ```
    from os import *
    ```
    možná kolize atd.

- lépe abosultní, než relativní cesty
    ```
    from tensorflow import keras
    from tensorflow.keras import layers
    ```
---

# **PEP 8 - Struktura kódu**

### Whitespaces

-  pozor na extra znaky
   ```
   # Spravne
   spam(ham[1], {eggs: 2})

   # Spatne
   spam( ham[ 1 ], { eggs: 2 } )
   ```

---

# **PEP 8 - Struktura kódu**

### Whitespaces

- mezera ihned za čárkou, dvojtečkou, středníkem
  ```
  if x == 4: print(x, y); x, y = y, x
  ```


-  indexace, funkce
   ```
   # Spravne
   dct['key'] = lst[index]

   # Spatne
   dct ['key'] = lst [index]
   ```

---

# **PEP 8 - Struktura kódu**

### Whitespaces

- trailing comma (tuple s jedním prvkem)
    ```
    # Spravne:
    foo = (0,)

    # Spatne:
    bar = (0, )
    ```
- pozor na **trailing whitespace**, soubor končit **novým řádkem**

---

# **PEP 8 - Struktura kódu**

### Whitespaces


- nezarovnávat hodnoty proměnných
  ```
  # Spravne
  x = 1
  y = 2
  long_variable = 3

  # Spatne
  x             = 1
  y             = 2
  long_variable = 3
  ```

---


# **PEP 8 - Struktura kódu**

### Komentáře

- **Neaktuální komentáře jsou horší než žádné komentáře**
- Každý komentář - celá věta
- **vždy** anglicky

#### In-line komentáře
- `print(x)  # FIXME: remove debug print`
- not too obvious
- 2 mezery za kódem, 1 za mříží

---

# **PEP 8 - Naming conventions**

- pozor na klíčová slova (`sum`, ...), zaměnitelná písmena v názvu funkcí (O, I, ...)

#### Názvy metod, funkcí, proměnných
- vystihující snake case 

#### Názvy modulů
- krátké, vše lowercase

---

# **PEP 8 - Naming conventions**

#### Názvy tříd
- CapWords (metody ale *snake case*)

#### Názvy výjmek (Exceptions)
- CapWords, ale končící suffixem `Error`

#### Globání proměnné
- pls don't

---


# **PEP 257 - Docstring**

- komentáře na úrovni modulu, funkcí, tříd, metod, ...
- možnost generování dokumentace (`sphinx`)
- vyžadováno některými tooly (`pylint`)

- jednořádkové docstringy (trojité uvozovky vždy - jednoduše rozšiřitelné):
    ```
    def function(a, b):
        """Do X and return a list."""
        pass
    ```

---

# **PEP 257 - Docstring**

- multi-line docstring
    ```
    def complex(real=0.0, imag=0.0):
        """Form a complex number.

        Keyword arguments: <- pripadne numpy/google style parametry
        real -- the real part (default 0.0)
        imag -- the imaginary part (default 0.0)
        """

        if imag == 0.0 and real == 0.0:
            return complex_zero
        ...
    ```

---


# [**Pylint**](https://pypi.org/project/pylint/)

- statická analýza kódu - bez nutnosti spuštění
- hledání chyb, mrtvého kódu, `code smells`
- navrhuje refaktor kódu
- spuštění pomocí `pylint [options] module` (`pylint .`)
- použití `.pylintrc`, případně cmd options

---

# [**Pylint**](https://pypi.org/project/pylint/)
```
class Test:

    def __init__(self):
        import math; print(math.PI)
        x = 5; y = "hello"; print(x + y)

    def access_dict(self):
        my_dict = {"name": "Alice", "age": 30}; print(my_dict['city'])
```

---

# [**Pylint**](https://pypi.org/project/pylint/)

```
pylint/simplecaesar.py:3:0: C0303: Trailing whitespace (trailing-whitespace)
pylint/simplecaesar.py:7:0: C0303: Trailing whitespace (trailing-whitespace)
pylint/simplecaesar.py:9:0: C0304: Final newline missing (missing-final-newline)
pylint/simplecaesar.py:1:0: C0114: Missing module docstring (missing-module-docstring)
pylint/simplecaesar.py:2:0: C0115: Missing class docstring (missing-class-docstring)
pylint/simplecaesar.py:5:8: C0415: Import outside toplevel (math) (import-outside-toplevel)
pylint/simplecaesar.py:5:21: C0321: More than one statement on a single line (multiple-statements)
pylint/simplecaesar.py:5:27: E1101: Module 'math' has no 'PI' member (no-member)
pylint/simplecaesar.py:6:8: C0103: Variable name "x" doesn't conform to snake_case naming style (invalid-name)
pylint/simplecaesar.py:6:15: C0321: More than one statement on a single line (multiple-statements)
pylint/simplecaesar.py:6:15: C0103: Variable name "y" doesn't conform to snake_case naming style (invalid-name)
pylint/simplecaesar.py:8:4: C0116: Missing function or method docstring (missing-function-docstring)
pylint/simplecaesar.py:9:48: C0321: More than one statement on a single line (multiple-statements)
pylint/simplecaesar.py:2:0: R0903: Too few public methods (1/2) (too-few-public-methods)

------------------------------------------------------------------
Your code has been rated at 0.00/10 (previous run: 0.00/10, +0.00)
```

---

# [`isort`](https://pycqa.github.io/isort/)

- automatické řazení importů
- použití na konkrétní adresář, soubor
- `python -m isort .`

---

# [`isort`](https://pycqa.github.io/isort/)

```
from my_module import func

import numpy as np
import math
import pandas as pd
```

---

# [`isort`](https://pycqa.github.io/isort/)

```
import math

import numpy as np
import pandas as pd
from my_module import func
```

---

# [`black`](https://github.com/psf/black)

- automatické (**pouze**) formátování kódu
- použití na konkrétní adresář, soubor
- `python -m black {source_file_or_directory}...`

---

# **Mypy**
- statická kontrola typů
- na `mypy` založeno `PEP 484 – Type Hints` - přidání typů k proměnným, se kterými pracujeme
    ```
    def greeting(name: str) -> str:
        return 'Hello ' + name
    ```
---
# **Mypy**

#### Základní typy
- `str, int, float, bool, None` - podobnost s datovými typy v [`numpy`](https://numpy.org/doc/stable/user/basics.types.html)

---

# **Mypy**

#### Datové struktury
- z modulu `typing`:
    ```
    from typing import TypeVar, Iterable, List

    def getter(array: List[str], item: str) -> str:
        return item

    def feeder(str) -> None:
        pass

    feeder(getter(['A', 'B', 'C'], 'A'))
    ```
---

# **Mypy**

#### Generika
```
from typing import TypeVar, Any

T = TypeVar('T', int, float, complex)

def func(x: T = 1.0, y: Any) -> None:
    pass
```

---
# **Mypy**

#### Specifikace parametrů
```
from typing import Union, Optional, List, Dict
def func(x: Union[str, int], y: Optional[Dict[str, List[int]]]):
    pass
```

---
# **Mypy**

#### Typování proměnných
```
age: int = 1

# Neni potreba inicializace
a: int 

# Typovani podminek
child: bool
if age < 18:
    child = True
else:
    child = False
```

---
# **Mypy**

#### Typování proměnných - datové typy
```
# redundantni - mypy dela automaticky
x: int = 1
z: float = 1.0

# python < 3.9
from typing import List, Dict
x: List[int] = [1]
x: Dict[str, float] = {"field": 2.0}
```


---



# **Mypy - použití**

- instalace přes `pip`
- `mypy <file>/<folder>`

1. Napište program, který načte od uživatele vstup a přičtěte k němu číslo `1`. Tento program zkontrolujte pomocí `mypy`.

```
input_number = input("Zadej číslo: ")
print("Výsledek je: ", input_number + 1)
```

---

# **Mypy - použití**

- Kontrola typů z jiného modulu:
```
from pathlib import Path

def load_template(template_path: Path, name: str) -> str:
    # Mypy ví, že `file_path` má metodu `read_text` a vrací `str`
    template_length = template_path.read_text()
    # takže tuto operaci zastaví
    return template_length + 1
```

---

# **AI pomocníci - ChatGPT**

- Vytvořeno OpenAI (GPT-4, DALL-E)
- Nyní GPT-4
- Pomocník formou chatu (prompt - odpověď)
- [https://chat.openai.com/chat](https://chat.openai.com/chat)
- Nutný účet (Microsoft, Google), ale zdarma

---
# **AI pomocníci - ChatGPT**

> Write me an example python code for Fibonacci sequence both recursive and in loop complying to both pytlint and mypy standards.

> Write me rc file for pylint to ignore following errors: C0114, C0115, C0116

> Write the most beautiful yet complex Python algorithm on 10 lines tops

> How to ...

---

# **AI pomocníci - ChatGPT**

```
from typing import List

# Recursive solution
def fibonacci_recursive(n: int) -> int:
    if n <= 1:
        return n
    else:
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

# Loop solution
def fibonacci_loop(n: int) -> List[int]:
    fib = [0, 1]
    for i in range(2, n+1):
        fib.append(fib[i-1] + fib[i-2])
    return fib
```

---

# **AI pomocníci - Github copilot**
- Párové programování s AI
- [https://copilot.github.com/](https://copilot.github.com/)
- Integrace pro VS Code, PyCharm, ...
- Placené (10$/měsíc)

- Nápověda podle kontextu, nebo komentářů
- Automatické psaní unit testů pro vybraný kus kódu

