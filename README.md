# AdventOfCode

Collection of task completed in [AdventOfCode](https://adventofcode.com/) in various programming languages, such as JavaScript, Python etc

TODO: 
- Complete 2024
- 2023 not imported yet
- Complete tasks in more languages
- Implement commands for more languages
- TODO add how to install bun and other dependencies
- TODO add more info about the commands

## Dependencies

Bun for Javascript

## Commands

These commands expects the script file to be named `solution.*` depending on the programming language (currently supported, `Python` and `JavaScript`), i.e. `solution.js` and `solution.py`.

The input files are expected to be named as:
- `test.txt` - Test input
- `in.txt` - Large input

Then the following commands can be run for various purposes, depending on the programming language:
- `aoc-load $1 $2` - Tries to fetch the input data from the [AdventOfCode](https://adventofcode.com/) website and write it to `in.txt`. Requires token from website to be active
- Python
    - `aos` - 
    - `aot` - 
    - `aoc` - 
- JavaScript
    - `jaos` - 
    - `jaot` - 
    - `jaoc` - 


```bash
# Add these to your ~/.bash_aliases
AOC="D:/workspace/AdventOfCode/2024" # remember to change this to whatever your AOC directory is
AOC_COOKIE="" # get this from the cookies tab in network tools on the AOC website

alias aos="cd $AOC; python solution.py < in.txt"
alias aot="cd $AOC; echo -ne '\\e[0;34m'; python solution.py < test.txt; echo -ne '\\e[0m'"
alias aoc="aot; echo; aos"

alias jaos="cd $AOC; bun solution.js in.txt"
alias jaot="cd $AOC; bun solution.js test.txt"
alias jaoc="jaot; echo; jaos"

function aoc-load () {
    if [ $1 ]
    then
        curl --cookie "session=$AOC_COOKIE" https://adventofcode.com/$1/day/$2/input > in.txt
    else
        curl --cookie "session=$AOC_COOKIE" "$(echo `date +https://adventofcode.com/%Y/day/%d/input` | sed 's/\/0/\//g')" > in.txt
    fi
}
```