# AdventOfCode

Collection of task completed in [AdventOfCode](https://adventofcode.com/) in various programming languages, such as JavaScript, Python, Rust etc.

## Table of contents
- [AdventOfCode](#adventofcode)
  - [Table of contents](#table-of-contents)
  - [TODO](#todo)
  - [Dependencies](#dependencies)
  - [Workflow](#workflow)
    - [Bash help commands](#bash-help-commands)
  - [Formatting](#formatting)
    - [Virtual environment](#virtual-environment)
    - [Pre commit hooks](#pre-commit-hooks)
    - [Generate Python requirements file](#generate-python-requirements-file)

## TODO
- Complete 2024
- 2023 not imported yet (on the Mac I think)
- Complete tasks in more languages
- Implement commands for more languages
- TODO add rust (and JS?) checks in pre-commit hook
- Add templates for Python and Javascript
- Create section on [Formatting](#formatting)
- TODO fix all file/folder paths in this document, relative to where they are supposed to be, like templates on line 44

## Dependencies

- Bun for Javascript, install with:
```bash
powershell -c "irm bun.sh/install.ps1|iex" # https://bun.sh/docs/installation
```

- Rust, install here: <https://www.rust-lang.org/tools/install>

## Workflow

These commands expects the script file to be named `solution.*` depending on the programming language (currently supported, `Python` and `JavaScript`), i.e. `solution.js` and `solution.py`. For Rust, go into the years folder, and the run `cargo new dayX` to create a new file, remove the `main.rs` file, and create `bin/part1.rs` and `bin/part2.rs` to start working.

The input files are expected to be named as:
- `test.txt` - Test input
- `in.txt` - Large input

In the [templates](/templates/) folder there are templates for all used languages to get a start for creating the solutions.

### Bash help commands

After doing the information above the following commands can be run for various purposes, depending on the programming language:
- `aoc-load $1 $2` - Tries to fetch the input data from the [AdventOfCode](https://adventofcode.com/) website and write it to `in.txt`. Requires cookie token from website to be active and set.
- Python
    - `aot` - Runs `solution.py` with `test.txt` as input (output in blue)
    - `aos` - Runs `solution.py` with `in.txt` as input
    - `aoc` - Runs `aot` and `aos`
- JavaScript
    - `jaos` - Runs `solution.js` with `test.txt` as input (output in blue)
    - `jaot` - Runs `solution.js` with `in.txt` as input
    - `jaoc` - Runs `jaot` and `jaos`
- Rust
    - `raos <day> <part>` - Runs `<day>/bin/<part>.rs` with `test.txt` as input, where `<day>` and `<part>` is just the integer of the day, e.g. `raos 7 1`
    - `raot <day> <part>` - Runs `day<day>/bin/part<part>.rs` with `in.txt` as input, where `<day>` and `<part>` is just the integer of the day, e.g. `raos 7 1`
    - `raoc <day> <part>` - Runs `raot <day> <part>` and `raos <day> <part>`, where `<day>` and `<part>` is just the integer of the day, e.g. `raos 7 1`

```bash
# Add these to your ~/.bash_aliases
AOC="D:/workspace/AdventOfCode/2024" # change this to whatever your AOC directory is
AOC_COOKIE="" # get this from the cookies tab in network tools on the AOC website

alias aot="cd $AOC; echo -ne '\\e[0;34m'; python solution.py < test.txt; echo -ne '\\e[0m'"
alias aos="cd $AOC; python solution.py < in.txt"
alias aoc="aot; echo; aos"

alias jaos="cd $AOC; bun solution.js in.txt"
alias jaot="cd $AOC; bun solution.js test.txt"
alias jaoc="jaot; echo; jaos"

alias raos="rao in.txt"
alias raot="rao test.txt"
alias raoc="raoc_func"

function raoc_func() {
    raot "$1" "$2" && echo && raos "$1" "$2"
}

function rao () {
    prev_dir=$(pwd)
    if [ $2 ]
    then
        cd $AOC
        cd day$2
        if [ $3 ]
        then
            cargo run --bin part$3 $AOC/$1
        else
            echo "Usage: rao <input_file> <day> <part>"
            echo "Please provide which part to run"
        fi
    else
        echo "Usage: rao <input_file> <day> <part>"
        echo "Please provide which day to run"
    fi
    cd $prev_dir
}

function aoc-load () {
    if [ $1 ]
    then
        curl --cookie "session=$AOC_COOKIE" https://adventofcode.com/$1/day/$2/input > in.txt
    else
        curl --cookie "session=$AOC_COOKIE" "$(echo `date +https://adventofcode.com/%Y/day/%d/input` | sed 's/\/0/\//g')" > in.txt
    fi
}
```

Then run e.g. `exec bash` or `source /path/to/.bashrc` to activate the changes.

## Formatting

TODO

### Virtual environment

To create and activate the virtual environment, install the requirements, run:

```bash
#python -m pip install --upgrade pip # Optional steps
#python -m pip install --upgrade virtualenv
python -m venv ./venv
source venv/bin/activate
source venv/Scripts/activate # Windows
pip install -r requirements.txt --upgrade

deactivate # To exit the environment
```

### Pre commit hooks

This repository runs several scripts and checks before a commit can be created. Check [.git-hooks](.git-hooks/) for what is actually run.

To activate the git hooks locally run this command:
```bash
git config --local core.hooksPath .git-hooks
```

### Generate Python requirements file

The requirements in [requirements.txt](requirements.txt) is created by `pip-compile` command.

When you add a new package add it to [requirements.in](requirements.in) and then follow the instructions above in [Virtual environment](#virtual-environment) chapter and then run:

```bash
pip-compile --no-emit-index-url --output-file requirements.txt requirements.in
```