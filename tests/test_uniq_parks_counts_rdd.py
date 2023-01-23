import os
from answers.answer import uniq_parks_counts_rdd


def test_uniq_parks_count_rdd():
    a = uniq_parks_counts_rdd(os.path.join(".", "data", "frenepublicinjection2016.csv"))
    try:
        out = open(os.path.join("tests", "list_parks_count.txt"), "r").read()
        assert a == out
    except:
        try:
            out = open(
                os.path.join("tests", "list_parks_count.txt"),
                "r",
                encoding="ISO-8859-1",
            ).read()
            assert a == out
        except:
            try:
                out = open(
                    os.path.join("tests", "list_parks_count.txt"), "r", encoding="utf-8"
                ).read()
                assert a == out
            except:
                out = open(
                    os.path.join("tests", "list_parks_count.txt"),
                    "r",
                    encoding="latin1",
                ).read()
                assert a == out
