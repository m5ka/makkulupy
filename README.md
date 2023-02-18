# makkulupy 💬

**makkulupy** is a lightweight tool for accessing the makkulu dictionary API and returning its data in a Pythonic way.

## How to use
```python
import makkulupy

words = makkulupy.get_words(headword="makkulu")

for word in words:
    print(f"{word.headword} means {word.definition}")
```

## License
makkulupy is licensed under the **BSD 2 Clause** (see [LICENSE] to read in full)