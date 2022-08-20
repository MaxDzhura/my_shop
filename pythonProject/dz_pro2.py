
class Grouplimit(Exception):
    def __init__(self, value, message):
        super().__init__()
        self.value = value
        self.message = message

    def __str__(self):
        return f"{self.value},{self.message}"


class People:

    def __init__(self, surname, name, age):
        self.surname = surname.strip().title()
        self.name = name.strip().title()
        self.age = age

    def __str__(self):
        return f"{self.surname}--{self.name}--{self.age}"


class Student(People):

    def __init__(self, surname, name, age, gender):
        super().__init__(surname, name, age)
        self.gender = gender


    def __add__(self, other):

        tmp = Group("Питон")
        tmp.students.append(self)
        tmp.students.append(other)
        return tmp


    def __str__(self):
        return f"{super().__str__()}, {self.gender}"


STUDENT_LIMIT = 10

class Group:

    def __init__(self, course):
        self.students = []
        self.course = course

    def __add__(self, other):
        if isinstance(other,Student):
            self.students.append(other)
            return self


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
        res = f"{self.course}:\n"
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
            stop =  index.stop or len(self.students)
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




st1 = Student("Алексеев", "Альберто", "22", "Man")
st2 = Student("Веселовко", "Алекс", "19", "Man")
st3 = Student("Бобиков", "Вася", "23", "Man")
st4 = Student("Гномов", "Витя", "18", "Man")
st5 = Student("Таппнок", "Коля", "20", "Man")
st6 = Student("Таппнок", "Коля", "20", "Man")
st7 = Student("Таппнок", "Коля", "20", "Man")
st8 = Student("Таппнок", "Коля", "20", "Man")
st9 = Student("Таппнок", "Коля", "20", "Man")
st10 = Student("Таппнок", "Коля", "20", "Man")
st11 = Student("Таппнок", "Коля", "20", "Man")
st12 = Student("Таппнок", "Коля", "20", "Man")


gr1 = Group("Python")
x = st1 + st2 + st5 + st3
s = x[:2]
a = x[1]
print(s)

#try:
    #gr1.addstudent(st4)
    #gr1.addstudent(st2)
    #gr1.addstudent(st1)
    #gr1.addstudent(st3)

#except Exception as ex:
    #print(ex)

#print(gr1.search("Гномов"))
#print(gr1.search_simvol("Б"))
#print(gr)

# for i in x:
#     print(i)




