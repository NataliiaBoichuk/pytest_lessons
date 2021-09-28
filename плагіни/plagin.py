# Каждый раз, когда вы помещаете фикстуры и/или hook-функции в файл conftest.py
# верхнего уровня проекта, вы создаёте локальный плагин conftest

# pytest-django: write tests for django apps, using pytest integration.
#
# pytest-twisted: write tests for twisted apps, starting a reactor and processing deferreds from test functions.
#
# pytest-cov: coverage reporting, compatible with distributed testing
#
# pytest-xdist: to distribute tests to CPUs and remote hosts,
# to run in boxed mode which allows to survive segmentation faults,
# to run in looponfailing mode, automatically re-running failing tests on file changes.
#
# pytest-instafail: to report failures while the test run is happening.
#
# pytest-bdd: to write tests using behaviour-driven testing.
#
# pytest-timeout: to timeout tests based on function marks or global definitions.
#
# pytest-pep8: a --pep8 option to enable PEP8 compliance checking.
#
# pytest-flakes: check source code with pyflakes.
#
# oejskit: a plugin to run javascript unittests in live browsers.

# pip install --no-index --find-links=./some_plugins/ pytest-cov
# --no-index указывает pip не подключаться к PyPI.
# --find-links=./some_plugins/ указывает pip искать в каталоге some_plugins.
# В нашем примере мы создадим плагин, который изменит внешний вид статуса теста.
# Добавим параметр командной строки, чтобы включить это новое поведение.
# Добавим текст в выходной заголовок. В частности, мы изменим все индикаторы состояния FAILED (неудачный)
# на “OPPORTUNITY (перспективный) для усовершенствования,”
# изменим F на O, и добавим “Thanks for running the tests” (Спасибо за выполнение тестов) к заголовку.
# Для этого будем использовать опцию --nice
