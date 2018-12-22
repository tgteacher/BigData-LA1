import subprocess
import sys
sys.path.insert(0, './answers')
from answer import parks

def test_count():
    a = parks("./data/frenepublicinjection2016.csv")
    assert(a == 8976)
