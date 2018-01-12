import subprocess

def test_uniq_parks():
    command="python ./answers/uniq_parks_df.py ./data/frenepublicinjection2016.csv"
    process = subprocess.Popen(command, shell=True,
                               stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE)
    code=process.wait()
    assert(not code), "Command failed"
    assert(process.stdout.read().decode("utf-8")==open("tests/list_parks.txt","r").read())
