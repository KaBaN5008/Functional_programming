import re
from functools import reduce
from typing import Optional


TEXT = """Functional programming is simple, simple, and pure.
Pure functions are deterministic; functions avoid side effects.
"""


# Уровень 1
def split_words(text: str) -> list[str]:
    return re.findall(r"[a-zа-яё0-9]+", text.lower())


# Уровень 2
def count_word_frequencies(words: list[str]) -> dict[str, int]:
    return reduce(
        lambda frequencies, word: frequencies | {word: frequencies.get(word, 0) + 1},
        words,
        {},
    )


# Уровень 3
def top_word(freq: dict[str, int]) -> Optional[str]:
    return max(
        freq,
        key=freq.get,
        default=None,
    )


# Уровень 4
# Функции чистые: они не меняют входные данные, не печатают результат и не работают
# с файлами. При одинаковых аргументах они всегда возвращают одинаковые значения,
# поэтому их можно назвать детерминированными. Для пустой строки split_words
# возвращает [], count_word_frequencies возвращает {}, а top_word возвращает None.
