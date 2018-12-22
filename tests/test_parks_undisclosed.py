import subprocess
import os
import sys
sys.path.insert(0, './answers')
from answer import parks

def test_count():
    a = parks("./data/frenepublicinjection2014.csv")
    assert(a == 1698)
