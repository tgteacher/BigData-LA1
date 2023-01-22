import os
from answers.answer import count_rdd


def test_count_rdd():
    a = count_rdd(os.path.join(".", "data", "frenepublicinjection2016.csv"))
    assert a == 27244
