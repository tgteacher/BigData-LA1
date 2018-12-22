import subprocess
import sys
sys.path.insert(0, './answers')
from answer import count_rdd

def test_count_rdd():
    a = count_rdd("./data/frenepublicinjection2016.csv")
    assert(a == 27244)
