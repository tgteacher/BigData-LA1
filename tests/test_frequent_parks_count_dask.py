import os
from answers.answer import frequent_parks_count_dask


def test_frequent_parks_count_dask():
    a = frequent_parks_count_dask(
        os.path.join(".", "data", "frenepublicinjection2016.csv")
    )

    try:
        out = open(os.path.join("tests", "frequent.txt"), "r").read()
        assert a == out
    except:
        try:
            out = open(
                os.path.join("tests", "frequent.txt"), "r", encoding="ISO-8859-1"
            ).read()
            assert a == out
        except:
            try:
                out = open(
                    os.path.join("tests", "frequent.txt"), "r", encoding="utf-8"
                ).read()
                assert a == out
            except:
                out = open(
                    os.path.join("tests", "frequent.txt"), "r", encoding="latin1"
                ).read()
                assert a == out
