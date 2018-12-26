import subprocess
import sys
sys.path.insert(0, './answers')
from answer import uniq_parks_df

def test_uniq_parks():
    a = uniq_parks_df("./data/frenepublicinjection2014.csv")
    assert(a == open("tests/list_parks_undisclosed.txt","r").read())
