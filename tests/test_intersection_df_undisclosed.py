import sys
sys.path.insert(0, './answers')
from answer import intersection_df

def test_intersection_df():
    a = intersection_df("./data/frenepublicinjection2014.csv", "./data/frenepublicinjection2015.csv")
    assert(a == open("tests/intersection_undisclosed.txt","r").read())
