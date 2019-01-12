import subprocess
import sys
sys.path.insert(0, './answers')
from answer import parks_dask

def test_parks_dask():
    a = parks_dask("./data/frenepublicinjection2016.csv")
    assert(a == 8976)
