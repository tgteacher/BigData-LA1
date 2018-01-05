# Big Data LA 1

The goal of this assignment is to implement a basic analysis of
textual data using Apache Spark. To get started smoothly and become
familiar with the assignment's technical context (Git, GitHub,
pytest), we will implement a few steps in plain Python.


Important preliminary notes:

* The requested tasks, described below, are all evaluated with a test
  run with [pytest](http://pytest.org). Your assignment will be graded
  directly from the result of those tests, see details
  [here](./README.md). You may want to get familiar with pytest before
  you start.
  
* The tests contain examples of expected outputs that you may want to
  check in case the instruction below are unclear. Every detail in
  your answer counts! In particular, you should pay attention to the
  exact syntax of the expected output: forget a new line and the tests
  won't pass!

* Your answers to the tasks below *must* be located in directory `answers`. 

# Dataset

We will study a dataset provided by the city of Montreal that contains
the list of trees treated against the [emerald ash
borer](https://en.wikipedia.org/wiki/Emerald_ash_borer). The dataset
is described at
http://donnees.ville.montreal.qc.ca/dataset/frenes-publics-proteges-injection-agrile-du-frene
(use Google translate to translate from French to English). 

## Task

Write a Python script that downloads the [2016](http://donnees.ville.montreal.qc.ca/dataset/ebb813dd-a93f-4fb0-8137-80492a30a1fa/resource/0a5984e4-752f-401e-b2d9-aa0567535d39/download/frenepublicinjection2016.csv) and [2015](http://donnees.ville.montreal.qc.ca/dataset/ebb813dd-a93f-4fb0-8137-80492a30a1fa/resource/a57f787f-bde9-4a59-88d1-4ae742edd9b8/download/frenepublicinjection2015.csv) datasets to `data/frenepublicinjection2016.csv` and `data/frenepublicinjection2015.csv`.

## Required syntax

`download.py <data_file>`

## Test

`tests/test_adownload.py`

# Counting entries

## Task

Write a Python script that counts the number of entries (lines) in
the data file passed as first argument.

## Required syntax

`count.py <data_file>`

## Test

`tests/test_count.py`

# Filtering

## Task

Write a Python script that counts, in the data
set passed as first argument, the number of trees that are *located in
a park*.

## Required syntax

`parks.py <data_file>`

## Test

`tests/test_parks.py`

# Unique elements

## Task

Write a Python script that prints the list
of unique parks where trees from the data set passed as first argument
were treated. The list must be ordered alphabetically.

## Required syntax

`uniq_parks.py <data_file>`

## Test

`tests/test_uniq_parks.py`

# Unique counts

## Task

Write a Python script that counts the number of trees treated in each
park and prints a list of (park, count) pairs ordered alphabetically
by the park name.

## Required syntax

`uniq_parks_count.py <data_file>`

## Test

`tests/test_uniq_parks_count.py`

# Most frequent items

## Task

Write a Python script that prints the list of the 10 parks with the
highest number of treated trees. Parks must be ordered by decreasing
number of treated trees. The data file must be passed as argument.

## Required syntax

`frequent_parks_count.py`

## Test

`tests/test_frequent_parks_count.py`

# File combinations

## Task

Write a Python script that prints the
alphabetically sorted list of parks that had trees treated in 2016 and
2015 (data files must be passed as arguments).

## Required syntax

`intersection.py <data_file_1> <data_file_2>`

## Test

`tests/test_intersection.py`

# RDDs

# DataFrames

# Undisclosed tests

- Tests that the RDD or DataFrame API was used.
- Same tests, on a different dataset.