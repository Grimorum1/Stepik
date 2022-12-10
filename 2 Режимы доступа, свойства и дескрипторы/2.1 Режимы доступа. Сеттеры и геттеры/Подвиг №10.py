"""
Подвиг 10 (на повторение). Объявите класс EmailValidator для проверки корректности email-адреса. Необходимо запретить создание объектов этого класса: при создании экземпляров должно возвращаться значение None, например:

em = EmailValidator() # None

В самом классе реализовать следующие методы класса (@classmethod):

get_random_email(cls) - для генерации случайного email-адреса по формату: xxxxxxx...xxx@gmail.com, где x - любой допустимый символ в email (латинский буквы, цифры, символ подчеркивания и точка);
check_email(cls, email) - возвращает True, если email записан верно и False - в противном случае.

Корректность строки email определяется по следующим критериям:

- допустимые символы: латинский алфавит, цифры, символы подчеркивания, точки и собачка @ (одна);
- длина email до символа @ не должна превышать 100 (сто включительно);
- длина email после символа @ не должна быть больше 50 (включительно);
- после символа @ обязательно должна идти хотя бы одна точка;
- не должно быть двух точек подряд.

Также в классе нужно реализовать приватный статический метод класса:

is_email_str(email) - для проверки типа переменной email, если строка, то возвращается значение True, иначе - False.

Метод is_email_str() следует использовать в методе check_email() перед проверкой корректности email. Если параметр email не является строкой, то check_email() возвращает False.

Пример использования класса EmailValidator (эти строчки в программе писать не нужно):

res = EmailValidator.check_email("sc_lib@list.ru") # True
res = EmailValidator.check_email("sc_lib@list_ru") # False

P.S. В программе требуется объявить только класс. На экран ничего выводить не нужно. 

"""

import random
class EmailValidator:
    a = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789._"

    def __new__(cls, *args, **kwargs):
        return None


    @classmethod
    def check_email(cls, email):
        if cls.__is_email_str(email):
            email1 = email.split("@")
            if len(email1)==2 and len(email1[0])<=100 and len(email1[1])<=50 and "." in email1[1] and ".." not in email:
                for i in email:
                    if i not in cls.a and i!="@":
                        return False

                return True
        return False



    @classmethod
    def get_random_email(cls):
        return "".join(random.sample(cls.a, 20))+"@gmail.com"

    @staticmethod
    def __is_email_str(email):
        if type(email) == str:
            return True
        return False
