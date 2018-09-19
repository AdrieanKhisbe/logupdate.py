import sys
import cursor
from ansiwrap import wrap
from shutil import get_terminal_size

ESC = "\u001B["

def erase_lines(count):
    """
    Produce the ANSI code to erase COUNT lines.
    """
    return "".join([
         (ESC + "2K") # erase Line
       + (ESC + "1A" if i < count -1 else "") # cursor up
        for i in range(count)
    ]) + ESC + "G"

class LogUpdate():
    """
    LogUpdate enables to Log by overwriting the previous output in a stream.
    """
    def __init__(self, stream, show_cursor=None):
        """
        Create a LogUpdate instance on the given stream.

        Will hide cursor by default but it's possible to
        preserve it with the `show_cursor=True` option.
        """
        self.show_cursor = show_cursor
        self.stream = stream
        self.prev_line_count = 0

    def __call__(self, *message):
        """
        Log the given MESSAGE.

        This will overwrite the previous outputed message.

        You can provide several arguments, they will be joined
        with a space character
        """
        if not self.show_cursor:
            cursor.hide()
        paragraphs = [wrap(line,
                     get_terminal_size().columns or 80,
                     drop_whitespace=False,   # trim
                     replace_whitespace=False,
                     break_long_words=False)  # wordWrap
                     for line in " ".join(message).splitlines()]
        lines = [l for line in paragraphs for l in line]
        self.stream.write(erase_lines(self.prev_line_count) + "\n".join(lines) + "\n")
        self.prev_line_count = 1 + len(lines)
        return self

    def clear(self, restore_cursor=None):
        """
        Erase the previously logged lines.

        This will only affect the log since the last done() call.

        You can eventualy decide to restore the cursor by giving
        the `restore_cursor=True` keyword argument.
        """
        self.stream.write(erase_lines(self.prev_line_count))
        if restore_cursor:
            cursor.show()
        self.prev_line_count = 0
        return self

    def done(self, restore_cursor=None):
        """
        Persist the logged output.

        This enable to start a new "log session" below.

        You can eventualy decide to control the cursor restoring
        with the option `restore_cursor=True/False`.
        By default it will restore the cursor if it was hidden.
        Use `restore_cursor=False` to keep it hidden
        """
        self.prev_line_count = 0
        if restore_cursor if (restore_cursor is not None) else not self.show_cursor:
            cursor.show()
        return self

logupdate = LogUpdate(sys.stdout)
logupdate.stderr = LogUpdate(sys.stderr)
logupdate.create = LogUpdate
