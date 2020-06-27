"""
Разработка классов и объектов «запись», «комментарий» для приложения «Блог» (использование наследования).
"""
class Blog():
  entries = []
  users = []
  
  def __init__(self, title, owner):
    self.title = title
    self.owner = owner

  def __str__(self):
    res = ""
    for entry in self.entries:
      res += str(entry)
    return res
  
  def add_entry(self, entry):
    self.entries.append(entry)
  
  def delete_entry(self, id):
    for i in range(len(self.entries)):
      if self.entries[i].id == id:
        del self.entries[i]


class Entry():
  def __init__(self, title, text, id):
    self.title = title
    self.text = text
    self.id = id
    self.comments = []
  
  def __str__(self):
    entry = f"\n{self.title}\n{self.text}\n\n"
    comments = ""
    for comment in self.comments:
      comments += str(comment)
    return entry + comments

  def add_comment(self, comment):
    self.comments.append(comment)
  
  def delete_comment(self, id):
    for i in range(len(self.comments)):
      if self.comments[i].id == id:
        del self.comments[i]
  

class Comment():
  def __init__(self, author, text, id):
    self.author = author
    self.text = text
    self.id = id
  
  def __str__(self):
    return f"\tComment by {self.author}: {self.text}\n"


class User():
  def __init__(self, login, pwd):
    self.login = login
    self.pwd = pwd
    self.attr = {}
  
  def __str__(self):
    return self.login
  

class Owner(User):
  def __init__(self, login, pwd, blog_title):
    User.__init__(self, login, pwd)
    self.blog = Blog(blog_title, self)
  
  def delete_user(self, login):
    for i in range(len(self.blog.users)):
      if self.blog.users[i].login == login:
        del self.blog.users[i]


admin = Owner("admin", "pass", "My blog")
blog = admin.blog

user1 = User("Jax", "123")

entry1 = Entry("First entry", "Some text", 0)
entry2 = Entry("Second entry", "Even more text", 1)
entry_love = Entry("For Jax only", "Jax, I love you <3", 69)
entry3 = Entry("I'm leaving", "Blame Jax. Bye.", 2)

comment1 = Comment(user1, "Nice post!", 0)
entry1.add_comment(comment1)

comment69 = Comment(user1, "You're not my type, sorry. Let's be friends?", 69)
entry_love.add_comment(comment69)

comment2 = Comment(user1, "Nooo, come back! I miss you!", 2)
entry3.add_comment(comment2)

blog.add_entry(entry1)
blog.add_entry(entry2)
blog.add_entry(entry_love)
blog.add_entry(entry3)

print(blog)
