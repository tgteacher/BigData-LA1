import hashlib
import os
import subprocess

def test_download():
    os.remove("data/frenepublicinjection2016.csv")
    os.remove("data/frenepublicinjection2015.csv")
    command="python3 ./answers/download.py"
    process = subprocess.Popen(command, shell=True,
                               stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE)
    code=process.wait()
    assert(not code), "Download command failed"
    assert(os.path.exists("data/frenepublicinjection2016.csv")), "File frenepublicinjection2016.csv not found"
    assert(hashlib.md5(open("data/frenepublicinjection2016.csv",'rb').read()).hexdigest()=="b0ed7c3042d3f82dc56d7ef70802d4ee"), "Invalid file content"
    assert(os.path.exists("data/frenepublicinjection2015.csv")), "File frenepublicinjection2015.csv not found"
    assert(hashlib.md5(open("data/frenepublicinjection2015.csv",'rb').read()).hexdigest()=="fbe71a6b2bb71ddc649619102bfe2438"), "Invalid file content"
