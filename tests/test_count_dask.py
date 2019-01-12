import subprocess
import sys
sys.path.insert(0, './answers')
from answer import count_dask

def test_count_dask():
    a = count_dask("./data/frenepublicinjection2016.csv")
    assert(a == 27244)
