import random


class Array:
    def __init__(self, row, col, empty=0):
        self.empty = empty

        self.array = []
        self.row = row
        self.col = col
        for i in range(row):
            r = []
            for j in range(col):
                r.append(empty)
            self.array.append(r)

    def __getitem__(self, index):
        return self.array[index]

    def get(self):
        return self.array

    def contains(self, element):
        for i in self.array:
            if element in i:
                return True
        return False

    def addDigit(self):
        freeCells = []
        for i in range(self.row):
            for j in range(self.col):
                if self.array[i][j] == self.empty:
                    freeCells.append([i, j])
        if freeCells:
            i, j = random.choice(freeCells)
            self.array[i][j] = random.choice([2, 4])

    def move(self, direction):
        for i in range(self.row):
            if direction == 1:
                for j in range(self.col - 1, 0, -1):
                    if self.array[i][j] == self.empty:
                        for k in range(j, -1, -1):
                            if self.array[i][k] != self.empty:
                                self.array[i][j] = self.array[i][k]
                                self.array[i][k] = self.empty
                                break

            elif direction == -1:
                for j in range(self.col):
                    if self.array[i][j] == self.empty:
                        for k in range(j, self.col):
                            if self.array[i][k] != self.empty:
                                self.array[i][j] = self.array[i][k]
                                self.array[i][k] = self.empty
                                break

    def sum(self):
        for i in range(self.row):
            for j in range(self.col - 1, 0, -1):
                if self.array[i][j] == self.array[i][j - 1] and self.array[i][j] != self.empty:
                    self.array[i][j] = 2 * self.array[i][j]
                    self.array[i][j - 1] = self.empty

    def shift(self):
        self.array = [*zip(*self.array)]
        row = self.row
        self.row = self.col
        self.col = row
        for i in range(self.row):
            self.array[i] = list(self.array[i])
