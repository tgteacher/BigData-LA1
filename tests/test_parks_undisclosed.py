import subprocess
import os

def test_count():
    command="python ./answers/parks.py ./data/frenepublicinjection2014.csv"
    process = subprocess.Popen(command, shell=True,
                               stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE)
    code=process.wait()
    assert(not code), "Command failed"
    assert(process.stdout.read().decode("utf-8")=="1698"+os.linesep)
