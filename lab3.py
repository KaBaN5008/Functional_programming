from dataclasses import dataclass
from enum import Enum
from typing import Generic, TypeAlias, TypeVar


T = TypeVar("T")
E = TypeVar("E")


# Уровень 1
class LoadState(Enum):
    LOADING = "loading"
    SUCCESS = "success"
    ERROR = "error"


# Уровень 2
@dataclass(frozen=True)
class User:
    name: str
    age: int
    email: str


# Уровень 3
@dataclass(frozen=True)
class Success(Generic[T]):
    value: T


@dataclass(frozen=True)
class Failure(Generic[E]):
    error: E


Result: TypeAlias = Success[T] | Failure[E]


USERS = (
    User("Alice", 21, "alice@example.com"),
    User("Bob", 25, "bob@example.com"),
    User("Charlie", 19, "charlie@example.com"),
)


def load_users() -> Result[list[User], str]:
    return (
        Success(list(USERS))
        if USERS
        else Failure("Список пользователей пуст")
    )


# Уровень 4
# Мощность LoadState равна 3, потому что у типа есть три возможных значения:
# LOADING, SUCCESS и ERROR.
#
# Мощность Result[list[User], str] равна мощности list[User] плюс мощности str:
# |Result[list[User], str]| = |Success[list[User]]| + |Failure[str]|.
# Так как строки, целые числа и списки в Python не имеют заданного конечного
# ограничения, этот тип можно считать бесконечным.
