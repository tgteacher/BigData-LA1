import subprocess
import sys
sys.path.insert(0, './answers')
from answer import uniq_parks_df

def test_uniq_parks_df():
    a = uniq_parks_df("./data/frenepublicinjection2016.csv")
    assert(a == open("tests/list_parks.txt","r").read())
