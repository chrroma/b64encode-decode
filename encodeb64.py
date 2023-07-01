import base64
import time
from pic import luffy

print(luffy)

while True:
    e_or_d = input("would you like to decode or encode? ")
    if e_or_d == "stop":
        break
    if e_or_d == "encode" or e_or_d == "encode":
        encode = input("enter text to encode here: ")
        encoded = base64.b64encode(encode.encode())
        print(encoded)
        time.sleep(1)
    elif e_or_d == "decode" or e_or_d == "Decode":
        dec = input("enter text to decode here: ")
        decoded = base64.b64decode(dec.encode())
        print(decoded)
        time.sleep(1)

