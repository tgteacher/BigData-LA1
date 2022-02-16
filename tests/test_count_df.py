import subprocess
import sys
import os
sys.path.insert(0, os.path.join('.', 'answers'))
from answer import count_df

def test_count_df():
    a = count_df(os.path.join('.', 'data', 'frenepublicinjection2016.csv'))
    assert(a == 27244)
