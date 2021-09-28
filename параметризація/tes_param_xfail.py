import sys
import pytest


@pytest.mark.parametrize(
    ("n", "expected"),
    [
        (1, 2),
        pytest.param(1, 0, marks=pytest.mark.xfail),
        pytest.param(1, 3, marks=pytest.mark.xfail(reason="some bug")),
        (2, 3),
        (3, 4),
        (4, 5),
        pytest.param(
            10, 11, marks=pytest.mark.skipif(sys.version_info >= (3, 0), reason="py2k")
        ),
    ],
)
def test_increment(n, expected):
    assert n + 1 == expected

# Це дозволить запустити тест з аргументами ,
# встановлених на x=0/y=2, x=1/y=2, x=0/y=3і x=1/y=3виснажливих параметри в порядку декораторів.


@pytest.mark.parametrize("x", [0, 1])
@pytest.mark.parametrize("y", [2, 3])
def test_foo(x, y):
    pass
