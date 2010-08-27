import time
import create

SERIAL_PORT = "/dev/ttyUSB0"
r = create.Create( SERIAL_PORT )

r.playSong( [(70,32),(72,16),(74,16),(75,16),(74,16),(70,16),(65,32),(68,32),(70,16),(68,16),(67,32),(65,32)] )
time.sleep(3) # Give Katamari time to finish

for i in 'go':    
    r.playSong( [(60,8),(64,8),(67,8),(72,8)] )
    time.sleep(1) # Give C chord time to finish

for i in range(8,24,8):
    r.playSong( [(55,i),(57,i),(59,i),(60,i),(62,i),(64,i),(66,i),(67,i),(67,i),(66,i),(64,i),(62,i),(60,i),(59,i),(57,i),(55,i)] )
    time.sleep(3) # Give G scale time to finish

r.shutdown()
