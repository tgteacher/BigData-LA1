import os
from answers.answer import parks_dask


def test_parks_dask():
    a = parks_dask(os.path.join(".", "data", "frenepublicinjection2016.csv"))
    assert a == 8976
