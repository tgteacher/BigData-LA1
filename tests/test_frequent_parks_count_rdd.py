import sys
sys.path.insert(0, './answers')
from answer import frequent_parks_count_rdd

def test_frequent_parks_count_rdd():
    a = frequent_parks_count_rdd("./data/frenepublicinjection2016.csv")
    assert(a == open("tests/frequent.txt","r").read())
