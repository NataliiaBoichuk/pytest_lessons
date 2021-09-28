# Плагін пропонує два варіанти командного рядка для повторного запуску помилок з останнього pytestвиклику:
#
# --lf, --last-failed- запустити лише останні провалені
#
# --ff, --failed-first- спочатку запустити збої, а потім решту тестів.
#
# Для очищення (зазвичай не потрібно) --cache-clear опція
# дозволяє видалити весь вміст кешу між сеансами перед тестовим запуском.
#
# Ви завжди можете підглянути вміст кешу за допомогою параметра --cache-show командного рядка:

# Плагіни або код підтримки conftest.py можуть отримати кешоване значення за допомогою configоб'єкта pytest .
# Ось базовий приклад плагіна, який реалізує пристосування,
# яке повторно використовує раніше створений стан у всіх викликах pytest:

import pytest
import time


def expensive_computation():
    print("running expensive computation...")


@pytest.fixture
def mydata(request):
    val = request.config.cache.get("example/value", None)
    if val is None:
        expensive_computation()
        val = 42
        request.config.cache.set("example/value", val)
    return val


def test_function(mydata):
    assert mydata == 23

# Якщо ви виконуєте цю команду вперше, ви можете побачити оператор print:
# Якщо запустити його вдруге, значення буде вилучено з кешу, і нічого не буде надруковано:
