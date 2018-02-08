import subprocess

def test_frequent_parks_count():
    command="python ./answers/frequent_parks_count_df.py data/frenepublicinjection2014.csv"
    process = subprocess.Popen(command, shell=True,
                               stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE)
    code=process.wait()
    assert(not code), "Command failed"
    assert(process.stdout.read().decode("utf-8")==open("tests/frequent_undisclosed.txt","r").read())
