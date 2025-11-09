import numpy as np

def moving_average(arr, window_size=3):
    results = []
    for i in range(len(arr) - window_size + 1):
        window_slice = arr[i: i + window_size] # gets the window slice
        window_average = np.mean(window_slice) # averages it
        results.append(window_average) # adds it to our list
    return np.array(results)

with open('303_Lab8_P2.txt', 'r') as f:
    data_line = f.readline()
    window_line = f.readline()

data_array = np.fromstring(data_line, sep=' ') # turns line into np array
window_val = int(window_line.strip()) # gets window line

result_array = moving_average(data_array, window_val) # calculates

np.savetxt('BME303_Lab8_P2_JohnTan-Aristy.txt', [result_array], fmt='%g', delimiter=' ')