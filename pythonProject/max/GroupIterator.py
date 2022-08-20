class GroupIterator:

    def __init__(self, studentss):
        self.studentss = studentss
        self.index = 0

    def __next__(self):
        if self.index < len(self.studentss):
            self.index += 1
            return self.studentss[self.index - 1]
        else:
            raise StopIteration

    def __iter__(self):
        return self