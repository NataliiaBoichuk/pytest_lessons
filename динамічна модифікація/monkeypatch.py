# Во время тестирования "monkey patching" —
# это удобный способ взять на себя часть среды выполнения тестируемого кода и
# заменить либо входные зависимости, либо выходные зависимости объектами или функциями,
# которые более удобны для тестирования.

# Фикстура monkeypatch обеспечивает следующие функции:
#
#
# setattr(target, name, value=<notset>, raising=True): Установить атрибут.
# delattr(target, name=<notset>, raising=True): Удалить атрибут.
# setitem(dic, name, value): Задать запись в словаре.
# delitem(dic, name, raising=True): Удалить запись в словаре.
# setenv(name, value, prepend=None): Задать переменную окружения .
# delenv(name, raising=True): Удалите переменную окружения.
# syspath_prepend(path): Начало пути в sys.путь, который является списком папок для импорта Python.
# chdir(path): Изменить текущий рабочий каталог.

# Параметр raising указывает pytest, следует ли создавать исключение,
# если элемент еще не существует.
# Параметр prepend для setenv() может быть символом.
# Если он установлен, значение переменной среды будет изменено на значение + prepend + <old value>.
import copy
import os
import json


def read_cheese_preferences():
    full_path = os.path.expanduser('~/.cheese.json')
    with open(full_path, 'r') as f:
        prefs = json.load(f)
    return prefs


def write_cheese_preferences(prefs):
    full_path = os.path.expanduser('~/.cheese.json')
    with open(full_path, 'w') as f:
        json.dump(prefs, f, indent=4)


def write_default_cheese_preferences():
    write_cheese_preferences(_default_prefs)


_default_prefs = {
    'slicing': ['manchego', 'sharp cheddar'],
    'spreadable': ['Saint Andre', 'camembert',
                   'bucheron', 'goat', 'humbolt fog', 'cambozola'],
    'salads': ['crumbled feta']
}


# Если у пользователя определен HOME set, os.path.expanduser() заменит ~ всем,
# что находится в переменной окружения пользователя HOME.
# Давайте создадим временный каталог и перенаправим HOME,
# чтобы указать на этот новый временный каталог:

def test_def_prefs_change_home(tmpdir, monkeypatch):
    monkeypatch.setenv('HOME', tmpdir.mkdir('home'))
    write_default_cheese_preferences()
    expected = _default_prefs
    actual = read_cheese_preferences()
    assert expected == actual

# У Windows, HOME та USERPROFILE буде використовуватися, якщо встановлено,
# інакше - комбінація HOMEPATH та HOMEDRIVE буде використовуватися.
# Ініціал ~user обробляється шляхом видалення останнього компонента каталогу зі створеного вище шляху користувача


def test_def_prefs_change_expanduser(tmpdir, monkeypatch):
    fake_home_dir = tmpdir.mkdir('home')
    monkeypatch.setattr(os.path, 'expanduser',
                        (lambda x: x.replace('~', str(fake_home_dir))))
    write_default_cheese_preferences()
    expected = _default_prefs
    actual = read_cheese_preferences()
    assert expected == actual

# Предположим, мы обеспокоены тем, что произойдет, если файл уже существует.
# Мы хотим быть уверенным, что он будет перезаписан по умолчанию,
# когда вызывается write_default_cheese_preferences():


def test_def_prefs_change_defaults(tmpdir, monkeypatch):
    # запись в файл один раз
    fake_home_dir = tmpdir.mkdir('home')
    monkeypatch.setattr(os.path, 'expanduser',
                        (lambda x: x.replace('~', str(fake_home_dir))))
    write_default_cheese_preferences()
    defaults_before = copy.deepcopy(_default_prefs)

    # изменение значений по умолчанию
    monkeypatch.setitem(_default_prefs, 'slicing', ['provolone'])
    monkeypatch.setitem(_default_prefs, 'spreadable', ['brie'])
    monkeypatch.setitem(_default_prefs, 'salads', ['pepper jack'])
    defaults_modified = _default_prefs

    # перезапись его измененными значениями по умолчанию
    write_default_cheese_preferences()

    # чтение и проверка
    # Поскольку _default_prefs-это словарь,
    # мы можем использовать monkeypatch.setitem(),
    # чтобы изменить элементы словаря только на время теста.
    actual = read_cheese_preferences()
    assert defaults_modified == actual
    assert defaults_modified != defaults_before
