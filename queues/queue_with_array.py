

class Queue:
    def __init__(self, initial_size = 10):
        self._array = [None for _ in range(initial_size)]
        self._queue_size = 0
        # always holds the position of the first added element, -1 in case queue empty
        self._front = -1
        # always points to the position where next element will be added
        self._tail = 0

    def size(self):
        return self._queue_size

    def is_empty(self):
        return len(self._array) == self._queue_size

    def enqueue(self, data):
        if self.size() == len(self._array):
            self._handle_capacity_full()

        self._array[self._tail] = data
        # move tail in a circular fashion to handle case in which front is not at 0 and there
        # is empty space before front
        self._tail = (self._tail + 1) % len(self._array)
        self._queue_size += 1

        # now that we know there is at least 1 element in queue so if front is at -1 move it to 0
        if self._front == -1:
            self._front = 0

    def _handle_capacity_full(self):
        # create a new array with double the size
        new_array = [None for _ in range(2 * len(self._array))]
        # copy the elements start from front to keep the order of elements as they were in old array
        index = 0
        for i in range(self._front, len(self._array)):
            new_array[index] = self._array[i]
            index += 1

        # as front can wrap around to go to start of array as well so now handle that case
        for i in range(0, self._front):
            new_array[index] = self._array[i]
            index += 1

        self._array = new_array
        # as we have copied front elements start from 0 in new array
        self._front = 0
        self._tail = index

    def dequeue(self):
        if self.is_empty():
            # reset front and back
            self._front = -1
            self._tail = 0
            return None

        front_value = self._array[self._front]
        # as tail can wrap around to start of array to fill in empty positions before when front has moved from 0 onward
        # so wrap around front as well to handle that case
        self._front = (self._front + 1) % len(self._array)
        self._queue_size -= 1
        return front_value

