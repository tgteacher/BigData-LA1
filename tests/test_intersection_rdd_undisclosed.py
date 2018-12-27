import sys
sys.path.insert(0, './answers')
from answer import intersection_rdd

def test_intersection_rdd():
    a = intersection_rdd("./data/frenepublicinjection2014.csv", "./data/frenepublicinjection2015.csv")
    assert(a == open("tests/intersection_undisclosed.txt","r").read())
