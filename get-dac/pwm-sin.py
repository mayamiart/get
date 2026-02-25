import pwm_dac as pwmd
import signal_generator as sg
import time
amplitude = 3
signal_frequency = 10
sampling_frequency = 10000
if __name__=="__main__":
    dac=pwmd.PWM_DAC(12, 500, 3.3, True)
    try:
        t=0.0
        while True:
            try:
                norm_amp = sg.get_sin_wave_amplitude(signal_frequency, t)
                dac.set_voltage(norm_amp * amplitude)
                sg.wait_for_sampling_period(sampling_frequency)
                t+=1.0/sampling_frequency
            except KeyboardInterrupt:
                print('Stop')
    finally:
        dac.deinit()   