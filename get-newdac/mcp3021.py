import smbus
import time

dynamic_range = 5

class MCP3021:
    def __init__(self, dynamic_range, address=0x4d, verbose = True):
        self.bus = smbus.SMBus(1)
        time.sleep(1)
        self.address = address
        self.wm = 0x00
        
        self.pds = 0x00

        self.verbose = verbose
        self.dynamic_range = dynamic_range

    def read(self):
        res = self.bus.read_word_data(self.address, 0)
        msb = res & 0xFF
        lsb = (res>>8) & 0xFF
        numb = msb<<8 + lsb<<2 
        return numb

    def deinit(self):
        self.bus.close()
           
if __name__ == "__main__":
    try:
        dac = MCP3021(dynamic_range)
        while True:
            print(dac.read())
            time.sleep(1)
    finally:
        dac.deinit()
