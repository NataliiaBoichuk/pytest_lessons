# Если вы планируете использовать фикстуру в нескольких тестах,
# то можно объявить ее в файле conftest.py.
# При этом импортировать ее не нужно - pytest найдет ее автоматически.
# Поиск фикстур начинается с тестовых классов, затем они иущется в тестовых модулях
# и в файлах conftest.py, и, в последнюю очередь, во встроенных и сторонних плагинах.

import pytest
import smtplib


@pytest.fixture(scope="module")
def smtp_connection():
    smtp_connection = smtplib.SMTP("smtp.gmail.com", 587, timeout=5)
    yield smtp_connection  # возвращает значение фикстуры
    print("teardown smtp")
    smtp_connection.close()