import subprocess
import sys
import os
sys.path.insert(0, os.path.join('.', 'answers'))
from answer import count_dask

def test_count_dask():
    a = count_dask(os.path.join('.', 'data', 'frenepublicinjection2016.csv'))
    assert(a == 27244)
