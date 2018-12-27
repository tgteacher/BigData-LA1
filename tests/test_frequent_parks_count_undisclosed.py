import sys
sys.path.insert(0, './answers')
from answer import frequent_parks_count

def test_frequent_parks_count():
    a = frequent_parks_count("./data/frenepublicinjection2014.csv")
    assert(a == open("tests/frequent_undisclosed.txt","r").read())
