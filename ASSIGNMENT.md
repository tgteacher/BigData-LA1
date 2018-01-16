# LA1: Apache Spark RDD and DataFrame APIs

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

We will use the
[2016](http://donnees.ville.montreal.qc.ca/dataset/ebb813dd-a93f-4fb0-8137-80492a30a1fa/resource/0a5984e4-752f-401e-b2d9-aa0567535d39/download/frenepublicinjection2016.csv)
and
[2015](http://donnees.ville.montreal.qc.ca/dataset/ebb813dd-a93f-4fb0-8137-80492a30a1fa/resource/a57f787f-bde9-4a59-88d1-4ae742edd9b8/download/frenepublicinjection2015.csv)
data sets available in directory `data`.

# Counting entries

## Task

Write a Python script that prints the number of trees (non-header lines) in
the data file passed as first argument.

## Required syntax

`count.py <data_file>`

## Test

`tests/test_count.py`

# Filtering

## Task

Write a Python script that prints the number of trees that are *located in
a park*.

## Required syntax

`parks.py <data_file>`

## Test

`tests/test_parks.py`

# Unique elements

## Task

Write a Python script that prints the list of unique parks where trees
were treated. The list must be ordered alphabetically. Every element in the list must be printed on
a new line.

## Required syntax

`uniq_parks.py <data_file>`

## Test

`tests/test_uniq_parks.py`

# Unique counts

## Task

Write a Python script that counts the number of trees treated in each
park and prints a list of "park: count" pairs ordered alphabetically
by the park name. Every element in the list must be printed on a new
line.

## Required syntax

`uniq_parks_counts.py <data_file>`

## Test

`tests/test_uniq_parks_counts.py`

# Most frequent items

## Task

Write a Python script that prints the list of the 10 parks with the
highest number of treated trees. Parks must be ordered by decreasing
number of treated trees. Every list element must be printed on a new line.

## Required syntax

`frequent_parks_count.py`

## Test

`tests/test_frequent_parks_count.py`

# File combinations

## Task

Write a Python script that prints the alphabetically sorted list of
parks that had trees treated both in 2016 and 2015. Every list element
must be printed on a new line.

## Required syntax

`intersection.py <data_file_1> <data_file_2>`

## Test

`tests/test_intersection.py`

# RDDs

## Task

Re-implement all the tasks above using Apache
Spark's Resilient Distributed Datasets API (RDD, see documentation
[here](https://spark.apache.org/docs/latest/rdd-programming-guide.html)). Outputs
must be identical to the ones obtained above in plain Python. Note:
all operations must be re-implemented using the RDD API -- for
instance, you are not allowed to simply convert results obtained with
plain Python to RDDs.

## Required syntax

- `count_rdd.py <data_file>`
- `parks_rdd.py <data_file>`
- `uniq_parks_rdd.py <data_file>`
- `uniq_parks_counts_rdd.py <data_file>`
- `frequent_parks_count_rdd.py`
- `intersection_rdd.py <data_file_1> <data_file_2>`

## Tests

- `tests/test_count_rdd.py`
- `tests/test_parks_rdd.py`
- `tests/test_uniq_parks_rdd.py`
- `tests/test_uniq_parks_counts_rdd.py`
- `tests/test_frequent_parks_count_rdd.py`
- `tests/test_intersection_rdd.py`

# DataFrames


## Task

Re-implement all the tasks above using Apache
Spark's DataFrame API (see documentation
[here](https://spark.apache.org/docs/latest/sql-programming-guide.html)). Outputs
must be identical to the ones obtained above in plain Python. Note:
all operations must be re-implemented using the DataFrame API -- for
instance, you are not allowed to simply convert results obtained with
the RDD API to Data Frames.

## Required syntax

- `count_df.py <data_file>`
- `parks_df.py <data_file>`
- `uniq_parks_df.py <data_file>`
- `uniq_parks_counts_df.py <data_file>`
- `frequent_parks_count_df.py`
- `intersection_df.py <data_file_1> <data_file_2>`

## Tests

- `tests/test_count_df.py`
- `tests/test_parks_df.py`
- `tests/test_uniq_parks_df.py`
- `tests/test_uniq_parks_counts_df.py`
- `tests/test_frequent_parks_count_df.py`
- `tests/test_intersection_df.py`

# Undisclosed tests

The following tests will be used to evaluate your assignment but will
remain undisclosed.

- All tests will be repeated using different datasets complying to the
  same format. This is to prevent you from just hard-coding the
  results of the tests in your answers. Hard-coded answers will be
  graded at most 50%, since all tests will be repeated on undisclosed
  data.

The total number of tests will be 36, distributed as follows:
- 12 plain Python tests (6 disclosed, 6 undisclosed)
- 12 RDD tests (6 disclosed, 6 undisclosed)
- 12 DataFrame tests (6 disclosed, 6 undisclosed)
