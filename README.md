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
logupdate.clear().done()
```

## Examples

You can find some example in the dedicated [examples](./examples) folder.

## API
- `logupdate(text, ...)`: log to stdout (overwriting previous input)
- `logupdate.clear([restore_cursor=None])`: Clear previous logged output. This can also restore the cursor if asked.
- `logupdate.done([restore_cursor=None])`: Persist the logged output. This enable to start a new "log session" below.
  This restores the cursor unless you ask not to.

- `logupdate.stderr(text, ...)`: log to stderr
- `logupdate.stderr.clear([restore_cursor=None])`: clear stderr.
- `logupdate.stderr.done([restore_cursor=None])`:  persist stderr.

- `logupdate.create(stream, [show_cursor=False])` : return a `logupdate` method dedicated to log to given `stream`.

## License
MIT © [AdrieanKhisbe](https://github.com/AdrieanKhisbe)
