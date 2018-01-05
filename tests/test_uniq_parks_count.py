import subprocess

def test_uniq_parks_count():
    command="python3 ./answers/uniq_parks_counts.py ./data/frenepublicinjection2016.csv"
    process = subprocess.Popen(command, shell=True,
                               stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE)
    code=process.wait()
    assert(not code), "Command failed"
    
    assert(process.stdout.read()==open("tests/list_parks_count.txt","r").read())
