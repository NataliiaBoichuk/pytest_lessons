import pytest

# Последнее изменение, которое мы сделаем,
# это добавим параметр командной строки, --nice, чтобы изменения нашего статуса происходили,
# только если подставить --nice


def pytest_addoption(parser):
    """Включает nice функцию с опцией --nice."""
    group = parser.getgroup('nice')
    group.addoption("--nice", action="store_true",
                    help="nice: turn failures into opportunities")


def pytest_report_header():
    """Благодарность тестеру за выполнение тестов."""
    if pytest.config.getoption('nice'):
        return "Thanks for running the tests."


def pytest_report_teststatus(report):
    """Превращает неудачи в возможности."""
    if report.when == 'call':
        if report.failed and pytest.config.getoption('nice'):
            return (report.outcome, 'O', 'OPPORTUNITY for improvement')
