import subprocess

def test_uniq_parks_count_df():
    command="python ./answers/uniq_parks_counts_df.py ./data/frenepublicinjection2014.csv"
    process = subprocess.Popen(command, shell=True,
                               stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE)
    code=process.wait()
    assert(not code), "Command failed"
    
    assert(process.stdout.read().decode("utf-8")==open("tests/list_parks_count_undisclosed.txt","r").read())
