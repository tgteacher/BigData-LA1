import subprocess
import os
import sys
sys.path.insert(0, './answers')
from answer import count

def test_count():
    a = count("./data/frenepublicinjection2014.csv")
    assert(a == 12828)
