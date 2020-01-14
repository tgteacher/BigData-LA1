import subprocess
import sys
sys.path.insert(0, './answers')
from answer import uniq_parks_dask

def test_uniq_parks_dask():
    a = uniq_parks_dask("./data/frenepublicinjection2016.csv")
    assert(a == open("tests/list_parks.txt","r").read())
