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
    log = logupdate.create(stream)
    log("Hello")
    output = project_output(stream)
    assert output[0].strip() == "Hello"

def test_append_several_message():
    stream = io.StringIO()
    log = logupdate.create(stream)
    log("Hello")
    log("Hola")
    log("Bonchour")
    log("Bonjour")

    output = project_output(stream)
    assert output[0].strip() == "Bonjour"
    assert output[1].strip() == ""

def test_append_multiline_message():
    stream = io.StringIO()
    log = logupdate.create(stream)
    log("Hola\nQue tal?")
    log("Bonchour\nFou Zallez bien?")
    log("Bonjour\nCa va?")

    output = project_output(stream)
    assert output[0].strip() == "Bonjour"
    assert output[1].strip() == "Ca va?"

def test_append_wraptexted_message():
    stream = io.StringIO()
    log = logupdate.create(stream)
    log("hihi " * 16)
    log(("haha " * 32).strip())

    output = project_output(stream)
    print(output)
    assert output[0].strip() == ("haha " * 16).strip()
    assert output[2].strip() == ("haha " * 16).strip()
    # for some reason in the screen there is an inserted newline.
    assert output[3].strip() == ""
    assert output[4].strip() == ""
