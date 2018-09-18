# logupdate.py

[![PyPI](https://img.shields.io/pypi/v/logupdate.svg)](https://pypi.org/project/logupdate/)
[![Supported Python Versions](https://img.shields.io/pypi/pyversions/logupdate.svg)](https://pypi.python.org/pypi/logupdate)
[![Build Status](https://travis-ci.org/AdrieanKhisbe/logupdate.py.svg?branch=master)](https://travis-ci.org/AdrieanKhisbe/logupdate.py)

> Log by overwriting the previous output in the terminal. 
> Useful for rendering progress bars, animations, etc.
> (Port of [sindresorhus/log-update](https://github.com/sindresorhus/log-update) from js to python)

## Install
Just pip install it, and you're good to go.

```bash
pip install logupdate
```

## Usage
```python
from logupdate import logupdate
from time import sleep

logupdate("Hello, a secret is about to be said to you")
sleep(1)
logupdate("You can pimp your interactive commands with logupdate")
sleep(1)
logupdate("Don't forget the secret ;)")
sleep(1)
logupdate.clear()
```

## Examples

You can find some example in the dedicated [examples](./examples) folder.

## API
- `logupdate(text, ...)`: log to stdout (overwriting previous input)
- `logupdate.clear()`: Clear previous logged output
- `logupdate.done()`: Persist the logged output. This enable to start a new "log session" below.

- `logupdate.stderr(text, ...)`: log to stderr
- `logupdate.stderr.clear()`: clear stderr
- `logupdate.stderr.done()`:  persist stderr

- `logupdate.create(stream, [options])` : return a `logupdate` method dedicated to log to given `stream`. Options, dict with key `show_cursor` (default to `False`)

# License
MIT © [AdrieanKhisbe](https://github.com/AdrieanKhisbe)
