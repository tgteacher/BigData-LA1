# LA1: Apache Spark RDD and DataFrame APIs

This repository is private in order to (1) encourage you to experiment
various solutions without the fear of making mistakes publicly (2)
discourage plagiarism, unauthorized collaboration and other offences
under Concordia's [Academic Code of Conduct](http://www.concordia.ca/students/academic-integrity/offences.html). You are encouraged to
discuss and exchange solutions during the lab sessions but you are
*not allowed* to share code electronically.

## Assignment submission

To prepare and submit your assignment, you will:
1. Ask your TA to give you access to the repository.
2. Fork the repository on GitHub.
3. In the settings of your fork, remove all contributors except (1) the course coordinator (username: `glatard`) (2) your TA. Failure to do so will be considered [unauthorized collaboration](http://www.concordia.ca/students/academic-integrity/offences.html) under Concordia's Academic Code of Conduct.
4. Clone your fork and implement the assignment (see [specific instructions](./ASSIGNMEENT.MD)).
5. Push your solution to your fork.
6. Release your fork on GitHub

Your code will be tested with Python 3.6.

## Specific instructions

Specific instructions to complete this assignment are available [here](./ASSIGNMENT.md).

## Grading

To grade your assignment, your TA will:
1. Clone the latest release of your forked GitHub repository.
2. Install any dependency with `pip install -r requirements.txt`.
3. Add undisclosed tests to directory `test`.
4. Run `pytest`.

Your grade will be determined from the number of passing tests as
returned by pytest. For instance, if 11 tests have passed out of 13,
your grade will be 84.6%.
