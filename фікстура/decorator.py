# Декоратор @pytest.fixture() используется, чтобы сообщить pytest,
# что функция является фикстурой.
# Когда вы включаете имя фикстуры в список параметров тестовой функции,
# pytest знает, как запустить её перед запуском теста.
# Фикстуры могут выполнять работу, а могут возвращать данные в тестовую функцию.

# Чтобы посмотреть список доступных фикстур, можно использовать опцию --fixtures:
#
# pytest --fixtures test_simplefactory.py

import pytest


@pytest.fixture
def smtp_connection():
    import smtplib

    return smtplib.SMTP("smtp.gmail.com", 587, timeout=5)


def test_ehlo(smtp_connection):
    response, msg = smtp_connection.ehlo()
    assert response == 250
    assert 0  # в демонстрационных целях
