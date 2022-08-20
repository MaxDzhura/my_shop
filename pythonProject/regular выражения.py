# 1. Напишите регулярное выражение, которое будет находить в тексте фрагменты, состоящие из одной буквы R,
# за которой следует одна или более букв b, за которой одна r. Учитывать верхний и нижний регистр.

import re
text = 'Hello testRar test2Rbbbr test3Rbbb test4Rbr'
result = re.findall(r'Rb+r', text)
print(result)


# 2. Напишите функцию, выполняющую валидацию номера банковской карты (9999-9999-9999-9999).

def validation_bank_card(card):
    pattern = r'(^9{4}\-9{4}\-9{4}\-9{4}$)'
    result = re.findall(pattern, card)
    if result:
        return 'Valid'
    else:
        return 'Invalid'


bank_card = '9999-9999-9999-9999'
print(validation_bank_card(bank_card))


# 3. Напишите функцию, принимающую строковые данные и выполняющую проверку на их соответствие мейлу.
# Требования:
# -цифры (0-9).
# -только латинские буквы в большом (A-Z) и малом (a-z) регистрах.
# -в теле мейла допустимы только символы “_” и “-”. Но они не могут быть первым символом мейла.
# -символ “-” не может повторяться.


def valid_email(email):
    pattern = r'(^[A-Za-z0-9]+.[\w_]+.[\w_]+@[0-9A-Za-z]+\.[a-z]{2,7})'
    result = re.findall(pattern, email)
    if result:
        return 'Valid email'
    else:
        return 'Invalid email'

email = 'He-ll_o2-_72@gmail.com'
print(valid_email(email))


# 4. Напишите функцию, проверяющую правильность логина. Правильный логин – строка от 2 до 10 символов,
# содержащая только буквы и цифры.


def valid_login(l):
    pattern = r'(^[\w]{2,10}$)'
    result = re.findall(pattern, l)
    if result:
        return 'Valid'
    else:
        return 'Invalid'

login = 'kHlk0398km'
print(valid_login(login))