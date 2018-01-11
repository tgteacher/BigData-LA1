import subprocess

def test_intersection_rdd():
    command="python3 ./answers/intersection_rdd.py  data/frenepublicinjection2016.csv\
   ./data/frenepublicinjection2015.csv"
    process = subprocess.Popen(command, shell=True,
                               stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE)
    code=process.wait()
    assert(not code), "Intersection command failed"
    assert(process.stdout.read()==open("tests/intersection.txt","r").read())
