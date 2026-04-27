from typing import Any


class Node:
    def __init__(self, key: Any, key_hash: Any, value: Any) -> None:
        self.key = key
        self.hash = key_hash
        self.value = value


class Dictionary:
    def __init__(self) -> None:
        self.capacity = 8
        self.length = 0
        self.threshold = int(self.capacity * (2 / 3))
        self.load_factor = 2 / 3
        self.hash_table = [None] * self.capacity

    def __setitem__(self, key: Any, value: Any) -> None:
        if self.check_load_factor():
            self.resize()

        hash_key = hash(key)
        position = hash_key % self.capacity

        while self.hash_table[position] is not None:
            if self.hash_table[position].key == key:
                self.hash_table[position].value = value
                return

            position = (position + 1) % self.capacity

        self.hash_table[position] = Node(key, hash_key, value)
        self.length += 1

    def __getitem__(self, key: Any) -> Any:
        key_to_hash = hash(key)
        index = key_to_hash % self.capacity
        while self.hash_table[index] is not None:
            if self.hash_table[index].key == key:
                return self.hash_table[index].value

            index = (index + 1) % self.capacity

        raise KeyError((f"Key '{key}' was not found in the Dictionary."))

    def __len__(self) -> int:
        return self.length

    def resize(self) -> None:
        self.capacity *= 2
        self.threshold = int(self.capacity * (2 / 3))
        self.length = 0
        bucket = self.hash_table
        self.hash_table = [None] * self.capacity
        for node in bucket:
            if node:
                self.__setitem__(node.key, node.value)

    def clear(self) -> None:
        self.hash_table = [None] * self.capacity
        self.length = 0

    def check_load_factor(self) -> bool:
        if self.length >= self.threshold:
            return True

        return False
