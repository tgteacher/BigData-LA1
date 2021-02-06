import sys
sys.path.insert(0, './answers')
from answer import intersection_df

def test_intersection_df():
    a = intersection_df("./data/frenepublicinjection2016.csv", "./data/frenepublicinjection2015.csv")
    try:
        out = open("tests/intersection.txt","r").read()
        assert(a == out)
    except:
        try:
            out = open("tests/intersection.txt","r", encoding="ISO-8859-1").read()
            assert(a == out)
        except:
            try:
                out = open("tests/intersection.txt","r", encoding="utf-8").read()
                assert(a == out)
            except:
                out = open("tests/intersection.txt","r", encoding="latin1").read()
                assert(a == out)
