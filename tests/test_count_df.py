import subprocess
import sys
sys.path.insert(0, './answers')
from answer import count_df

def test_count_df():
    a = count_df("./data/frenepublicinjection2016.csv")
    assert(a == 27244)
