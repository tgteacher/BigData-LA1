import subprocess
import sys
import os
sys.path.insert(0, os.path.join('.', 'answers'))
from answer import parks_df

def test_parks_df():
    a = parks_df(os.path.join('.', 'data', 'frenepublicinjection2016.csv'))
    assert(a == 8976)
