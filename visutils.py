import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import csv
import ipywidgets as wd

def load_and_prepare_cmd(filename):
    data = np.loadtxt("fieldA.csv", delimiter=',', skiprows = 1)
    g_mag = data[:,2] #Taking all of the g mags
    r_mag = data[:,3] #Taking all of the r mags
    indexes = np.where((g_mag > 14) & (g_mag < 24)) 
    g1 = g_mag[indexes] 
    r1 = r_mag[indexes] 
    g_minus_r = g1 - r1
    
    gr_indexes = np.where((g_minus_r > -0.5) & (g_minus_r < 2.5)) 
    gr = g_minus_r[gr_indexes]
    g = g1[gr_indexes]
    return g, gr
    fieldA = pd.read_csv("fieldA.csv").values

(g, gr) = load_and_prepare_cmd("fieldA.csv")

gridsize_slider = wd.FloatSlider(
    value = 50,
    min = 50.0,
    max = 300.0,
    step = 1)

def interactive_hess(grid_values):
    fig, ax = plt.subplots(
        figsize = (15,15),
        constrained_layout = True)

    ax.tick_params(axis='both',which='major',labelsize = 18)

    ax.set_xlabel("G - R",
                  fontfamily = 'serif',
                  fontsize = 25)

    ax.set_ylabel("G_Mag",
                  fontfamily = 'serif',
                  fontsize = 25)

    ax.invert_yaxis()

    ax.set_title("302 Homework CMD",
                 fontfamily = 'serif',
                 fontsize = 30)
    
    graph = ax.hexbin(gr, g, gridsize=grid_values, bins = 'log', cmap = 'inferno')
    bar_color = fig.colorbar(graph, ax=ax)
    bar_color.set_label('counts')
    plt.show()


plot = wd.interactive(interactive_hess, grid_values = gridsize_slider)

plot
    
    
    
