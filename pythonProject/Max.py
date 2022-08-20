
import re

# 4. Напишите функцию, проверяющую правильность логина. Правильный логин – строка от 2 до 10 символов,
# содержащая только буквы и цифры.


def validation_login(login):
    pattern = r'(^[\w]{2,10}$)'
    result = re.findall(pattern, login)
    if result:
        return 'Valid'
    else:
        return 'Invalid'

login = 'kHlk0398km'
print(validation_login(login))