import os
from answers.answer import parks_rdd


def test_parks_rdd():
    a = parks_rdd(os.path.join(".", "data", "frenepublicinjection2016.csv"))
    assert a == 8976
