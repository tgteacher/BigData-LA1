import subprocess
import sys
import os
sys.path.insert(0, os.path.join('.', 'answers'))
from answer import parks

def test_count():
    a = parks(os.path.join('.', 'data', 'frenepublicinjection2016.csv'))
    assert(a == 8976)
