from Student import STUDENT_LIMIT
from People import Grouplimit
from GroupIterator import GroupIterator

class Group:

    def __init__(self, curs):
        self.students = []
        self.curs = curs

    def addstudent(self, Student):
        if len(self.students) == STUDENT_LIMIT:
            raise Grouplimit(STUDENT_LIMIT, "Группа уже заполнена")
        if Student in self.students:
            raise ValueError("Студент уже есть в группе")

        self.students.append(Student)


    def delstudent(self, Student):
        if Student in self.students:
            self.students.remove(Student)

    def search(self, poisk):

        res = [i for i in self.students if i.surname == poisk]
        return f"\n".join(map(str, res)) or "Нет такого студента в группе"

    def search_simvol(self,poisk):
        res = [i for i in self.students if i.surname.startswith(poisk)]
        return f"\n".join(map(str, res)) or "Нет такого студента в группе"


    def __str__(self):
        res = f"{self.curs}:\n"
        res += "\n".join(map(str, self.students))
        return res

    def __getitem__(self, index):
        if isinstance(index, int):
            if 0 <= index <= len(self.students):
                return self.students[index]
            else:
                raise IndexError

        if isinstance(index, slice):
            res = []
            start = index.start or 0
            stop = index.stop or len(self.students)
            step = index.step or 1
            if start < 0 or stop > len(self.students):
                raise IndexError
            for i in range(start, stop, step):
                res.append(self.students[i])
            return res
        raise TypeError()

    def __len__(self):
        return len(self.students)

    def __iter__(self):
        return GroupIterator(self.students)