import os
from answers.answer import count


def test_count():
    a = count(os.path.join(".", "data", "frenepublicinjection2016.csv"))
    assert a == 27244
