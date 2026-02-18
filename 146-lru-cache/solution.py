from typing import List, Optional

class Node:
    def __init__(
        self,
        key: int,
        val: int,
        next: Optional['Node'] = None,
        prev: Optional['Node'] = None,
    ):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.nodes: dict[int, Node] = {}
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node: Node):
        """Disconnects a node from the list (guranteed it exists)"""
        prev = node.prev
        nxt = node.next
        if prev:
            prev.next = nxt
        if nxt:
            nxt.prev = prev
        node.prev = node.next = None

    def _add_to_mru(self, node: Node):
        """Adds a node to the MRU (tail) end"""
        last = self.tail.prev
        node.prev = last
        node.next = self.tail
        if last:
            last.next = node
        self.tail.prev = node

    def _move_to_mru(self, node: Node):
        """Moves an existing node to the MRU position"""
        self._remove(node)
        self._add_to_mru(node)

    def _evict_lru(self):
        """Evicts the node at the LRU position (head)"""
        lru = self.head.next
        if not lru or lru is self.tail:
            return
        self._remove(lru)
        del self.nodes[lru.key]
        

    def get(self, key: int) -> int:
        if key in self.nodes:
            node = self.nodes[key]
            self._move_to_mru(node)
            return node.val
        return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.nodes:
            node = self.nodes[key]
            node.val = value
            self._move_to_mru(node)
        else:
            node = Node(key, value)
            self.nodes[key] = node
            self._add_to_mru(node)

        if len(self.nodes) > self.capacity:
            self._evict_lru()


if __name__ == "__main__":
    cache = LRUCache(2)
