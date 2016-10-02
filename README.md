# Objective and How to Use

The point of this repository is that you clone it, program your answers, make a pull request, and then get Travis results telling you how many tests you passed. That is the sense in which these are automated tests that "grade" answers to Project Euler questions.

## Links

In the first pass, I'm looking at a dumb drop-in of answers from other places on the web. Here are some sources of answers with notes:

 - (MIT license, many utilities, not same test objective) https://github.com/iKevinY/EulerPy
 - (incompatible license) https://github.com/nayuki/Project-Euler-solutions/blob/master/Answers.txt
 - (MIT license, about 83 worked) https://github.com/kdungs/euler

The point of this is not to solve the questions. It is to use the obvious tools to build a testing mechanism.

# Obfuscated testing

Part of the fun of this repo might be solving a "reverse" problem. That is,
writing a program for each problem that somehow algorithmically tests
the correctness of the answer, based on the problem statement.

As an example, if the question asked "find the number that is a common factor
of both X and Y", then the test function should reasonably test that
X is divisible by the answer, and that Y is divisible by the answer.
Such methods do not necessarily have to divulge anything about the solution.

Some problems are easier than others to implement this philosophy for.

