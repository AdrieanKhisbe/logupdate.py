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
    assert output[1].strip() == ""

def test_append_multiline_message():
    stream = io.StringIO()
    logupdate_function = logupdate.create(stream)
    logupdate_function("Hola\nQue tal?")
    logupdate_function("Bonchour\nFou Zallez bien?")
    logupdate_function("Bonjour\nCa va?")

    output = project_output(stream)
    assert output[0].strip() == "Bonjour"
    assert output[1].strip() == "Ca va?"

def test_append_wraptexted_message():
    stream = io.StringIO()
    logupdate_function = logupdate.create(stream)
    logupdate_function("hihi " * 16)
    logupdate_function(("haha " * 32).strip())

    output = project_output(stream)
    print(output)
    assert output[0].strip() == ("haha " * 16).strip()
    assert output[2].strip() == ("haha " * 16).strip()
    # for some reason in the screen there is an inserted newline.
    assert output[3].strip() == ""
    assert output[4].strip() == ""
