import sys
sys.path.insert(0, './answers')
from answer import uniq_parks_counts

def test_uniq_parks_count():
    a = uniq_parks_counts("./data/frenepublicinjection2014.csv")
    assert(a == open("tests/list_parks_count_undisclosed.txt","r").read())
