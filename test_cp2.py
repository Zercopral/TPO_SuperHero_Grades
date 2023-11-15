import pytest
from module_cp2 import get_zip_rows

#Тест
#@pytest.mark.xfail()
@pytest.mark.parametrize('avg, final_mark',
                             get_zip_rows())
def test_avg_mark(avg, final_mark):
    assert avg == final_mark