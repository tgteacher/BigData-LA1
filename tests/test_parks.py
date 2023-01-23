import os
from answers.answer import parks


def test_count():
    a = parks(os.path.join(".", "data", "frenepublicinjection2016.csv"))
    assert a == 8976
