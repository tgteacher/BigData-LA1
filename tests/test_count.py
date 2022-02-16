import subprocess
import sys
import os
sys.path.insert(0, os.path.join('.', 'answers'))
from answer import count

def test_count():
    a = count(os.path.join('.', 'data', 'frenepublicinjection2016.csv'))
    assert(a == 27244)
