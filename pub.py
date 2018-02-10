import lcm
from position_type import pos_t

lc = lcm.LCM()

msg = pos_t()
msg.timestamp = 7
msg.position = (7,7,7)
msg.signal_strength = 75

try:
    lc.publish("Example", msg.encode())
    print("Publish sucessfull!")
except Exception as e:
    print("Publish not sucessful")
