import sys
sys.path.insert(0, './answers')
from answer import intersection_dask

def test_intersection_dask():
    a = intersection_dask("./data/frenepublicinjection2016.csv", "./data/frenepublicinjection2015.csv")
    assert(a == open("tests/intersection.txt","r").read())
