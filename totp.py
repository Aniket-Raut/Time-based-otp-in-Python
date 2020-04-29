import hashlib
import hmac
import struct
import base64
import time
import os

def getOtp():
    while True:
        detect_os()
        #os.system('cls')
        key="cml6 4636 tqdv ecet hchw 4x6z qqot 2h52" #Enter your key here
        format_key(key)
        decoded = base64.b32decode(format_key(key), True) # here is the decoded key
        epoch_time = time.time() # getting current epoch time
        interval = int(epoch_time /30) # getting interval
        msg = struct.pack(">Q", interval)
        digested = bytearray(hmac.new(decoded, msg, hashlib.sha1).digest())
        offset = digested[19] & 15
        otp = str((struct.unpack(">I", digested[offset:offset + 4])[0] & 0x7fffffff) % 1000000)
        check_length(otp)

def format_key(key):
    nkey =key.strip().replace(' ','')
    return nkey

def detect_os():
    if os.name=='nt':
        print("windows:")
        os.system('cls')
    else:
        print("not windows")
        os.system('clear')

def check_length(otp):
    if len(otp)<6:
        required_zeros=6-len(otp)
        print(required_zeros)
        newotp='0'*required_zeros+otp
        print("OTP is:"+newotp)
    else:
        print("OTP is:"+otp)


if __name__ == '__main__':
    getOtp()
