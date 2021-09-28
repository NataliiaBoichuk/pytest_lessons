# Расширяя предыдущий пример, мы можем указать фикстуре,
# что нужно создавать два объекта smtp_connection,
# тем самым заставив все тесты, ее использующие, выполняться дважды:

import pytest
import smtplib


@pytest.fixture(scope="module", params=["smtp.gmail.com", "mail.python.org"])
def smtp_connection(request):
    smtp_connection = smtplib.SMTP(request.param, 587, timeout=5)
    yield smtp_connection
    print("finalizing {}".format(smtp_connection))
    smtp_connection.close()


def pytest_addoption(parser):
    parser.addoption(
        "--stringinput",
        action="append",
        default=[],
        help="list of stringinputs to pass to test functions",
    )


def pytest_generate_tests(metafunc):
    if "stringinput" in metafunc.fixturenames:
        metafunc.parametrize("stringinput", metafunc.config.getoption("stringinput"))

