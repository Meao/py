# Реализуем класс, в котором некоторое количество полей будут 'зафиксированы' (first_name, last_name, email, ...) - обязательные для добавления
# Предоставим возможность пользователю класса задавать дополнительные атрибуты, которые мы будем сохранять отдельно с помощью __setattr__ и получать с помощью __getattr__.pass

# Реализуем класс с тремя полями

# Реализуем методы getattr и setattr, чтобы возможно было получать атрибут city и задавать его


class New_client():

    attrs = {}

    def __init__(self, first_name, last_name, email):

        if not (type(first_name) == str and type(last_name) == str
                and type(email) == str):
            raise ValueError('Error! Некорректный тип данных.')
        else:
            self.__first_name, self.__last_name, self.__email = first_name, last_name, email

    def __getattr__(self, name):
        return New_client.attrs.get(name, 'No attribute or value')

    def __setattr__(self, name, value):
        if (name not in self.__dict__):
            New_client.attrs[name] = value
            
    def __str__(self):
        return "Name: {} {}".format(self.__first_name, self.__last_name)


c1 = New_client('Nick', 'Zhukov', 'nz@ya.ru')
# print(c1.city)

c1.city = 'Saint Petersburg'
# print(c1.city)

c2 = New_client('Paul', 'Ivanov', 'pivanov@ya.ru')
# print(c2.city)

print(c1)

# Реализовав getattr и setattr видна особенность: __getattr__ вызывается только, если __внутри класса атрибут__, который мы пытаемся использовать, отсутствует.

# Т.е. реализуется это только для атрибутов класса, а значит два объекта c1 и с2 будут иметь одно и тоже значение этого атрибута

# Таким образом, это имеет смысл делать только если есть такие атрибуты, которые являются общими для всех объектов класса.

# Если реализовывать класс с использованием getattr и setattr, то решение получается слишком громоздкое и неправильное с точки зрения проектирования архитектуры класса.

# Проанализируйте собственное решение и если необходимо (т.е. есть атрибуты, которые могут быть у всех объектов класса РегистрационнаяФорма) реализуйте данный механизм для класса регистрационной формы.

# Реализуйте для собственного класса с помощью методов __repr__ и __str__ методы, позволяющие выводить на экран с помощью функции print в человекочитаемом виде содержимое вашего объекта с регистрационной формой (см. пример с классом Counter в конспекте лекции)
