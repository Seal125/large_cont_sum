import pytest
from large_cont_sum import large_cont_sum

# @pytest.mark.skip(reason='Implement first')
def test_large_cont_sum():
    assert large_cont_sum([1, 2, -1, 3, 4, 10, 10, -10, -1]) == 29
    assert large_cont_sum([1, 2, -1, 3, 4, -1]) == 9
    assert large_cont_sum([-1, 1]) == 1
