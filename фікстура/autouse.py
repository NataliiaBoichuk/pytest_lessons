# «autouse»-фикстуры соблюдают область действия, определенную с помощью параметра scope=:
# если для фикстуры установлен уровень scope='session' - она будет инициализирована только один раз,
# при этом неважно, где она определена. scope='class' означает инициализацию один раз для класса и т. д.
#
# если «autouse»-фикстура определена в тестовом модуле, то ее будут автоматически использовать все тесты модуля.
#
# если «autouse»-фикстура определена в файле conftest.py,
# то вызывать фикстуру будут все тесты во всех тестовых модулях соответствующей директории.
import datetime
import random
import time
import pytest


@pytest.fixture(autouse=True)
def check_duration(request, cache):
    key = 'duration/' + request.node.nodeid.replace(':', '_')
    # идентификатор узла (nodeid) может иметь двоеточия
    # ключи становятся именами файлов внутри .cache
    # меняем двоеточия на что-то безопасное в имени файла
    start_time = datetime.datetime.now()
    yield
    stop_time = datetime.datetime.now()
    this_duration = (stop_time - start_time).total_seconds()
    last_duration = cache.get(key, None)
    cache.set(key, this_duration)
    if last_duration is not None:
        errorstring = "длительность теста первышает последний боле чем в 2-а раза "
        assert this_duration <= last_duration * 2, errorstring


@pytest.mark.parametrize('i', range(5))
def test_slow_stuff(i):
    time.sleep(random.random())

