
from Student import Student
from Group import Group


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

try:
    gr1.addstudent(st4)
    gr1.addstudent(st2)
    gr1.addstudent(st1)
    gr1.addstudent(st3)

except Exception as ex:
    print(ex)
print(gr1)
print()
print(gr1.search("Гномов"))
print(gr1.search_simvol("Бобиков"))
print("*" * 40)
