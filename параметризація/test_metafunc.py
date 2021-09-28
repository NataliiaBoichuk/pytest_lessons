# pytest -q --stringinput="hello" --stringinput="world" test_metafunc.py

# Давайте також запустимо з введенням рядка, що призведе до невдалого тесту:
# pytest -q --stringinput="!" test_strings.py

# Зауважте, що при metafunc.parametrizeкількох викликах з різними наборами параметрів
# усі назви параметрів у цих наборах не можна дублювати, інакше буде виведена помилка.


def test_valid_string(stringinput):
    assert stringinput.isalpha()

