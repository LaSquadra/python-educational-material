# Lesson 12 Notes: Imports And Modules

Imports let one Python file use code from another file or from the standard
library.

## Big Idea

A module is a Python file. Importing lets you reuse code from that file.

```python
import math
```

After importing, you can use names from the module:

```python
math.pi
```

## Whole Module vs Specific Name

Importing the whole module keeps the module name visible:

```python
import pathlib
```

Importing a specific name can make code shorter:

```python
from pathlib import Path
```

Both styles are useful. Choose the one that makes your code clearer.

## The `__name__` Guard

The guard:

```python
if __name__ == "__main__":
    main()
```

means "run `main()` only when this file is run directly." This prevents script
startup code from running automatically when another file imports it.

## Modules vs Classes

- A module groups related code in a file.
- A class describes a kind of object.

They solve different organization problems.

## Common Beginner Mistakes

- Importing a package that is not installed.
- Naming a file the same as a standard library module.
- Forgetting that imported code can run if it is not guarded.
