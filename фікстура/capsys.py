# Фикстура capsys builtin обеспечивает две функциональные возможности: позволяет получить
# stdout и stderr из некоторого кода, и временно отключить захват вывода.
# Давайте посмотрим на получение stdout и stderr.

# Предположим, у вас есть функция для печати приветствия для stdout:
import sys


def greeting(name):
    print('Hi, {}'.format(name))


# Вы не можете проверить это,
# проверив возвращаемое значение. В
# ы должны как-то проверить stdout. Вы можете проверить результат с помощью capsys:


def test_greeting(capsys):
    greeting('Earthling')
    out, err = capsys.readouterr()
    assert out == 'Hi, Earthling\n'
    assert err == ''

    greeting('Brian')
    greeting('Nerd')
    out, err = capsys.readouterr()
    assert out == 'Hi, Brian\nHi, Nerd\n'
    assert err == ''


def yikes(problem):
    print('YIKES! {}'.format(problem), file=sys.stderr)


def test_yikes(capsys):
    yikes('Out of coffee!')
    out, err = capsys.readouterr()
    assert out == ''
    assert 'Out of coffee!' in err


def test_capsys_disabled(capsys):
    with capsys.disabled():
        print('\nalways print this') # всегда печатать это
    print('normal print, usually captured') # обычная печать, обычно захваченная