import pytest
from app import pc_utils


def test_cores():
    assert isinstance(pc_utils.get_cores_info(), int)


@pytest.mark.parametrize("n", range(100))
def test_cpu_usage(n):
    assert 0 <= pc_utils.get_cpu_usage_once() <= 100
