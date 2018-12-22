import subprocess
import os
import sys
sys.path.insert(0, './answers')
from answer import parks_rdd

def test_parks_rdd():
    a = parks_rdd("./data/frenepublicinjection2014.csv")
    assert(a == 1698)
