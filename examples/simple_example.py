from logupdate import logupdate
from time import sleep

logupdate("Hello")("Hola")
sleep(2)
logupdate("Hello You")
logupdate.done()
sleep(1)
logupdate("I'm gonna leave")
sleep(1)
logupdate("Bye")
sleep(1)
logupdate("Powered by logupdate ;)")
sleep(1)
logupdate.clear().done()


