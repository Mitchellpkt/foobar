from typing import List

from numpy import vectorize


@vectorize
def capslock(message: str) -> str:
    return message.upper()


list_of_messages: List[str] = ["foo", "bar"]
print(list(capslock(list_of_messages)))
