# pygrep

This project was created and named similar, since grep does not support capturing regular expression groups.

If no groups are specified the match will be just printed.

If capturing groups are specified, the groups are printed out with the given seperator.

```
$ ./pygrep.py -h
usage: pygrep.py [-h] -f FILE -r REGEX [-s SEPERATOR] [-D]

pygrep

optional arguments:
  -h, --help            show this help message and exit
  -f FILE, --file FILE  Input file
  -r REGEX, --regex REGEX
                        Regular expression string
  -s SEPERATOR, --sep SEPERATOR
                        Output seperator for captured groups (default: '|')
  -D, --debug           Enable debug.
```
