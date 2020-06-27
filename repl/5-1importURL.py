# Реализация скрипта, позволяющего выполнять импорт удаленных файлов по URL. Запись скринкаста (документа со скриншотами) с демонстрацией работы скрипта. Формирование отчета по практическому заданию и публикация его в портфолио. 
from importlib.abc import PathEntryFinder
from importlib.util import spec_from_loader
import re
import sys
from urllib.request import urlopen


def url_hook(some_str):
    """ С помощью этой функции мы перехватываем ситуацию, в которой то,
    что мы собираемся импортировать является URL-адресом"""
    if not some_str.startswith(("http", "https")):
        raise ImportError
    with urlopen(some_str) as page:
        data = page.read().decode("utf-8")
    filenames = re.findall("[a-zA-Z_][a-zA-Z0-0_]*.py", data)
    modnames = {name[:-3] for name in filenames}
    return URLFinder(some_str, modnames)

sys.path_hooks.append(url_hook("https://github.com/Meao/university-portfolio/blob/master/python/toimport.py"))
# print(url_hook.__doc__)
print(sys.path_hooks)
# print(id(url_hook)) # адрес места в памяти, где лежит определение функции 
# print(id(sys.path_hooks[-1])) # адрес в списке path_hooks функции url_hook


class URLFinder(PathEntryFinder):
    def __init__(self, url, available):
        self.url = url
        self.available = available
        
    def find_spec(self, name, target=None):
        if name in self.available:
            origin = "{}/{}.py".format(self.url, name)
            loader = URLLoader()
            return spec_from_loader(name, loader, origin=origin)
        
        else:
            return None


# импорт для "перехваченного" адреса URL модуля  


class URLLoader:
    def create_module(self, target):
        return None
    
    def exec_module(self, module):
        with urlopen(module.__spec__.origin) as page:
            source = page.read()
        code = compile(source, module.__spec__.origin, mode="exec")
        exec(code, module.__dict__)

# Далее, чтобы продемонстрировать работу этого скрипта, мы должны запустить сервер http так, чтобы наш желаемый для импорта модуль "лежал" на сервере (например, в корневой директории сервера):

# python3.5 -m http.server
# После этого мы запускаем файл, в котором содержится код, размещенный выше (обязательно добавление в sys.path_hooks).

# python3.5 -i activation_script.py
# Теперь, если мы попытаемся импортировать файл remote.py, в котором размещен просто какой-нибудь

# print('Hello, world! This is remote module.')
# будет выведен ImportError, потому что такого модуля пока у нас нет (транслятор про него ничего не знает). Однако, как только мы выполним код:

# sys.path.append("http://localhost:8000")
# добавив путь, где располагается модуль, в sys.path, будет срабатывать наш "кастомный" URLLoader. В path_hooks будет содержатся наша функция url_hook.
# sys.path.append("https://github.com/Meao/dietapp/blob/master/manage.py")
# import manage
# manage.f()

# url_hook(https://github.com/Meao/dietapp/blob/master/manage.py)
sys.path.append("https://repl.it/@MarinaKrvtsn/importable#toimport.py")
import toimport
toimport.function2import()
