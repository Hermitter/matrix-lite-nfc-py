import _matrix_hal_nfc as nfc
# from matrix_lite_nfc import read
import time
import asyncio

########################
##  SIMPLE READ FUNC  ##
# reader = nfc.reader()

# results = reader.scan({"rate": 1000,"info": True,"pages": True,"ndef": True,"page": 0,})

msg = nfc.Message()
msg.addTextRecord("Hello")
msg.addTextRecord("Hola", "es")
msg.addUriRecord("https://community.matrix.one")
msg.addMimeMediaRecord("text/json", '{"answer": 42}')

# print(msg.__dir__())
# print(msg.toString(),'\n')
# print(msg.getRecordCount(),"\n*")

print(msg.getRecords())