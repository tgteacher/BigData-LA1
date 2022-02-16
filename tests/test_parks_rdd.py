import subprocess
import sys
import os
sys.path.insert(0, os.path.join('.', 'answers'))
from answer import parks_rdd

def test_parks_rdd():
    a = parks_rdd(os.path.join('.', 'data', 'frenepublicinjection2016.csv'))
    assert(a == 8976)
