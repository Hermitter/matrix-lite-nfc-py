import _matrix_hal_nfc as hal
# from matrix_lite_nfc import read
import time
import asyncio

# print(nfc.read)
reader = hal.read()

def read_callback(code, tag):
    print(code,hal.status(code))
    print(tag.info)
    print(tag.page)

reader.read_nfc({
    "rate": 1000,
    "info": True,
    "page": 0,
},read_callback)




# def read_nfc(code,tag):
#     print("nfc status:",code)
#     print(tag.info)

# def led_loop():
#     everloop = [{}] * led.length
#     everloop[0] = {'b':100}
#     while True:
#         print("led moving", everloop[0])
#         everloop.append(everloop.pop(0))
#         led.set(everloop)
#         time.sleep(0.05)

# start main
# led_loop()