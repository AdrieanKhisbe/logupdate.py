from logupdate import logupdate
import io
from subprocess import run, PIPE

def test_append_simple_message():
    stream = io.StringIO()
    logupdate_function = logupdate.create(stream)
    logupdate_function("Hello")

    output = run(["echo", "-n", stream.getvalue()], shell=stdout=PIPE)
    print(output)
    print(output.stdout)
    print(output.stderr)
    print(dir(output))
    assert output == "Hello\n"