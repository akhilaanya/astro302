import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import csv

def load_and_prepare_cmd(filename):
    data = np.loadtxt("fieldA.csv", delimiter=',', skiprows = 1)
    g_mag = data[:,2] #Taking all of the g mags
    r_mag = data[:,3] #Taking all of the r mags
    g = np.where((data[:,2] > 14) & (data[:,2] < 24)) #Selecting desired g mags
    g_minus_r = g_mag - r_mag
    gr = np.where((g_minus_r > -0.5) & (g_minus_r < 2.5))
    fieldA = pd.read_csv("fieldA.csv").values

(g, gr) = load_and_prepare_cmd('fieldA.csv')
