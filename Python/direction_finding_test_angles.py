#!/usr/bin/env python3

# Keagan Chasenski
# CHSKEA001@myuct.ac.za
# 21/10/2021
# Direction Finding Thesis


### import statements ###
import time
import numpy as np
import AoA_calculation
import matplotlib
from matplotlib import pyplot as plt
import csv
import sys

### Starting prints ###
print("############################")
print("Starting Direction Finding...")

### Create CSV file, writer and header columns ###
f = open("Testing_AoA.csv", "w")
writer = csv.writer(f)
headers = ['Defined Angle', 'Calculated Angle']
writer.writerow(headers)

### Loop until 'quit' entered ###
while True:

    ### User input for defined angle ###
    defined_angle = input("Please enter the defined angle of arrival. \n")

    ### Break out of loop on 'quit' ###
    if defined_angle == 'quit':
        break

    ### Blank array for angles, average taken ###
    angle_degrees = np.zeros(50)
    counter = 0

    ### Loop for iterations for average angle ###
    for i in range(50):
        #store_IQ.main()
        time.sleep(0.3)

        ### call calcualtion program, AoA returned ###
        AoA_deg = AoA_calculation.main()

        ### Add to array ###
        angle_degrees[counter] = AoA_deg
        counter += 1

    ### Write pair of defined angle and calculated angle to CSV ###
    angle_avg = np.average(angle_degrees)
    writer.writerow([defined_angle,angle_avg])

    ### User Display ###
    print("############################")
    print("Average Angle = ", angle_avg)

### End program gracefully ###
print("Ending Direction Finding Application...")
print("############################")
f.close()

