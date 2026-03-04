import matplotlib.pyplot as plt
def plot_voltage_vs_time(time, voltage, max_voltage):
    plt.figure(figsize=(10,6))
    plt.plot(time,voltage)
    plt.xlabel('Time, s', fontsize=12)
    plt.ylabel('Voltage, V', fontsize=12)
    plt.xlim(0, 6)
    plt.ylim(0, 3.5)
    plt.grid()
    plt.legend()
    plt.show()

