import mcp4725_driver as mcp
import signal_generator as sg
import time
amplitude = 4.5
signal_frequency = 10
sampling_frequency = 10000
if __name__=="__main__":
    dac=mcp.MCP4725(5.04)
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