class Array:
    def __init__(self, a = []):
        self.array = a
    def QuickSort(self):
        left = 0
        right = len(self.array) - 1
        c = 0
        return self._QuickSort(left, right, c)
    def _QuickSort(self, left, right, c):
        if self.array == []:
            return self.array
        else:
            i = left
            j = right
            pivot = self.array[(i + j) // 2]
            while i <= j:
                while self.array[i] < pivot:
                    c += 1
                    i += 1
                c += 1
                while self.array[j] > pivot:
                    c += 1
                    j -= 1
                c += 1
                if i <= j:
                    a = self.array[i]
                    self.array[i] = self.array[j]
                    self.array[j] = a
                    i += 1
                    j -= 1
            if left < j:
                self._QuickSort(left, j, c)
            if i < right:
                self._QuickSort(i, right, c)
            return self.array
