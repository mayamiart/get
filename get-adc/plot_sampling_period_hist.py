import matplotlib.pyplot as plt

def plot_sampling_period_hist(time):
    sampling_periods =[]
    for i in range(1,len(time)):
        period = time[i]-time[i-1]
        sampling_periods.append(period)
    plt.figure(figsize=(10,6))
    plt.hist(sampling_periods)
    plt.title('Period')
    plt.xlim(0, 0.06)
    plt.ylim(0,3.5)
    plt.grid()
    plt.show()

