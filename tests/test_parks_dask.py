import subprocess
import sys
import os
sys.path.insert(0, os.path.join('.', 'answers'))
from answer import parks_dask

def test_parks_dask():
    a = parks_dask(os.path.join('.', 'data', 'frenepublicinjection2016.csv'))
    assert(a == 8976)
