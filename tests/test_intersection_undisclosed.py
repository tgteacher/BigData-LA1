import sys
sys.path.insert(0, './answers')
from answer import intersection

def test_intersection():
    a = intersection("./data/frenepublicinjection2014.csv", "./data/frenepublicinjection2015.csv")
    assert(a == open("tests/intersection_undisclosed.txt","r").read())
