
import numpy as np
import time


def read_slope_alignment():
    values = np.linspace(0, 0.4, 20)

    for i in values:
        with open('test.dat') as f:
            line = f.readlines()
            to_change = line[13]
            line[13] = f"Slope_Align = {round(i,3)} \n"
            print(line[13])

        with open('test.dat', 'w') as file:
            file.writelines(line)
        time.sleep(1)


read_slope_alignment()
