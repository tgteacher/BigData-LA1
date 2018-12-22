import subprocess
import os
import sys
sys.path.insert(0, './answers')
from answer import parks_df

def test_parks_df():
    a = parks_df("./data/frenepublicinjection2014.csv")
    assert(a == 1698)
