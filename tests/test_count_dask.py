import os
from answers.answer import count_dask

def test_count_dask():
    a = count_dask(os.path.join('.', 'data', 'frenepublicinjection2016.csv'))
    assert(a == 27244)
