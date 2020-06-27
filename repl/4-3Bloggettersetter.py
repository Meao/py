"""
Инвариантная самостоятельная работа

2.1. Разработка классов и объектов «запись», «комментарий» для приложения «Блог» (использование наследования).

2.2. Создание геттеров и сеттеров для классов «запись», «комментарий» приложения «Гостевая книга». Создание функций для вывода на печать информации, хранящийся в объектах.

2.3. Формирование отчета по практическому заданию и публикация его в портфолио.
Создание геттеров и сеттеров для классов «запись», «комментарий» приложения «Гостевая книга». Создание функций для вывода на печать информации, хранящийся в объектах.
"""
class Entry():
    def __init__(self, author, text):
        self.author = author
        self._text = text
        self.comments = []

    def print_entry(self):
        print('◯   ' + self.author)
        print(self._text)

    def print_comments(self):
        for comment in self.comments:
            comment.print_entry()
            print()

    @property
    def text(self):
        return self._text

    def add_comment(self, comment):
        self.comments.append(comment)

    @text.getter
    def text(self):
        return self._text

    @text.setter
    def text(self, text):
        self._text = text


class Comment(Entry):
    def __init__(self, author, text):
        super(Comment, self).__init__(author=author, text=text)


entry1 = Entry("Me", "Some text")

entry1.add_comment(Comment("user1", "Nice post!"))
entry1.add_comment(Comment("user2", "Let's be friends?"))

print("Entry")
entry1.print_entry()

print("\nComments")
entry1.print_comments()
