import smbus
class MCP4725:
    def __init__(self, dynamic_range, address=0x61, verbose = True):
        self.bus = smbus.SMBus(1)
    
        self.address = address
        self.wm = 0x00
        self.pds = 0x00
    
        self.verbose = verbose
        self.dynamic_range = dynamic_range

    def deinit(self):
        self.bus.close()

    def set_number(self, number):
        if not isinstance(number, int):
            print("На вход ЦАП можно подавать только целые числа")

        if not (0 <= number <= 4095):
            print("Число выходит за разраядность MCP4752 (12 бит)")

        first_byte = self.wm | self.pds | number >> 8
        second_byte = number & 0xFF
        self.bus.write_byte_data(0x61, first_byte, second_byte)

        if self.verbose:
            print(f"Число: {number}, отправленные по I2C данные: [0x{(self.address << 1):02X}, 0x{first_byte:02X}, 0x{second_byte:02X}]\n")
    def set_voltage(self, voltage):
        if not isinstance(voltage, (int,float)):
           print('Not int or float')
           return
        if voltage<0:
            print('under 0')
        if voltage>self.dynamic_range:
            print('more than dynamic range')
        max_code=4095
        code=int((voltage/self.dynamic_range)*max_code)
        self.set_number(code)
    
if __name__ == "__main__":
    dac = MCP4725(5.04)
    try:
       while True:
            try:
                voltage = float(input('Enter in Volts '))
                dac.set_voltage(voltage)
            except ValueError as mtg:
                print(f"{mtg}\nNot number. Try again\n")
    finally:
        dac.deinit()