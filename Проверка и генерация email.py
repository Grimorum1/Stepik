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

assert EmailValidator.check_email(f"{'a' * 100}@{'b' * 45}.aaaa") == True
assert EmailValidator.check_email("i.like.this.course@my.stepik.domen.org") == True
assert EmailValidator.check_email('name.surname@mail.com') == True
assert EmailValidator.check_email(1342) == False
assert EmailValidator.check_email('a+a@m.c') == False
assert EmailValidator.check_email('aabda..kkk@m.c') == False
assert EmailValidator.check_email('aaaa@bbb..cc') == False
assert EmailValidator.check_email(f"{'a' * 100}@{'b' * 45}.aaaaa") == False
assert EmailValidator.check_email(f"{'a' * 101}@{'b' * 45}.aaaa") == False
assert EmailValidator.check_email(f"{'a'}@{'b' * 45}aaaa") == False
assert EmailValidator.check_email('name.surnamemail.com') == False
assert EmailValidator.check_email('name@mail') == False