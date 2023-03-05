import pytest

from python_package_template.math import FnFloat, add, apply, mult


@pytest.mark.parametrize("params, result", [((1, 2), 3), ((1.5, 0.5), 2)])
def test_add(params: tuple[float, float], result: float) -> None:
    assert add(*params) == result


def test_mult() -> None:
    assert mult(0, 3) == 0


@pytest.mark.parametrize("fn, params, result", [(add, (1, 2), 3), (mult, (0, 4), 0)])
def test_apply_add(fn: FnFloat, params: tuple[float, float], result: float) -> None:
    assert apply(fn, *params) == result
