from copy import copy
import heapq


class Heap:
    def __init__(self, array: list = None):
        if array and len(array) > 0:
            self.heap = copy(array)
            self._heapify()
        else:
            self.heap = list()

    def peek(self) -> int | None:
        return self.heap[0] if self.heap else None

    def pop(self) -> int:
        if self.heap:
            candidate = self.heap[0]
            if len(self.heap) > 1:
                self.heap[0] = self.heap[-1]
                self.heap.pop()
                self._sift_down(0)
                return candidate
            else:
                return self.heap.pop()
        else:
            raise RuntimeError("Heap object is empty")

    def push(self, new_arg: int):
        self.heap.append(new_arg)
        self._sift_up(len(self.heap) - 1)

    def push_pop(self, new_arg):
        if len(self.heap) == 0:
            return new_arg
        elif self.peek() >= new_arg:
            return new_arg
        else:
            result = self.heap[0]
            self.heap[0] = new_arg
            self._sift_down(0)
            return result

    def _heapify(self):
        idx = (len(self.heap) - 2) // 2
        while idx >= 0:
            self._sift_down(idx)
            idx -= 1

    @staticmethod
    def _get_parent(idx: int) -> int:
        return (idx - 1)//2

    def _get_left(self, idx) -> int | None:
        res = 2 * idx + 1
        return res if res < len(self.heap) else None

    def _get_right(self, idx) -> int | None:
        res = 2 * idx + 2
        return res if res < len(self.heap) else None

    def _sift_up(self, idx):
        p_idx = self._get_parent(idx)
        while idx > 0 and self.heap[p_idx] > self.heap[idx]:
            self.heap[p_idx], self.heap[idx] = self.heap[idx], self.heap[p_idx]
            idx = p_idx
            p_idx = self._get_parent(idx)

    def _sift_down(self, idx):
        left = self._get_left(idx)
        right = self._get_right(idx)
        if left is not None and right is not None:
            min_idx = left if self.heap[left] < self.heap[right] else right
            if self.heap[min_idx] < self.heap[idx]:
                self.heap[min_idx], self.heap[idx] = self.heap[idx], self.heap[min_idx]
                self._sift_down(min_idx)
        elif left is not None:
            if self.heap[left] < self.heap[idx]:
                self.heap[left], self.heap[idx] = self.heap[idx], self.heap[left]
                self._sift_down(left)


if __name__ == '__main__':
    arr = [1,4,6,78,54,8,5,4,4,42,2,0,1]
    heap = Heap(arr)