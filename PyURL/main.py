# Реализация скрипта, позволяющего выполнять импорт удаленных файлов по URL. Запись скринкаста (документа со скриншотами) с демонстрацией работы скрипта. Формирование отчета по практическому заданию и публикация его в портфолио. 
from importlib.abc import PathEntryFinder
from importlib.util import spec_from_loader
from importlib.util import module_from_spec
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
    filenames = ["urr"]
# filenames = re.findall("[a-zA-Z_][a-zA-Z0-0_]*.py", data)
#modnames = {name[:-3] for name in filenames}
    return URLFinder(some_str, filenames)


class URLFinder(PathEntryFinder):
    def __init__(self, url, available):
        self.url = url
        self.available = available
        
    def find_spec(self, name, target=None):
        if name in self.available:
            origin = "{}/{}.py".format(self.url, name)
            loader = URLLoader()
            spec = spec_from_loader(name, loader, origin=origin)
            return spec
        
        else:
            return None

class URLLoader:
    def create_module(self, target):
        return None
    
    def exec_module(self, module):
        with urlopen(module.__spec__.origin) as page:
            source = page.read()
        code = compile(source, module.__spec__.origin, mode="exec")
        exec(code, module.__dict__)


sys.path.append("http://localhost:8000")

finder = url_hook("http://localhost:8000")
# print(finder)

sys.path_hooks.append(finder)

# print(sys.path)

spec = finder.find_spec("urr")
# print(spec)
mod = module_from_spec(spec)
# print(mod)

spec.loader.exec_module(mod)

mod.f2import()

