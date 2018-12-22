import subprocess
import sys
sys.path.insert(0, './answers')
from answer import count

def test_count():
    a = count("./data/frenepublicinjection2016.csv")
    assert(a == 27244)
