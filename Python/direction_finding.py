#!/usr/bin/env python3

import time 
import numpy as np
import store_IQ
import AoA_calculation
import matplotlib
from matplotlib import pyplot as plt

print("############################")
print("Starting Direction Finding...")

angle_degrees = np.zeros(100)
counter = 0

plt.figure(figsize=(15,5))
plt.title("Angle of Arrival in degrees")

#while True:
for i in range(20):
    store_IQ.main()
    time.sleep(0.3)
    AoA_deg = AoA_calculation.main()
    angle_degrees[counter] = AoA_deg
    
    plt.clf()
    plt.plot(angle_degrees)
    plt.pause(0.05)
    counter += 1
    #time.sleep(3)
    
plt.show()
print("############################")
print("Average Angle = ", np.average(angle_degrees))
print("Ending Direction Finding Application...")
print("############################")
    
    
    
