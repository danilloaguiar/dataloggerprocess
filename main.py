from numpy.random import randn
from numpy.fft import rfft
from scipy import signal
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np



#parameters 
CSV = 'RUN2.csv'
Acquisition_Frequency = 150
n_cel= 50
fc1, fc2 = 60*Acquisition_Frequency/n_cel, 60*Acquisition_Frequency/n_cel

#filter
b, a = signal.butter(2, 0.2, analog=False)
# Show that frequency response is the same
impulse = np.zeros(1000)
impulse[500] = 1
# Applies filter forward and backward in time
imp_ff = signal.filtfilt(b, a, impulse)
# Applies filter forward in time twice (for same frequency response)
imp_lf = signal.lfilter(b, a, signal.lfilter(b, a, impulse))



#oppening csv and saving in variable 
df = pd.read_csv(CSV)
tabela1, tabela2 = df.set_index('f1'), df.set_index('f2')
f1, f2 =tabela1.index.values, tabela2.index.values
d1, d2 = [fc1*sum(f1[i*n_cel:i*n_cel+n_cel]) for i in range(round(len(f1)/n_cel))],  [fc1*sum(f2[i*n_cel:i*n_cel+n_cel]) for i in range(round(len(f2)/n_cel))]



plt.subplot(2, 2, 1)
plt.plot(d1)
plt.minorticks_on()
plt.grid(which='major', linestyle='-', linewidth='0.5', color='black')
plt.grid(which='minor', linestyle=':', linewidth='0.5', color='black')
plt.xlabel('legenda x')
plt.ylabel('legenda y')



plt.subplot(2, 2, 3)
plt.plot(d2)
plt.minorticks_on()
plt.grid(which='major', linestyle='-', linewidth='0.5', color='black')
plt.grid(which='minor', linestyle=':', linewidth='0.5', color='black')
plt.xlabel('legenda x')
plt.ylabel('legenda y')



plt.subplot(2, 2, 2)
sig_ff = signal.filtfilt(b, a, d1)
plt.plot(d1, color='silver', label='Original')
plt.plot(sig_ff, color='#3465a4', label='filtfilt')
plt.minorticks_on()
plt.grid(which='major', linestyle='-', linewidth='0.5', color='black')
plt.grid(which='minor', linestyle=':', linewidth='0.5', color='black')
plt.legend(loc="best")


plt.subplot(2, 2, 4)
sig_ff = signal.filtfilt(b, a, d2)
plt.plot(d2, color='silver', label='Original')
plt.plot(sig_ff, color='#3465a4', label='filtfilt')
plt.minorticks_on()
plt.grid(which='major', linestyle='-', linewidth='0.5', color='black')
plt.grid(which='minor', linestyle=':', linewidth='0.5', color='black')
plt.legend(loc="best")

plt.show()

