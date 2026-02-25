import numpy as np
import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
def get_sin_wave_amplitude(freq, t):
    raw = np.sin(2*np.pi*freq*t)
    shifted = raw+1
    normal = shifted/2
    return normal
def wait_for_sampling_period(sampling_freq):
    period = 1.0/sampling_freq
    time.sleep(period)
