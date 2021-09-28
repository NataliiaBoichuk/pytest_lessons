# С помощью встроенной фикстуры pytestconfig вы можете управлять тем,
# как pytest работает с аргументами и параметрами командной строки, файлами конфигурации, плагинами и каталогом,
# из которого вы запустили pytest. Фикстура pytestconfig является ярлыком для request.config,
# и иногда упоминается в документации pytest как "the pytest config object"(объект конфигурации pytest).

# Мы будем использовать pytest hook pytest_addoption,
# чтобы добавить несколько параметров к параметрам, уже доступным в командной строке pytest:

# Добавление параметров командной строки через pytest_addoption должно выполняться через плагины
# или в файле conftest.py расположенного в верхней части структуры каталога проекта.
# Вы не должны делать это в тестовом подкаталоге.
#
# Параметры --myopt и --foo <value> были добавлены в предыдущий код, а строка справки была изменена, как показано ниже:

def pytest_addoption(parser):
    parser.addoption("--myopt", action="store_true",
                     help="some boolean option")
    parser.addoption("--foo", action="store", default="bar",
                     help="foo: bar or baz")


# @hookspec(historic=True)
# def pytest_addoption(parser: "Parser", pluginmanager: "PytestPluginManager") -> None:
    """Register argparse-style options and ini-style config values,
    called once at the beginning of a test run.

    .. note::

        This function should be implemented only in plugins or ``conftest.py``
        files situated at the tests root directory due to how pytest
        :ref:`discovers plugins during startup <pluginorder>`.

    :param pytest.Parser parser:
        To add command line options, call
        :py:func:`parser.addoption(...) <pytest.Parser.addoption>`.
        To add ini-file values call :py:func:`parser.addini(...)
        <pytest.Parser.addini>`.

    :param pytest.PytestPluginManager pluginmanager:
        The pytest plugin manager, which can be used to install :py:func:`hookspec`'s
        or :py:func:`hookimpl`'s and allow one plugin to call another plugin's hooks
        to change how command line options are added.

    Options can later be accessed through the
    :py:class:`config <pytest.Config>` object, respectively:

    - :py:func:`config.getoption(name) <pytest.Config.getoption>` to
      retrieve the value of a command line option.

    - :py:func:`config.getini(name) <pytest.Config.getini>` to retrieve
      a value read from an ini-style file.

    The config object is passed around on many internal objects via the ``.config``
    attribute or can be retrieved as the ``pytestconfig`` fixture.

    .. note::
        This hook is incompatible with ``hookwrapper=True``.
    """