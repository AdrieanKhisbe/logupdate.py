from logupdate import logupdate
from time import sleep

logupdate("This is gonna be...")
sleep(1)
logupdate("This is gonna be a very very very long example")
sleep(3)
logupdate("This is gonna be a very very very long example with very very long lines that span over terminal size")
sleep(3)
logupdate(
    """This is gonna be a very very very long example with very very long lines that span over terminal size
And that use also multilines!""")
sleep(3)

logupdate.clear()
logupdate("Voilà").done()
