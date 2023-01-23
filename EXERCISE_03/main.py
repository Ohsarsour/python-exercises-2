import numpy as np
random_numbers = np.random.random(size=5)
print(random_numbers)
print("Mean:{}".format(np.average(random_numbers)),"Median:{}".format(np.median(random_numbers)),"Standard Deviation:{}".format(np.std(random_numbers)))