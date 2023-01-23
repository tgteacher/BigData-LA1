import os
from answers.answer import parks_df


def test_parks_df():
    a = parks_df(os.path.join(".", "data", "frenepublicinjection2016.csv"))
    assert a == 8976
