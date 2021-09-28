# Щоб зареєструвати хуки з pytest, їх потрібно структурувати у власному модулі або класі.
# Цей клас або модуль можна потім передати за pluginmanagerдопомогою pytest_addhooksфункції
# (яка сама є гачком, виявленим pytest).
import pytest


def pytest_addhooks(pluginmanager):
    """ This example assumes the hooks are grouped in the 'sample_hook' module. """
    from hook_function import hook

    pluginmanager.add_hookspecs(hook)


@pytest.fixture()
def my_fixture(pytestconfig):
    # call the hook called "pytest_my_hook"
    # 'result' will be a list of return values from all registered functions.
    result = pytestconfig.hook.pytest_my_hook(config=pytestconfig)
