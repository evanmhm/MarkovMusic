# MarkovMusic

[![Python 2.7][python-img]][python-url]

This is a project using python and markov chains to analyze midi files and output markov generated music. Currently, it works, however, I have not put in the effort to make it include empty space or work properly with multiple simultaneous notes.

## How to Run

Before running install dependencies using the text file and pip command:

```bash
$ sudo -H pip install -r requirements.txt
```

Then run the program using:

```bash
$ python run.py
```

The file "rebuilt.mid" is then generated from a markov chain of the input file defined in `src/app.py`

## Options

Currently there is only one option flag `-v` or `--verbose` for verbose. Verbose prints more in depth values of the process. If you forget the options `-h` or `--help` will give descriptions.

[python-img]: https://img.shields.io/badge/python-2.7-blue.svg?style=flat-square
[python-url]: https://www.python.org/downloads
