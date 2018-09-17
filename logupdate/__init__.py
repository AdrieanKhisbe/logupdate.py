import sys
import cursor
from ansiescapes import eraseLines



class LogUpdate():

    def __init__(self, stream, options = None):
        self.options = {"show_cursor": False, **(options or {})}
        self.stream = stream
        self.prev_line_count = 0

    def render(self, *message):
        if not self.options["show_cursor"]:
            cursor.hide()
        output = " ".join(message) + "\n"
        print(eraseLines(self.prev_line_count))
        stream.write(eraseLines(self.prev_line_count) + output)
        self.prev_line_count = len(output.split("\n"))

    def __call__(self, *message):
        self.render(*message)

logupdate = LogUpdate(sys.stdout)