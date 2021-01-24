# advent-of-code
Advent of code challenges

## [2020](./advent_2020)

### General approach
For my first advent code I wanted to do it in the language I know best - python. I went for a test driven development
style approach and tried to be as pythonic as possible without much refactoring.

My general approach was to sketch out some types and function names while reading the problem then writing failing
tests, then write code to make the tests pass.

### Problems and take aways
I found myself in some case over-engineering in anticipation of the second part of the question in terms of the 
abstractions I created, which I will try to avoid in future AOCs but when it did work out it was rather satisfying.

Day 13 part b took a while as my tests didn't capture a key edge case which caused a bit of trying to optimize an 
infinite loop... Will try to assume my tests are ineffective rather than that my code is inefficient in future.  

### Running it

Paths are configured assuming we run from the root directory e.g.
```bash
# tests
python -m unittest
python -m unittest advent_2020/tests/test_day_2.py
# run
python advent_2020/day_2.py
```
