from typing import TypeVar
from typing import Generic

T = TypeVar("T")

class Queue(Generic[T]):
    def __init__(self) -> None:
        self.nodes: list[T] = []

    def is_empty(self):
        return len(self.nodes) == 0

    def enqueue(self, value: T):
        self.nodes.append(value)

    def dequeue(self):
        return self.nodes.pop(0)

if __name__ == "__main__":
    queue = Queue[int]()

    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.enqueue(4)

    print(queue.nodes)

    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.dequeue())

    print(queue.nodes)
