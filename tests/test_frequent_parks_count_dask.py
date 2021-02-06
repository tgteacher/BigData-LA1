import sys
sys.path.insert(0, './answers')
from answer import frequent_parks_count_dask

def test_frequent_parks_count_dask():
    a = frequent_parks_count_dask("./data/frenepublicinjection2016.csv")

    try:
        out = open("tests/frequent.txt","r").read()
        assert(a == out)
    except:
        try:
            out = open("tests/frequent.txt","r", encoding="ISO-8859-1").read()
            assert(a == out)
        except:
            try:
                out = open("tests/frequent.txt","r", encoding="utf-8").read()
                assert(a == out)
            except:
                out = open("tests/frequent.txt","r", encoding="latin1").read()
                assert(a == out)
