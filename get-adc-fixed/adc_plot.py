from matplotlib import pyplot as plt

def plot_voltage_vs_time(time,voltage,max_voltage):
    plt.figure(figsize=(10,6))
    plt.plot(time,voltage)
    plt.title("Зависимость напряжения от времени")
    plt.ylabel("Напряжение, В")
    plt.xlabel("Время, с")
    plt.grid(True)
    plt.ylim(0,max_voltage)
    plt.xlim(min(time), max(time))
    plt.show()
def plot_sampling_period_hist(time):
    timeizm = []
    for i in range(len(time)-1):
        timeizm.append(time[i+1]-time[i])
    plt.figure(figsize=(10,6))
    plt.hist(timeizm)
    plt.title("Распределение периодов времени")
    plt.ylabel("Количество измерений")
    plt.xlabel("Период измерения")
    plt.grid(True)
    plt.xlim(0,0.06)
    plt.show()