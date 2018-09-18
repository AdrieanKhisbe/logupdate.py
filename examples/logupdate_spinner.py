from logupdate import logupdate
from time import sleep

frames = ['-', '\\', '|', '/']

i = 0
try:
    while True:
        i = (i+1) % len(frames)
        frame = frames[i]
        logupdate(
f"""
        ♥♥
   {frame} unicorns {frame}
        ♥♥
"""
        )
        sleep(0.08)
except:
    logupdate.clear()