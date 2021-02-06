import subprocess
import sys
sys.path.insert(0, './answers')
from answer import uniq_parks_dask

def test_uniq_parks_dask():
    a = uniq_parks_dask("./data/frenepublicinjection2016.csv")
    try:
        out = open("tests/list_parks.txt","r").read()
        assert(a == out)
    except:
        try:
            out = open("tests/list_parks.txt","r", encoding="ISO-8859-1").read()
            assert(a == out)
        except:
            try:
                out = open("tests/list_parks.txt","r", encoding="utf-8").read()
                assert(a == out)
            except:
                out = open("tests/list_parks.txt","r", encoding="latin1").read()
                assert(a == out)
