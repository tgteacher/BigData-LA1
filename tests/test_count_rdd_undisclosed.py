import subprocess
import os
import sys
sys.path.insert(0, './answers')
from answer import count_rdd

def test_count_rdd():
    a = count_rdd("./data/frenepublicinjection2014.csv")
    assert(a == 12828)
