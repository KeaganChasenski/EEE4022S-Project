#!/usr/bin/env python3
import numpy as np

def main():
    
    y = 1.991976 # Wave length and 150.5MHz
    pi = np.pi
    d = 1.19 # 119cm 1.19m Spacing of antenna 


    ### Read data from files ###
    a1_data = np.fromfile('a1_data.iq', np.complex64)  # complex64, from Antenna 1
    a2_data = np.fromfile('a2_data.iq', np.complex64)  # complex64 from Antenna 2


    ### Remove start portion ###
    startindex = 100000
    endindex = 200000
    a1_clipped = a1_data[startindex:endindex]
    a2_clipped = a2_data[startindex:endindex]
    
    ### Remove DC value from LO ###
    mean1 = np.mean(a1_clipped)
    mean2 = np.mean(a2_clipped)

    a1_dc = a1_clipped - mean1
    a2_dc = a2_clipped - mean2 
    
    ### FFT data ###
    A1 = np.fft.fft(a1_clipped)
    A1_shift = np.fft.fftshift(A1)

    A2 = np.fft.fft(a2_clipped)
    A2_shift = np.fft.fftshift(A2)


    ### Find Signal in FFT ###
    ### Get max from within Signal ###
    signal_start = 18000
    signal_end = 23000
    maxsignal_1 = np.argmax(A1_shift[signal_start:signal_end]) +signal_start
    maxsignal_2 = np.argmax(A2_shift[signal_start:signal_end]) + signal_start



    ### Get Phase Difference ###
    p1 = A1_shift[maxsignal_1]
    p2 = A2_shift[maxsignal_2]

    Z = p1 * np.conj(p2)
    phase_diff = np.angle(Z)


    ### Calculate AoA ###
    x = (y * phase_diff) / (2 * pi * d)
    AoA_rad = np.arcsin(x)
    AoA_deg = AoA_rad * 180/pi 


    ### Display values ###

    #print("############################")
    #print("Phase difference: ", phase_diff)
    #print("Angle of arrival in rad: ", AoA_rad)
    #print("AoA in deg: ", AoA_deg, "\n")
    #print("############################")
    
    return AoA_deg

if __name__ == '__main__':
    main()
    
    
    
