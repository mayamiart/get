import time
import r2r_adc 
import adc_plot 
import plot_sampling_period_hist
r2r = r2r_adc.R2R_ADC(3.3,0.0001)
voltage_values=[]
time_values=[]
dur =6
try:
    start_time = time.time()
    while (time.time()-start_time)<dur:
        voltage_values.append(r2r.get_sc_voltage())
        time_values.append(time.time()-start_time)
    adc_plot.plot_voltage_vs_time(time_values, voltage_values, 3.3)
    plot_sampling_period_hist.plot_sampling_period_hist(time_values)
finally:
    del r2r
