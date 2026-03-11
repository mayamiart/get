import RPi.GPIO as GPIO
import time
class R2R_ADC:
    def __init__(self, dynamic_range, compare_time = 0.01, verbose = False):
        self.dynamic_range = dynamic_range
        self.verbose = verbose
        self.compare_time = compare_time
        
        self.bits_gpio = [26, 20, 19, 16, 13, 12, 25, 11]
        self.comp_gpio = 21

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.bits_gpio, GPIO.OUT, initial = 0)
        GPIO.setup(self.comp_gpio, GPIO.IN)
    def __del__(self):
        try:
            self.number_to_dac(0)
            GPIO.cleanup()
            if self.verbose:
                print('Set 0')
        except RuntimeError:
            print('Runtime')
    def number_to_dac(self, number):
        a = [int(i) for i in bin(number)[2:].zfill(8)]
        for i in range(len(a)):
            GPIO.output(self.bits_gpio[i], a[i])
    def sequential_counting_adc(self):
        for value in range(255+1):
            self.number_to_dac(value)
            time.sleep(self.compare_time)
            comparator_output = GPIO.input(self.comp_gpio)
            if comparator_output==1:
                return value
        return 255
    def get_sc_voltage(self):
        digital_value = self.sequential_counting_adc()
        step = self.dynamic_range/255.0
        voltage = step*digital_value
        if self.verbose:
            print(digital_value, step, voltage)
        return voltage
    def successive_approximation_adc(self):
        low=0
        high=255
        value=0
        while (high-low)>1:
            value=(high+low)//2
            self.number_to_dac(value)
            time.sleep(0.001)
            if GPIO.input(self.comp_gpio)==1:
                high=value
            else:
                low=value
        return value
    def get_sar_voltage(self):
        digital_value = self.successive_approximation_adc()
        voltage = (digital_value/255)*self.dynamic_range
        return voltage

if __name__ == "__main__":
    adc=None
    try:
       adc=R2R_ADC(3.2, 0.01, True)
       while True:
           #voltage = adc.get_sc_voltage()
           #print("real", voltage)
           voltage = adc.get_sar_voltage()
           print(f'Volts:{voltage}')
    except KeyboardInterrupt:
        print("Stop")
    finally:
        if adc:
            del adc
        print('End')