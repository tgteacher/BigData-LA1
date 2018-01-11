import subprocess

def test_frequent_parks_count():
    command="python3 ./answers/frequent_parks_count_rdd.py data/frenepublicinjection2016.csv"
    process = subprocess.Popen(command, shell=True,
                               stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE)
    code=process.wait()
    assert(not code), "Command failed"
    assert(process.stdout.read()==open("tests/frequent.txt","r").read())
