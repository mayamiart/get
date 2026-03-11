import time
import mcp3021_driver
import adc_plot 
import plot_sampling_period_hist
mcp = mcp3021_driver.MCP3021(5)
voltage_values=[]
time_values=[]
dur =6
try:
    start_time = time.time()
    while (time.time()-start_time)<dur:
        voltage_values.append(mcp.get_voltage())
        time_values.append(time.time()-start_time)
    adc_plot.plot_voltage_vs_time(time_values, voltage_values, 3.3)
    plot_sampling_period_hist.plot_sampling_period_hist(time_values)
finally:
    del mcp