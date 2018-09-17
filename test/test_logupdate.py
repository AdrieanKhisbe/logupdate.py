from logupdate import logupdate
import io
from pyte import Screen, Stream

def project_output(stream):
    screen = Screen(80, 24)
    terminal_stream = Stream(screen)
    terminal_stream.feed(stream.getvalue())
    return screen.display

def test_append_simple_message():
    stream = io.StringIO()
    logupdate_function = logupdate.create(stream)
    logupdate_function("Hello")
    output = project_output(stream)
    assert output[0].strip() == "Hello"

def test_append_several_message():
    stream = io.StringIO()
    logupdate_function = logupdate.create(stream)
    logupdate_function("Hello")
    logupdate_function("Hola")
    logupdate_function("Bonchour")
    logupdate_function("Bonjour")

    output = project_output(stream)
    assert output[0].strip() == "Bonjour"
