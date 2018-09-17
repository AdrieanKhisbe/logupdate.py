import sys
import cursor
from ansiwrap import wrap
from shutil import get_terminal_size

ESC = "\u001B["

def erase_lines(count):
    return "".join([
         (ESC + "2K") # erase Line
       + (ESC + "1A" if i < count -1 else "") # cursor up
        for i in range(count)
    ]) + ESC + "G"

class LogUpdate():

    def __init__(self, stream, options = None):
        self.options = {"show_cursor": False, **(options or {})}
        self.stream = stream
        self.prev_line_count = 0

    def __call__(self, *message):
        if not self.options["show_cursor"]:
            cursor.hide()
        lines = wrap(" ".join(message),
                     get_terminal_size().columns or 80,
                     drop_whitespace=False,   # trim
			         break_long_words=False)  # wordWrap
        self.stream.write(erase_lines(self.prev_line_count) + "\n".join(lines) + "\n")
        self.prev_line_count = 1 + len(lines)

    def clear(self):
        self.stream.write(erase_lines(self.prev_line_count))
        self.prev_line_count = 0

    def done(self):
        self.prev_line_count = 0
        if not self.options["show_cursor"]:
            cursor.show()

logupdate = LogUpdate(sys.stdout)
logupdate.stderr = LogUpdate(sys.stderr)
logupdate.create = LogUpdate
