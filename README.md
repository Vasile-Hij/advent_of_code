# Advent of code

![AdventOfCode](https://img.shields.io/badge/Advent%20Of%20Code-2022-blue?style=flat-square) [![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://img.shields.io/github/license/Vasile-hij/pyAOC-2022?style=flat-square) ![GitHub top Language](https://img.shields.io/github/languages/count/Vasile-hij/pyAOC-2022?style=flat-square) ![GitHub commit activity](https://img.shields.io/github/commit-activity/w/Vasile-Hij/pyAOC-2022)

`This is the most wonderful time of the year - Andy Williams`

This repository is built on python that run with poetry making all configs that you need automatically: creates directories, 
scripts, request HTML page from Advent of Code site and downloaded in 'src/cached_html', taking 'input', 'sample file' 
from 'src/input' and send back 'result' to the AoC page and pass the day filling the input on to the page (the last part is on progress).


1. Clone and cd to root project then:
`$ poetry install`, then `poetry shell` to activate the environment;

2. Two ways of run it when you need creating files and populate them with data:

    A. *Automatically*: go on Chrome Browser on [Advent of Code](https://adventofcode.com/) and choose [GitHub] as a sign in option
     (only this method it is available for now).

    B. *Manually*: add input manually: `input/{year}/day{day}.txt` and `input/{year}/day{day}_sample.txt`.

   Note: If you want to use project with your own inputs and different approach in solving problems, you have to remove 
   anything in directory 'py/', except 'script_example.txt'; then in directory 'src/' remove completely 'input/' 
   and 'cached_html/'. Then add manually the input into the files as in 2.B step.

3. Run:
$`python main.py -v <yearday>` e.g: `python main.py -v 2201` '22' represent year 2022 and '01' is day 01.

   If no year is mentioned, it will be taken automatically last year available: `python main.py -v 01`. 
   In this case '22' is the last year available for 'day01'.

4. Testing:
For testing sample input add '-s s': `python main.py -v 2201 -s s`


 
| Day                                    | Name                    | Solution             | Part 1    | Part 2    | Stars |
|----------------------------------------|-------------------------|----------------------|-----------|-----------|-------|
| [01](data/cached_html/2022/day1.html)  | Calorie Counting        | [py](py/22/day01.py) | 66487     | 197301    | **    |
| [02](data/cached_html/2022/day2.html)  | Rock Paper Scissors     | [py](py/22/day02.py) | 13446     | 13509     | **    |
| [03](data/cached_html/2022/day3.html)  | Rucksack Reorganization | [py](py/22/day03.py) | 8053      | 2425      | **    |
| [04](data/cached_html/2022/day4.html)  | Camp Cleanup            | [py](py/22/day04.py) | 433       | 852       | **    |
| [05](data/cached_html/2022/day5.html)  | Supply Stacks           | [py](py/22/day05.py) | JRVNHHCSJ | GNFBSBJLH | **    |
| [06](data/cached_html/2022/day6.html)  | Turning Trouble         | [py](py/22/day06.py) | 1287      | 3716      | **    |
| [07](data/cached_html/2022/day7.html)  | No Space Left On Device | [py](py/22/day07.py) | 1367870   | 549173    | **    |
| [08](data/cached_html/2022/day8.html)  | Treetop Tree House      | [py](py/22/day08.py) | 1533      | 345744    | **    |
| [09](data/cached_html/2022/day9.html)  |                         | [py](py/22/day09.py) |           |           |       |
| [10](data/cached_html/2022/day10.html) |                         | [py](py/22/day10.py) |           |           |       |
| [11](data/cached_html/2022/day11.html) |                         | [py](py/22/day11.py) |           |           |       |
| [12](data/cached_html/2022/day12.html) |                         | [py](py/22/day12.py) |           |           |       |
| [13](data/cached_html/2022/day13.html) |                         | [py](py/22/day13.py) |           |           |       |
| [14](data/cached_html/2022/day14.html) |                         | [py](py/22/day14.py) |           |           |       |
| [15](data/cached_html/2022/day15.html) |                         | [py](py/22/day15.py) |           |           |       |
| [16](data/cached_html/2022/day16.html) |                         | [py](py/22/day16.py) |           |           |       |
| [17](data/cached_html/2022/day17.html) |                         | [py](py/22/day17.py) |           |           |       |
| [18](data/cached_html/2022/day18.html) |                         | [py](py/22/day18.py) |           |           |       |
| [19](data/cached_html/2022/day19.html) |                         | [py](py/22/day19.py) |           |           |       |
| [20](data/cached_html/2022/day20.html) |                         | [py](py/22/day20.py) |           |           |       |
| [21](data/cached_html/2022/day21.html) |                         | [py](py/22/day21.py) |           |           |       |
| [22](data/cached_html/2022/day22.html) |                         | [py](py/22/day22.py) |           |           |       |
| [23](data/cached_html/2022/day23.html) |                         | [py](py/22/day23.py) |           |           |       |
| [24](data/cached_html/2022/day24.html) |                         | [py](py/22/day24.py) |           |           |       |
| [25](data/cached_html/2022/day25.html) |                         | [py](py/22/day25.py) |           |           |       |


### Changelog (see [GitHub issues](https://github.com/Vasile-Hij/advent_of_code/issues?q=is%3Aissue+sort%3Aupdated-desc+is%3Aclosed)):
- [x] [#1](https://github.com/Vasile-Hij/advent_of_code/issues/1) Poetry environment
- [x] [#2](https://github.com/Vasile-Hij/advent_of_code/issues/2) Run script from command line v0.1
- [x] [#3](https://github.com/Vasile-Hij/advent_of_code/issues/3) Refactor day 01 - 04 to run with command line now
- [x] [#4](https://github.com/Vasile-Hij/advent_of_code/issues/4) Refactor run command line v0.2 to accept more functions
- [x] [#7](https://github.com/Vasile-Hij/advent_of_code/issues/7) Refactor day 01-07 to run with command line v2
- [x] [#9](https://github.com/Vasile-Hij/advent_of_code/issues/9) Automate scripts and input file
- [x] [#10](https://github.com/Vasile-Hij/advent_of_code/issues/10) Get input data from AoC in HTML format
- [x] [#16](https://github.com/Vasile-Hij/advent_of_code/issues/16) Cache AOC's HTML storyline and input
- [x] [#17](https://github.com/Vasile-Hij/advent_of_code/issues/17) Migrate project from functions to classes (bonus: coloured print)
- [x] Test methods (continuously to be update it)
- [x] [#19](https://github.com/Vasile-Hij/advent_of_code/issues/19) Submit result to AOC


### TO DO'S:
    1. find a pattern to automate downloading multiple examples when given and chose the right one required for testing solution
