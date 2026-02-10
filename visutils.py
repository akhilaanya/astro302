import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import csv
import ipywidgets as wd

def load_and_prepare_cmd(filename):
    data = np.loadtxt("fieldA.csv", delimiter=',', skiprows = 1)
    g_mag = data[:,2] #Taking all of the g mags
    r_mag = data[:,3] #Taking all of the r mags
    g = np.where((data[:,2] > 14) & (data[:,2] < 24)) #Selecting desired g mags
    g_minus_r = g_mag - r_mag
    gr = np.where((g_minus_r > -0.5) & (g_minus_r < 2.5))
    fieldA = pd.read_csv("fieldA.csv").values

(g, gr) = load_and_prepare_cmd('fieldA.csv')

def interactive_hess(g,gr):
    fig, axs = plt.subplots(
        figsize = (15,15),
        constrained_layout = True)

    ax.tick_params(axis='both',which='major',labelsize = 18)

    ax.set_xlabel("G - R",
                  fontfamily = 'serif',
                  fontsize = 25)

    ax.set_ylabel("G_Mag",
                  fontfamily = 'serif',
                  fontsize = 25)

    ax.set_title("302 Homework CMD",
                 fontfamily = 'serif',
                 fontsize = 30)

    ax.plot(g_mag, g_minus_r,
            color = "purple",
            marker = "o",
            linestyle = "None",
            markersize = 5);
    
    gridsize_slider = wd.FloatSlider(
        value = 2.0,
        min = 50.0,
        max = 300.0,
        step = 1,
        bins = 'log')

interactive_hess()
    
    
    
