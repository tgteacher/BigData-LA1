import sys
sys.path.insert(0, './answers')
from answer import frequent_parks_count_rdd

def test_frequent_parks_count_rdd():
    a = frequent_parks_count_rdd("./data/frenepublicinjection2014.csv")
    assert(a == open("tests/frequent_undisclosed.txt","r").read())
