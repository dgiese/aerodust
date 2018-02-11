import lcm
from position_type import pos_t

def my_handler(channel, data):
    msg = post_t.decode(data)
    print("Received message on channel \"%s\"" % channel)
    print("\tTimestamp \"%s\"" % str(msg.timestamp))
    print("\tPosition \"%s\"" % str(msg.position))
    print("\tsignal_strength \"%s\"" % str(msg.signal_strength))
    print("")

lc = lcm.LCM("udpm://239.255.76.67?ttl=1")
subscription = lc.subscribe("Example", my_handler)

try:
    while True:
        lc.handle()
except KeyboardInterrupt:
    pass
